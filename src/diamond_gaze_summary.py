"""Tables and a figure for the gaze study (output of src/diamond_gaze.py).

For each game and policy: drift with feedback / open-loop drift, drift / drift of random gaze at the same budget (paired by
episode, both under the same random numbers), share of episodes where the policy beats random, and the pooled bias of
the online drift estimate from the patches that were shown. 95% CIs resample episodes.

    python src/diamond_gaze_summary.py --data <diamond_gaze.py output> --out results/diamond_gaze
"""
import argparse
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wm_audit import ci, cluster_sets, context_frames, load_condition, md_table, patchify

POLICY_LABELS = {"random": "Random", "motion": "Motion", "disagree": "Disagreement", "pred_vis": "Predicted error (visual)",
                 "pred_all": "Predicted error (visual + disagreement)", "disagree_e30": "Disagreement, 30% floor",
                 "combo": "Motion x disagreement", "combo_e30": "Motion x disagreement, 30% floor",
                 "oracle": "Oracle (not deployable)"}


def drift_per_clip(clips, n_ctx):
    """Mean over rollouts and imagined frames of the full-frame MSE of the prediction made before feedback."""
    return np.array([np.mean([((p[n_ctx:] - c["gt"][n_ctx:]) ** 2).mean() for p in c["preds"]]) for c in clips])


