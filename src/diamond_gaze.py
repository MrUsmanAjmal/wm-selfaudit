"""Which patch should the agent look at? Gaze policies for closed-loop feedback on DIAMOND (Atari), on a CPU.

For every game the pretrained agent plays NEW real episodes (a different seed from src/diamond_audit.py). Every policy
is run on the same windows with the same random numbers, as two parallel rollouts per window, so policies can be
compared clip by clip. After each predicted frame, each rollout is shown k real 16x16 patches of that frame.

Policies (all but the oracle use only what the agent has before it looks, and keep a uniform floor eps, so the
patches still give an unbiased drift estimate):
  random       uniform
  motion       root-mean-square change of the patch since the previous frame (the earlier "guided" gaze)
  disagree     root-mean-square difference between the two parallel rollouts
  pred_vis     predicted patch error from texture, motion and time
  pred_all     predicted patch error from disagreement, texture, motion and time
  combo        geometric mean of the (normalised) motion and disagreement scores: high only where both are high
  oracle       the k patches with the largest true error (not deployable)
A suffix _e30 raises the uniform floor from 10% to 30% (lighter importance weights, so a more reliable drift estimate).

The error predictors are linear models fit on the open-loop rollouts of src/diamond_audit.py (other episodes) with the
same code as the audit (src/wm_audit.py), then frozen.

    python src/diamond_gaze.py --diamond <diamond repo> --fit-data <diamond_audit.py output> --out <data dir>
"""
import argparse
import json
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diamond_audit import CONTEXT, PATCH, TRAINED_HORIZON, load_game, play_episodes, save, setup
from wm_audit import FEATURES_PAIR, FEATURES_VISUAL, build_units, context_frames, fit_models, load_condition

POLICIES = ["random", "motion", "disagree", "pred_vis", "pred_all", "oracle", "disagree_e30", "combo", "combo_e30"]
BUDGET_POLICIES = ["random", "motion", "pred_all", "oracle"]


