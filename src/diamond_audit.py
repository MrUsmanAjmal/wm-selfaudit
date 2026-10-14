"""Second world model: DIAMOND (Alonso et al., NeurIPS 2024) on Atari, with the official pretrained models.

For every game, the pretrained agent plays real episodes in the real Atari environment. From one random window per
episode, the world model is rolled out from 4 real frames with the actions that were really taken, so its rollout
can be compared with what actually happened:

  - open loop: 3 independent rollouts per window (audit, calibration, self-assessment);
  - closed loop: 2 rollouts per window and gaze policy, with one real 16x16 patch (1/16 of the 64x64 frame) pasted
    into every predicted frame before it conditions the next one.

Rollouts are saved in the same format as the Diffusion Forcing dumps, so src/wm_audit.py analyses them unchanged.
Runs on a CPU. Needs the DIAMOND repository and its requirements (Python <= 3.12).

    python src/diamond_audit.py --diamond <path to diamond repo> --out <data dir> --games Breakout Pong
"""
import argparse
import json
import os
import sys
import time

import numpy as np
import torch

PATCH = 16
CONTEXT = 4
TRAINED_HORIZON = 15
S_CHURN = 1.0  # stochastic-sampler control: EDM churn noise added at every denoising step


def setup(diamond):
    sys.path.insert(0, os.path.join(diamond, "src"))
    from hydra import compose, initialize_config_dir
    from omegaconf import OmegaConf
    OmegaConf.register_new_resolver("eval", eval, replace=True)
    with initialize_config_dir(version_base="1.3", config_dir=os.path.join(diamond, "config")):
        return compose(config_name="trainer")


def load_game(cfg, game):
    import gymnasium
    from huggingface_hub import hf_hub_download
    from hydra.utils import instantiate
    from omegaconf import OmegaConf
    from agent import Agent
    from envs.atari_preprocessing import AtariPreprocessing
    from models.diffusion import DiffusionSampler

    cfg.agent = OmegaConf.load(hf_hub_download("eloialonso/diamond", "atari_100k/config/agent/default.yaml"))
    for attempt in range(10):
        try:
            ckpt = hf_hub_download("eloialonso/diamond", f"atari_100k/models/{game}.pt")
            break
        except Exception as e:
            print(f"download of {game}.pt failed ({type(e).__name__}); retry {attempt + 1}", flush=True)
            time.sleep(20 * (attempt + 1))
    else:
        raise SystemExit(f"could not download the {game} model")
    env = gymnasium.make(f"{game}NoFrameskip-v4", full_action_space=False, frameskip=1, render_mode="rgb_array")
    env = AtariPreprocessing(env=env, noop_max=30, frame_skip=4, screen_size=64)
    agent = Agent(instantiate(cfg.agent, num_actions=env.action_space.n)).eval()
    agent.load(ckpt)
    sampler = DiffusionSampler(agent.denoiser, instantiate(cfg.world_model_env.diffusion_sampler))
    stoch_cfg = instantiate(cfg.world_model_env.diffusion_sampler)
    stoch_cfg.s_churn = S_CHURN
    stochastic = DiffusionSampler(agent.denoiser, stoch_cfg)
    assert cfg.agent.denoiser.inner_model.num_steps_conditioning == CONTEXT
    return env, agent, sampler, stochastic


def to_tensor(o):
    return torch.tensor(o).div(255).mul(2).sub(1).permute(2, 0, 1)