def online_bias(clips, n_ctx, P, sets_fn):
    ests, truths, vids = [], [], []
    for c in clips:
        if "gaze" not in c["extra"]:
            return None
        gt_p = patchify(c["gt"], P)
        J = gt_p.shape[1]
        for r, p in enumerate(c["preds"]):
            e = ((patchify(p, P) - gt_p) ** 2).mean(-1)[n_ctx:]
            j = c["extra"]["gaze"][r].astype(int)
            q = c["extra"]["q"][r].astype(np.float64)
            ests.append(float(np.mean(e[np.arange(len(j)), j] / (J * q))))
            truths.append(float(e.mean()))
            vids.append(c["video"])
    ests, truths = np.array(ests), np.array(truths)
    stat = lambda s: 100 * (ests[s].sum() / truths[s].sum() - 1)
    return stat(np.arange(len(ests))), ci(stat, sets_fn(vids))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="results/diamond_gaze")
    ap.add_argument("--B", type=int, default=5000)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    plan = json.load(open(os.path.join(a.data, "plan.json")))["conditions"]
    games = sorted({n.rsplit("_open", 1)[0] for n in plan if n.endswith("_open")})
    summary, rows, rows_rand = {}, [], []
    for g in games:
        conds = [n for n in plan if n.startswith(g + "_") and os.path.isdir(os.path.join(a.data, n))]
        if f"{g}_open" not in conds:
            continue
        loaded = {n: load_condition(os.path.join(a.data, n))[0] for n in conds}
        loaded = {n: v for n, v in loaded.items() if v}
        base = loaded[f"{g}_open"]
        n_ctx = context_frames(base)
        P = plan[f"{g}_open"]["patch"]
        vids = np.array([c["video"] for c in base])
        sets = cluster_sets(vids, B=a.B)
        full = np.arange(len(vids))
        d_open = drift_per_clip(base, n_ctx)
        d = {n: drift_per_clip(v, n_ctx) for n, v in loaded.items()}
        summary[g] = {}
        label = plan[f"{g}_open"]["label"].split(":")[0]
        for n in sorted(loaded, key=lambda n: (plan[n].get("patches_per_frame", 0), list(POLICY_LABELS).index(plan[n]["gaze"]) if "gaze" in plan[n] else -1)):
            if "gaze" not in plan[n]:
                continue
            pol, k = plan[n]["gaze"], plan[n]["patches_per_frame"]
            x = d[n]
            r_open = lambda s, x=x: x[s].sum() / d_open[s].sum()
            res = dict(policy=pol, k=k, vs_open=r_open(full), vs_open_ci=ci(r_open, sets))
            rand = d.get(f"{g}_random_k{k}")
            if rand is not None and pol != "random":
                r_rand = lambda s, x=x: x[s].sum() / rand[s].sum()
                res.update(vs_random=r_rand(full), vs_random_ci=ci(r_rand, sets), beats_random=float((x < rand).mean()))
            ob = online_bias(loaded[n], n_ctx, P, lambda v: cluster_sets(v, B=a.B)) if pol != "oracle" and k == 1 else None
            if ob:
                res.update(online_bias=ob[0], online_bias_ci=ob[1])
            summary[g][n] = res
            rows.append([label, POLICY_LABELS[pol], str(k), f"{res['vs_open']:.2f} ({res['vs_open_ci'][0]:.2f}-{res['vs_open_ci'][1]:.2f})",
                         f"{res['vs_random']:.2f} ({res['vs_random_ci'][0]:.2f}-{res['vs_random_ci'][1]:.2f})" if "vs_random" in res else "",
                         f"{100 * res['beats_random']:.0f}%" if "beats_random" in res else "",
                         f"{res['online_bias']:+.1f} ({res['online_bias_ci'][0]:+.1f} to {res['online_bias_ci'][1]:+.1f})" if "online_bias" in res else ""])
    md = ("## Which patch to look at: gaze policies on DIAMOND\n\nNew episodes, 2 rollouts per window, every policy under the "
          "same random numbers. Drift ratios are total drift with feedback over total drift of the comparison, 95% CI over "
          "episodes (paired). Online bias: pooled bias of the drift estimate from the patches that were shown.\n\n"
          + md_table(["Game", "Gaze", "Patches/frame", "vs open loop", "vs random gaze", "Episodes better than random",
                      "Online bias (%)"], rows) + "\n")
    # how often each policy is clearly better / worse than random, over games
    tally = []
    for pol in POLICY_LABELS:
        for k in sorted({r["k"] for gs in summary.values() for r in gs.values()}):
            vals = [r for gs in summary.values() for r in gs.values() if r["policy"] == pol and r["k"] == k and "vs_random" in r]
            if vals:
                tally.append([POLICY_LABELS[pol], str(k), str(len(vals)), str(sum(r["vs_random_ci"][1] < 1 for r in vals)),
                              str(sum(r["vs_random_ci"][0] > 1 for r in vals)),
                              f"{np.exp(np.mean([np.log(r['vs_random']) for r in vals])):.2f}"])
    md += ("\n**Against random gaze, over games** (clearly better: CI below 1; clearly worse: CI above 1)\n\n"
           + md_table(["Gaze", "Patches/frame", "Games", "Clearly better", "Clearly worse", "Geometric mean ratio"], tally) + "\n")
    open(os.path.join(a.out, "gaze.md"), "w").write(md)
    json.dump(summary, open(os.path.join(a.out, "gaze.json"), "w"), indent=1, default=float)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    pols = [p for p in POLICY_LABELS if p != "random"]
    fig, ax = plt.subplots(figsize=(1.2 * len(summary) + 3, 3.8))
    w = 0.8 / len(pols)
    for i, pol in enumerate(pols):
        for gi, g in enumerate(summary):
            r = summary[g].get(f"{g}_{pol}_k1")
            if not r or "vs_random" not in r:
                continue
            x = gi + (i - (len(pols) - 1) / 2) * w
            ax.bar(x, r["vs_random"], w, color=f"C{i}", label=POLICY_LABELS[pol] if gi == 0 else None)
            ax.errorbar(x, r["vs_random"], yerr=[[r["vs_random"] - r["vs_random_ci"][0]], [r["vs_random_ci"][1] - r["vs_random"]]],
                        color="k", capsize=2, lw=0.8)
    ax.axhline(1, color="k", ls="--", lw=1)
    ax.set_xticks(range(len(summary)), [g.capitalize() for g in summary], fontsize=8)
    ax.set_ylabel("drift / drift with random gaze")
    ax.set_title("One real patch per frame: below 1 = better than random gaze", fontsize=10)
    ax.grid(axis="y", alpha=.3)
    ax.legend(fontsize=7, ncol=3)
    fig.tight_layout()
    fig.savefig(os.path.join(a.out, "fig_gaze_vs_random.png"), dpi=150)
    plt.close(fig)
    print(md)


if __name__ == "__main__":
    main()