def patch_vectors(x):
    """(B, C, H, W) in [-1, 1] -> (B, J, P*P*C) in [0, 1], patches in the same order as wm_audit.patchify."""
    b, c, h, w = x.shape
    x = (x + 1) / 2
    return x.reshape(b, c, h // PATCH, PATCH, w // PATCH, PATCH).permute(0, 2, 4, 3, 5, 1).reshape(b, -1, PATCH * PATCH * c)


def features(x, prev, other, k, H):
    """Observation-free features of every patch, as in wm_audit.build_units: dict name -> (B, J)."""
    g, gp, go = patch_vectors(x), patch_vectors(prev), patch_vectors(other)
    return dict(texture=g.var(-1, unbiased=False), motion=((g - gp) ** 2).mean(-1),
                time=torch.full(g.shape[:2], (k + 1) / H), disagreement_pair=((g - go) ** 2).mean(-1))


def predicted_error(f, w, names):
    z = torch.stack([f[n] for n in names] + [torch.ones_like(f["time"])], -1).double()
    return (z @ torch.as_tensor(w)).float()


def gaze_probs(policy, f, models, eps):
    """Sampling probabilities over patches. A suffix _eNN sets the uniform floor to NN%."""
    J = f["time"].shape[1]
    if "_e" in policy:
        policy, eps = policy.split("_e")[0], int(policy.split("_e")[1]) / 100
    if policy == "random":
        return torch.full_like(f["time"], 1.0 / J)
    norm = lambda v: v / (v.mean(1, keepdim=True) + 1e-12)
    s = {"motion": f["motion"].sqrt(), "disagree": f["disagreement_pair"].sqrt(),
         "combo": (norm(f["motion"].sqrt()) * norm(f["disagreement_pair"].sqrt())).sqrt(),
         "pred_vis": predicted_error(f, models["pred_vis"], FEATURES_VISUAL).clamp(min=0),
         "pred_all": predicted_error(f, models["pred_all"], FEATURES_PAIR).clamp(min=0)}[policy] + 1e-12
    return (1 - eps) * s / s.sum(1, keepdim=True) + eps / J


@torch.no_grad()
def paired_rollout(sampler, ctx, acts, real, policy=None, k=1, models=None, eps=0.1, gen=None):
    """Two rollouts per window, run as one batch (chain a = first B, chain b = last B). Each chain is shown its own k
    patches per frame. Returns predictions (2B, H, ...) made before the patches of that frame are shown, and for k = 1
    the chosen patch and its probability (H, 2B)."""
    B, H = real.shape[:2]
    ctx2, acts2, real2 = ctx.repeat(2, 1, 1, 1, 1), acts.repeat(2, 1), real.repeat(2, 1, 1, 1, 1)
    buf = ctx2.clone()
    w = real.shape[-1] // PATCH
    preds, chosen, probs = [], [], []
    for t in range(H):
        x, _ = sampler.sample(buf, acts2[:, t:t + CONTEXT])
        x = x.clamp(-1, 1)
        preds.append(x.clone())
        if policy is not None:
            other = torch.cat([x[B:], x[:B]])
            if policy == "oracle":
                err = ((patch_vectors(x) - patch_vectors(real2[:, t])) ** 2).mean(-1)
                j = err.topk(k, dim=1).indices
                q = torch.ones(2 * B, k)
            else:
                q_all = gaze_probs(policy, features(x, buf[:, -1], other, t, H), models, eps)
                j = torch.multinomial(q_all, k, replacement=False, generator=gen)
                q = q_all.gather(1, j)
            for b in range(2 * B):
                for jj in j[b].tolist():
                    r, c = divmod(jj, w)
                    rows, cols = slice(r * PATCH, (r + 1) * PATCH), slice(c * PATCH, (c + 1) * PATCH)
                    x[b, :, rows, cols] = real2[b, t, :, rows, cols]
            chosen.append(j[:, 0].numpy())
            probs.append(q[:, 0].numpy())
        buf = torch.cat([buf[:, 1:], x[:, None]], 1)
    out = torch.stack(preds, 1)
    if policy is None or k > 1:
        return out, None, None
    return out, np.stack(chosen), np.stack(probs)


def fit_game(fit_data, name):
    clips = load_condition(os.path.join(fit_data, name))[0]
    units = build_units(clips, PATCH, context_frames(clips))
    return {"pred_vis": fit_models(units, FEATURES_VISUAL)[0], "pred_all": fit_models(units, FEATURES_PAIR)[0]}


def conditions(budgets):
    out = [("open", None, 1)] + [(f"{p}_k1", p, 1) for p in POLICIES]
    out += [(f"{p}_k{k}", p, k) for k in budgets if k > 1 for p in BUDGET_POLICIES]
    return out


def run_game(cfg, game, fit_data, out, episodes, horizon, seed, budgets, log):
    name = game.lower()
    conds = conditions(budgets)
    todo = [c for c in conds if not all(os.path.exists(f"{out}/{name}_{c[0]}/run_{r}/batch_000.npz") for r in (0, 1))]
    if not todo:
        log(f"{game}: done already")
        return
    models = fit_game(fit_data, name)
    t0 = time.time()
    env, agent, sampler, _ = load_game(cfg, game)
    eps_, tried = play_episodes(env, agent, episodes, CONTEXT + horizon + 1, seed)
    rng = np.random.default_rng(seed)
    starts = [int(rng.integers(0, len(A) - CONTEXT - horizon + 1)) for _, A in eps_]
    T = CONTEXT + horizon
    gt = torch.stack([O[s:s + T] for (O, _), s in zip(eps_, starts)])
    acts = torch.stack([A[s:s + T - 1] for (_, A), s in zip(eps_, starts)])
    clips = [[i, s] for i, s in enumerate(starts)]
    ctx, real = gt[:, :CONTEXT], gt[:, CONTEXT:]
    B = len(clips)
    log(f"{game}: {B} new episodes (of {tried} played), {time.time() - t0:.0f}s")
    for cname, policy, k in todo:
        torch.manual_seed(seed + 7)  # the same sampler noise for every policy: paired comparisons
        gen = torch.Generator().manual_seed(seed + 11)
        t1 = time.time()
        pred, gz, q = paired_rollout(sampler, ctx, acts, real, policy, k, models, gen=gen)
        for r, sl in enumerate((slice(0, B), slice(B, 2 * B))):
            save(f"{out}/{name}_{cname}/run_{r}/batch_000.npz", torch.cat([ctx, pred[sl]], 1), gt, clips,
                 None if gz is None else gz[:, sl], None if q is None else q[:, sl])
        log(f"{game}: {cname} in {time.time() - t1:.0f}s")


def write_plan(out, games, budgets):
    plan = dict(reference=f"{games[0].lower()}_open", model="DIAMOND (Atari 100k pretrained), gaze study", conditions={})
    for g in games:
        n = g.lower()
        for cname, policy, k in conditions(budgets):
            c = dict(label=f"{g}: {cname}", patch=PATCH, trained_frames=CONTEXT + TRAINED_HORIZON, fit_on=f"{n}_open")
            if policy:
                c.update(gaze="oracle" if policy == "oracle" else policy, patches_per_frame=k, role="feedback")
            plan["conditions"][f"{n}_{cname}"] = c
    json.dump(plan, open(f"{out}/plan.json", "w"), indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--diamond", required=True)
    ap.add_argument("--fit-data", required=True, help="output folder of src/diamond_audit.py (predictors are fit there)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--games", nargs="+", default=["Breakout", "Pong", "Boxing", "MsPacman", "Seaquest", "Freeway",
                                                   "Asterix", "RoadRunner"])
    ap.add_argument("--episodes", type=int, default=32)
    ap.add_argument("--horizon", type=int, default=30)
    ap.add_argument("--budgets", type=int, nargs="+", default=[1, 2, 4])
    ap.add_argument("--seed", type=int, default=50000)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    torch.set_num_threads(os.cpu_count())
    cfg = setup(os.path.abspath(a.diamond))
    logf = open(os.path.join(a.out, "generation.log"), "a")

    def log(msg):
        line = f"[{time.strftime('%H:%M:%S')}] {msg}"
        print(line, flush=True)
        logf.write(line + "\n")
        logf.flush()

    write_plan(a.out, a.games, a.budgets)
    for gi, game in enumerate(a.games):
        run_game(cfg, game, a.fit_data, a.out, a.episodes, a.horizon, a.seed + 100000 * gi, a.budgets, log)
    log("all games done")


if __name__ == "__main__":
    main()