@torch.no_grad()
def play_episodes(env, agent, n, min_len, seed, max_steps=3000):
    """Real episodes with the pretrained agent: frames in [-1, 1] (L+1, 3, 64, 64) and actions (L,)."""
    episodes, k = [], 0
    while len(episodes) < n:
        torch.manual_seed(seed + k)
        obs, _ = env.reset(seed=seed + k)
        k += 1
        hx = cx = torch.zeros(1, agent.actor_critic.lstm_dim)
        O, A = [to_tensor(obs)], []
        for _ in range(max_steps):
            out = agent.actor_critic.predict_act_value(O[-1][None], (hx, cx))
            hx, cx = out.hx_cx
            a = torch.distributions.Categorical(logits=out.logits_act).sample().item()
            obs, _, term, trunc, _ = env.step(a)
            A.append(a)
            O.append(to_tensor(obs))
            if term or trunc:
                break
        if len(A) >= min_len:
            episodes.append((torch.stack(O), torch.tensor(A)))
    return episodes, k


def patch_means(x):
    b, c, h, w = x.shape
    return x.reshape(b, c, h // PATCH, PATCH, w // PATCH, PATCH).mean(dim=(1, 3, 5)).reshape(b, -1)


@torch.no_grad()
def rollout(sampler, ctx_obs, acts, real, gaze=None, eps=0.1, gen=None):
    """ctx_obs (B, 4, 3, 64, 64) real context; acts (B, 4 + H - 1) real actions; real (B, H, 3, 64, 64) real future.
    Returns predictions (B, H, ...) made before any patch of that frame is shown, and the chosen patches."""
    B, H = real.shape[:2]
    buf = ctx_obs.clone()
    preds, chosen, probs = [], [], []
    w = real.shape[-1] // PATCH
    J = (real.shape[-2] // PATCH) * w
    for k in range(H):
        x, _ = sampler.sample(buf, acts[:, k:k + CONTEXT])
        x = x.clamp(-1, 1)
        preds.append(x.clone())
        if gaze is not None:
            if gaze == "oracle":
                j = patch_means((x - real[:, k]) ** 2).argmax(1)
                q = torch.ones(B)
            else:
                if gaze == "random":
                    q_all = torch.full((B, J), 1.0 / J)
                else:
                    s = patch_means((x - buf[:, -1]) ** 2).sqrt() + 1e-12
                    q_all = (1 - eps) * s / s.sum(1, keepdim=True) + eps / J
                j = torch.multinomial(q_all, 1, generator=gen).squeeze(1)
                q = q_all.gather(1, j[:, None]).squeeze(1)
            for b in range(B):
                r, c = divmod(int(j[b]), w)
                rows, cols = slice(r * PATCH, (r + 1) * PATCH), slice(c * PATCH, (c + 1) * PATCH)
                x[b, :, rows, cols] = real[b, k, :, rows, cols]
            chosen.append(j.numpy())
            probs.append(q.numpy())
        buf = torch.cat([buf[:, 1:], x[:, None]], 1)
    out = torch.stack(preds, 1)
    return out, (np.stack(chosen) if chosen else None), (np.stack(probs) if probs else None)


def save(path, pred, gt, clips, gaze=None, q=None):
    """wm_audit format: (T, B, C, H, W) in [0, 1]. Full precision: DIAMOND's rollouts differ by less than float16 resolves."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    f = lambda x: ((x.clamp(-1, 1) + 1) / 2).permute(1, 0, 2, 3, 4).numpy().astype(np.float32)
    extra = {} if gaze is None else dict(gaze=gaze.astype(np.int16), q=q.astype(np.float32))
    tmp = path[:-4] + ".part.npz"
    np.savez_compressed(tmp, pred=f(pred), gt=f(gt), clips=np.array(clips, dtype=np.int64), **extra)
    os.replace(tmp, path)


def run_game(cfg, game, out, episodes, horizon, runs, fb_runs, seed, log):
    name = game.lower()
    todo = [f"{out}/{n}/run_{r}/batch_000.npz" for n in (name, f"{name}_stoch") for r in range(runs)] + \
           [f"{out}/{name}_fb_{g}/run_{r}/batch_000.npz" for g in ("guided", "random", "oracle") for r in range(fb_runs)]
    if all(os.path.exists(p) for p in todo):
        log(f"{game}: done already")
        return
    t0 = time.time()
    env, agent, sampler, stochastic = load_game(cfg, game)
    eps, tried = play_episodes(env, agent, episodes, CONTEXT + horizon + 1, seed)
    rng = np.random.default_rng(seed)
    starts = [int(rng.integers(0, len(A) - CONTEXT - horizon + 1)) for _, A in eps]
    T = CONTEXT + horizon
    gt = torch.stack([O[s:s + T] for (O, _), s in zip(eps, starts)])
    acts = torch.stack([A[s:s + T - 1] for (_, A), s in zip(eps, starts)])
    clips = [[i, s] for i, s in enumerate(starts)]
    log(f"{game}: {len(eps)} episodes (of {tried} played), lengths {min(len(A) for _, A in eps)}-"
        f"{max(len(A) for _, A in eps)} steps, {time.time() - t0:.0f}s")
    ctx, real = gt[:, :CONTEXT], gt[:, CONTEXT:]
    for si, (cond, smp) in enumerate(((name, sampler), (f"{name}_stoch", stochastic))):
        for r in range(runs):
            path = f"{out}/{cond}/run_{r}/batch_000.npz"
            if os.path.exists(path):
                continue
            torch.manual_seed(seed + 1000 + 100 * si + r)
            t1 = time.time()
            pred, _, _ = rollout(smp, ctx, acts, real)
            save(path, torch.cat([ctx, pred], 1), gt, clips)
            log(f"{game}: open-loop rollout {r}{' (stochastic sampler)' if si else ''} in {time.time() - t1:.0f}s")
    for gi, g in enumerate(("guided", "random", "oracle")):
        for r in range(fb_runs):
            path = f"{out}/{name}_fb_{g}/run_{r}/batch_000.npz"
            if os.path.exists(path):
                continue
            torch.manual_seed(seed + 2000 + 10 * gi + r)
            gen = torch.Generator().manual_seed(seed + 3000 + 10 * gi + r)
            t1 = time.time()
            pred, gz, q = rollout(sampler, ctx, acts, real, gaze=g, gen=gen)
            save(path, torch.cat([ctx, pred], 1), gt, clips, gz, q)
            log(f"{game}: {g} feedback rollout {r} in {time.time() - t1:.0f}s")


def write_plan(out, games, horizon):
    plan = dict(reference=games[0].lower(), model="DIAMOND (Atari 100k pretrained)", horizon=horizon, conditions={})
    for g in games:
        n = g.lower()
        plan["conditions"][n] = dict(label=g, patch=PATCH, trained_frames=CONTEXT + TRAINED_HORIZON, fit_on=n)
        plan["conditions"][f"{n}_stoch"] = dict(label=f"{g}, stochastic sampler", patch=PATCH,
                                                trained_frames=CONTEXT + TRAINED_HORIZON, fit_on=f"{n}_stoch",
                                                s_churn=S_CHURN)
        for gaze, lab in (("guided", "Guided gaze"), ("random", "Random gaze"), ("oracle", "Oracle gaze (not deployable)")):
            plan["conditions"][f"{n}_fb_{gaze}"] = dict(label=f"{g}: {lab}", patch=PATCH, trained_frames=CONTEXT + TRAINED_HORIZON,
                                                        fit_on=n, gaze=gaze, role="feedback")
    json.dump(plan, open(f"{out}/plan.json", "w"), indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--diamond", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--games", nargs="+", default=["Breakout", "Pong", "Boxing", "MsPacman", "Seaquest", "Freeway",
                                                   "Asterix", "RoadRunner"])
    ap.add_argument("--episodes", type=int, default=32)
    ap.add_argument("--horizon", type=int, default=30)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--fb-runs", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0)
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

    write_plan(a.out, a.games, a.horizon)
    for gi, game in enumerate(a.games):
        run_game(cfg, game, a.out, a.episodes, a.horizon, a.runs, a.fb_runs, a.seed + 100000 * gi, log)
    log("all games done")


if __name__ == "__main__":
    main()
