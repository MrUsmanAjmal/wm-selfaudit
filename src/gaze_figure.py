"""Figure for the gaze study on DIAMOND: per-game drift relative to random gaze (1 patch per frame), and drift relative
to open loop as the number of patches per frame grows (geometric mean over games).

    python src/gaze_figure.py --summary results/diamond_gaze/gaze.json --out results/diamond_gaze/fig_gaze_atari.png
"""
import argparse
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--summary", required=True)
ap.add_argument("--out", required=True)
a = ap.parse_args()
s = json.load(open(a.summary))
games = list(s)
shown = [("motion", "Motion"), ("disagree", "Disagreement"), ("combo", "Motion x disagreement"), ("oracle", "Oracle (not deployable)")]
colors = ["C0", "C1", "C2", "0.55"]

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 3.6), gridspec_kw=dict(width_ratios=[2.2, 1]))
w = 0.8 / len(shown)
for i, (p, lab) in enumerate(shown):
    for gi, g in enumerate(games):
        r = s[g].get(f"{g}_{p}_k1")
        if not r or "vs_random" not in r:
            continue
        x = gi + (i - (len(shown) - 1) / 2) * w
        a1.bar(x, r["vs_random"], w, color=colors[i], label=lab if gi == 0 else None)
        a1.errorbar(x, r["vs_random"], yerr=[[r["vs_random"] - r["vs_random_ci"][0]], [r["vs_random_ci"][1] - r["vs_random"]]],
                    color="k", capsize=1.5, lw=0.7)
a1.axhline(1, color="k", ls="--", lw=1)
a1.set_xticks(range(len(games)), [g.capitalize().replace("Mspacman", "MsPacman").replace("Roadrunner", "RoadRunner") for g in games], fontsize=9)
a1.set_ylabel("drift / drift with random gaze")
a1.set_title("Which patch to look at (1 real patch per frame); below 1 = better than random", fontsize=10)
a1.grid(axis="y", alpha=.3)
a1.legend(fontsize=8, ncol=4, loc="upper left")
a1.set_ylim(0, 1.25)

gm = lambda p, k: np.exp(np.mean(np.log([d[f"{g}_{p}_k{k}"]["vs_open"] for g, d in s.items() if f"{g}_{p}_k{k}" in d])))
for p, lab, c in [("random", "Random", "0.2"), ("motion", "Motion", "C0"), ("pred_all", "Predicted error", "C4"),
                  ("oracle", "Oracle (not deployable)", "0.55")]:
    ks = [k for k in (1, 2, 4) if all(f"{g}_{p}_k{k}" in d for g, d in s.items())]
    a2.plot(ks, [gm(p, k) for k in ks], "o-", color=c, label=lab)
a2.plot([1], [gm("combo", 1)], "*", ms=12, color="C2", label="Motion x disagreement")
a2.set_xscale("log", base=2)
a2.set_xticks([1, 2, 4], ["1", "2", "4"])
a2.set_xlabel("real patches per frame (of 16)")
a2.set_ylabel("drift / open-loop drift")
a2.set_title("Observation budget (geometric mean, 8 games)", fontsize=10)
a2.grid(alpha=.3)
a2.legend(fontsize=7)
fig.tight_layout()
fig.savefig(a.out, dpi=150)
print("saved", a.out)
