"""Qualitative figure for the Minecraft gaze study: the same clip and frame under every gaze policy, for the clip with
the median and the clip with the worst drift ratio of motion x disagreement gaze against random gaze.

    python src/gaze_examples.py --data <wm_audit_data from notebook 07> --out results/closed_loop_gaze/fig_gaze_examples.png
"""
import argparse
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wm_audit import context_frames, load_condition

ap = argparse.ArgumentParser()
ap.add_argument("--data", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--patch", type=int, default=32)
a = ap.parse_args()
cols = [("minecraft", "no feedback"), ("pair_random", "random gaze"), ("pair_motion", "motion gaze"),
        ("pair_disagree", "disagreement gaze"), ("pair_combo", "motion x disagreement")]
data = {n: {(c["video"], c["start"]): c for c in load_condition(os.path.join(a.data, n))[0]} for n, _ in cols}
keys = sorted(set.intersection(*[set(d) for d in data.values()]))
n_ctx = context_frames([data["pair_random"][k] for k in keys])
drift = lambda c: np.mean([((p[n_ctx:] - c["gt"][n_ctx:]) ** 2).mean() for p in c["preds"]])
ratio = np.array([drift(data["pair_combo"][k]) / drift(data["pair_random"][k]) for k in keys])
order = np.argsort(ratio)
picks = [(keys[order[len(order) // 2]], "median clip"), (keys[order[-1]], "worst clip")]
t = data["pair_random"][keys[0]]["gt"].shape[0] - 1
fig, axs = plt.subplots(len(picks), len(cols) + 1, figsize=(2.3 * (len(cols) + 1), 2.55 * len(picks)))
for row, (k, tag) in zip(axs, picks):
    gt = data["pair_random"][k]["gt"][t]
    row[0].imshow(np.clip(gt, 0, 1))
    row[0].set_title(f"real, frame {t - n_ctx + 1}", fontsize=8)
    row[0].set_ylabel(f"{tag}\n(ratio {ratio[keys.index(k)]:.2f})", fontsize=8)
    for ax, (n, lab) in zip(row[1:], cols):
        c = data[n][k]
        p = c["preds"][0][t]
        ax.imshow(np.clip(p, 0, 1))
        err = ((p - gt) ** 2).mean()
        ax.set_title(f"{lab}\nMSE {err:.3f}", fontsize=8)
        if "gaze" in c["extra"]:
            j = int(c["extra"]["gaze"][0][t - n_ctx])
            w = gt.shape[1] // a.patch
            r_, c_ = divmod(j, w)
            ax.add_patch(Rectangle((c_ * a.patch - 0.5, r_ * a.patch - 0.5), a.patch, a.patch, fill=False, ec="red", lw=1.5))
    for ax in row:
        ax.set_xticks([])
        ax.set_yticks([])
fig.tight_layout()
fig.savefig(a.out, dpi=150)
print("saved", a.out, "| clips", [p[0] for p in picks], "| ratios", [round(float(ratio[keys.index(p[0])]), 2) for p in picks])
