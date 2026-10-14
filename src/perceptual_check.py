"""Calibration and feedback measured with a perceptual distance (LPIPS) instead of pixel MSE.

For a calibrated model, reality and two rollouts are exchangeable draws from the same predictive distribution, so
E d(rollout, real) = E d(rollout, other rollout) for ANY distance d. The calibration ratio therefore does not depend
on pixel MSE, and LPIPS gives an independent check that is less sensitive to small misalignments.

    python src/perceptual_check.py --data <wm_audit_data> --out results/perceptual --conds minecraft minecraft_fast
    python src/perceptual_check.py --data <wm_audit_data from notebook 04> --out results/perceptual --feedback
"""
import argparse
import json
import os
import sys

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wm_audit import BIN_LABELS, ci, cluster_sets, context_frames, horizon_bins, load_condition, md_table


class Lpips:
    def __init__(self):
        import lpips
        self.net = lpips.LPIPS(net="alex", verbose=False).eval()

    @torch.no_grad()
    def __call__(self, a, b):
        """a, b: (T, H, W, 3) in [0, 1] -> (T,) LPIPS distances."""
        ta = torch.from_numpy(np.ascontiguousarray(a.transpose(0, 3, 1, 2))) * 2 - 1
        tb = torch.from_numpy(np.ascontiguousarray(b.transpose(0, 3, 1, 2))) * 2 - 1
        return self.net(ta, tb).reshape(-1).numpy().astype(np.float64)


def per_rollout(clips, n_ctx, dist):
    """err[c][r] and dis[c][r]: per-frame distance to reality and mean distance to the other rollouts."""
    err, dis = [], []
    for c in clips:
        P = [p[n_ctx:] for p in c["preds"]]
        g = c["gt"][n_ctx:]
        R = len(P)
        pair = {(r, s): dist(P[r], P[s]) for r in range(R) for s in range(r + 1, R)}
        err.append([dist(p, g) for p in P])
        dis.append([np.mean([pair[min(r, s), max(r, s)] for s in range(R) if s != r], axis=0) for r in range(R)])
    return err, dis


def calibration(data, conds, out, dist, B=5000):
    plan = json.load(open(os.path.join(data, "plan.json")))
    rows, summary = [], {}
    for name in conds:
        clips = load_condition(os.path.join(data, name))[0]
        if not clips:
            continue
        n_ctx = context_frames(clips)
        T = clips[0]["gt"].shape[0]
        bins = horizon_bins(T - n_ctx, plan["conditions"][name]["trained_frames"] - n_ctx)
        err, dis = per_rollout(clips, n_ctx, dist)
        videos = [c["video"] for c in clips for _ in c["preds"]]
        E = [e for ce in err for e in ce]
        D = [d for cd in dis for d in cd]
        sets = cluster_sets(videos, B=B)
        full = np.arange(len(E))
        summary[name] = {}
        for bn, sl in bins.items():
            sE = np.array([e[sl].sum() for e in E])
            sD = np.array([d[sl].sum() for d in D])
            rel = np.array([(d[sl].mean() - e[sl].mean()) / e[sl].mean() for e, d in zip(E, D)])
            ratio = lambda s: sE[s].sum() / sD[s].sum()
            bias = lambda s: 100 * rel[s].mean()
            r_ci, b_ci = ci(ratio, sets), ci(bias, sets)
            summary[name][bn] = dict(error_over_disagreement=float(ratio(full)), ratio_ci=r_ci,
                                     disagreement_bias_pct=float(bias(full)), bias_ci=b_ci,
                                     mean_error=float(sE.sum() / sum(e[sl].size for e in E)))
            rows.append([plan["conditions"][name]["label"], BIN_LABELS[bn], f"{ratio(full):.2f} ({r_ci[0]:.2f}-{r_ci[1]:.2f})",
                         f"{bias(full):+.1f} ({b_ci[0]:+.1f} to {b_ci[1]:+.1f})"])
        print(f"{name}: {len(clips)} clips done", flush=True)
    md = ("## Calibration with a perceptual distance (LPIPS)\n\nMean LPIPS(rollout, real) / mean LPIPS(rollout, other "
          "rollouts); 1 = calibrated for any distance. Bias: disagreement used as the drift estimate. 95% CI over videos.\n\n"
          + md_table(["Condition", "Frames", "Error / disagreement [95% CI]", "Bias of disagreement (%) [95% CI]"], rows) + "\n")
    return md, summary


def feedback(data, out, dist, base="minecraft", conds=("feedback_guided", "feedback_random", "feedback_oracle"), B=5000):
    plan = json.load(open(os.path.join(data, "plan.json")))
    load = lambda n: {(c["video"], c["start"]): c for c in load_condition(os.path.join(data, n))[0]}
    b = load(base)
    names = [n for n in conds if os.path.isdir(os.path.join(data, n))]
    fb = {n: load(n) for n in names}
    keys = sorted(set(b).intersection(*[set(fb[n]) for n in names]))
    n_ctx = context_frames([b[k] for k in keys])
    T = b[keys[0]]["gt"].shape[0]
    bins = horizon_bins(T - n_ctx, plan["conditions"][base]["trained_frames"] - n_ctx)
    drift = lambda c: np.mean([dist(p[n_ctx:], c["gt"][n_ctx:]) for p in c["preds"]], axis=0)
    base_d = np.array([drift(b[k]) for k in keys])
    sets = cluster_sets([k[0] for k in keys], B=B)
    full = np.arange(len(keys))
    rows, summary = [], {}
    for n in names:
        d = np.array([drift(fb[n][k]) for k in keys])
        summary[n] = {}
        for bn, sl in bins.items():
            x, y = d[:, sl].mean(1), base_d[:, sl].mean(1)
            ratio = lambda s, x=x, y=y: x[s].sum() / y[s].sum()
            r_ci = ci(ratio, sets)
            summary[n][bn] = dict(ratio=float(ratio(full)), ratio_ci=r_ci, clips_improved=float((x < y).mean()))
            rows.append([plan["conditions"][n]["label"], BIN_LABELS[bn], f"{y.mean():.3f}", f"{x.mean():.3f}",
                         f"{ratio(full):.2f} ({r_ci[0]:.2f}-{r_ci[1]:.2f})", f"{100 * (x < y).mean():.0f}%"])
        print(f"{n}: done", flush=True)
    md = ("## Feedback measured with LPIPS\n\nPerceptual drift of the model's prediction of each frame (LPIPS to the real "
          f"frame), with feedback / without, on {len(keys)} clips; 95% CI over videos.\n\n"
          + md_table(["Feedback", "Frames", "LPIPS without", "LPIPS with", "Ratio [95% CI]", "Clips improved"], rows) + "\n")
    return md, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="results/perceptual")
    ap.add_argument("--conds", nargs="*", default=[])
    ap.add_argument("--feedback", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    torch.set_num_threads(os.cpu_count() or 4)
    dist = Lpips()
    if a.feedback:
        md, s = feedback(a.data, a.out, dist)
        tag = "feedback"
    else:
        md, s = calibration(a.data, a.conds, a.out, dist)
        tag = "calibration"
    open(os.path.join(a.out, f"lpips_{tag}.md"), "w").write(md)
    json.dump(s, open(os.path.join(a.out, f"lpips_{tag}.json"), "w"), indent=2)
    print(md)


if __name__ == "__main__":
    main()
