"""One table and one figure for the DIAMOND (Atari) experiment, from the outputs of wm_audit.py analyze / feedback.

    python src/diamond_summary.py --results results/diamond
"""
import argparse
import json
import os

import numpy as np

UCV = "Uniform + CV[visual+disagreement]"
SHR = "Uniform + shrunk CV[visual+disagreement]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    a = ap.parse_args()
    s = json.load(open(os.path.join(a.results, "summary.json")))["conditions"]
    games = [n for n in s if not n.endswith("_stoch")]
    fb = {}
    for g in games:
        f = os.path.join(a.results, "feedback", g, "feedback.json")
        if os.path.exists(f):
            fb[g] = json.load(open(f))["bins"]
    fmt = lambda x, lo, hi, d=2: f"{x:.{d}f} [{lo:.{d}f}, {hi:.{d}f}]"
    rows, out = [], {}
    for g in games:
        c, st = s[g], s.get(f"{g}_stoch")
        cal, cal_s = c["calibration"]["all"], (st["calibration"]["all"] if st else None)
        bias = next(r for r in c["self_assessment"]["all"] if r["method"] == "Rollout disagreement")
        audit = next(r for r in c["audits"]["all"] if r["method"] == UCV)
        shr = next(r for r in c["audits"]["all"] if r["method"] == SHR)
        row = dict(game=c["label"], episodes=c["videos"], ratio=cal["error_over_disagreement"],
                   ratio_ci=[cal["ratio_lo"], cal["ratio_hi"]], bias=bias["bias_pct"], bias_ci=[bias["bias_lo"], bias["bias_hi"]],
                   audit_var=audit["var_ratio"], audit_ci=[audit["ratio_lo"], audit["ratio_hi"]],
                   shrunk_var=shr["var_ratio"], shrunk_ci=[shr["ratio_lo"], shr["ratio_hi"]])
        if cal_s:
            row.update(ratio_stoch=cal_s["error_over_disagreement"], ratio_stoch_ci=[cal_s["ratio_lo"], cal_s["ratio_hi"]])
        for pol in ("guided", "random", "oracle"):
            r = fb.get(g, {}).get("all", {}).get(f"{g}_fb_{pol}")
            if r:
                row[f"fb_{pol}"], row[f"fb_{pol}_ci"] = r["ratio"], r["ratio_ci"]
        out[g] = row
        rows.append("| " + " | ".join([
            row["game"], str(row["episodes"]), fmt(row["ratio"], *row["ratio_ci"], 0 if row["ratio"] > 20 else 1),
            fmt(row["ratio_stoch"], *row["ratio_stoch_ci"], 1) if cal_s else "",
            f"{row['bias']:+.1f}", fmt(row["audit_var"], *row["audit_ci"]), fmt(row["shrunk_var"], *row["shrunk_ci"]),
            *[fmt(row[f"fb_{p}"], *row[f"fb_{p}_ci"]) if f"fb_{p}" in row else "" for p in ("guided", "random", "oracle")]]) + " |")
    md = ("## DIAMOND (Atari), one window per real episode\n\n"
          "Error / disagreement: mean real error over mean disagreement between 3 rollouts (1 = calibrated), with the "
          "default deterministic sampler and with a stochastic sampler. Bias: disagreement used as the drift estimate (%). "
          "CV: variance of uniform sampling with the visual+disagreement control variate, relative to plain uniform "
          "sampling (1 real 16x16 patch per frame); shrunk CV: the same with the control-variate weight chosen on the "
          "other episodes. Feedback: drift with one real patch per frame fed back / without. "
          "95% CIs resample episodes.\n\n"
          "| Game | Episodes | Error / disagreement | Error / disagreement, stochastic sampler | Bias of disagreement (%) | "
          "CV variance vs uniform | Shrunk CV variance vs uniform | Feedback: guided | Feedback: random | Feedback: oracle |\n"
          "|---|---|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
    vals = lambda k: np.array([out[g][k] for g in games if k in out[g]])
    md += (f"\nAcross {len(games)} games: error / disagreement {vals('ratio').min():.0f}–{vals('ratio').max():.0f} with the default "
           f"sampler and {vals('ratio_stoch').min():.1f}–{vals('ratio_stoch').max():.1f} with the stochastic sampler; "
           f"control-variate variance ratio {vals('audit_var').min():.2f}–{vals('audit_var').max():.2f} "
           f"(shrunk: {vals('shrunk_var').min():.2f}–{vals('shrunk_var').max():.2f})")
    if len(vals("fb_guided")):
        md += (f"; feedback ratio {vals('fb_guided').min():.2f}–{vals('fb_guided').max():.2f} (guided), "
               f"{vals('fb_random').min():.2f}–{vals('fb_random').max():.2f} (random), "
               f"{vals('fb_oracle').min():.2f}–{vals('fb_oracle').max():.2f} (oracle)")
    md += ".\n"
    open(os.path.join(a.results, "diamond_summary.md"), "w").write(md)
    json.dump(out, open(os.path.join(a.results, "diamond_summary.json"), "w"), indent=2)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.2))
    x = np.arange(len(games))
    for i, (k, lab) in enumerate((("ratio", "default sampler"), ("ratio_stoch", "stochastic sampler"))):
        v = [out[g].get(k, np.nan) for g in games]
        lo = [out[g].get(f"{k}_ci", [np.nan, np.nan])[0] for g in games]
        hi = [out[g].get(f"{k}_ci", [np.nan, np.nan])[1] for g in games]
        a1.errorbar(x + (i - 0.5) * 0.25, v, yerr=[np.subtract(v, lo), np.subtract(hi, v)], fmt="o", capsize=3,
                    color=f"C{i}", label=lab)
    a1.axhline(1, color="k", ls="--", lw=1)
    a1.set_yscale("log")
    a1.set_xticks(x, [out[g]["game"] for g in games], rotation=30, ha="right", fontsize=8)
    a1.set_ylabel("mean real error / mean disagreement")
    a1.set_title("DIAMOND: 1 = calibrated (log scale)", fontsize=10)
    a1.legend(fontsize=8)
    a1.grid(alpha=.3, which="both")
    w = 0.26
    for i, pol in enumerate(("guided", "random", "oracle")):
        v = [out[g].get(f"fb_{pol}", np.nan) for g in games]
        ci = [out[g].get(f"fb_{pol}_ci", [np.nan, np.nan]) for g in games]
        a2.bar(x + (i - 1) * w, v, w, color=f"C{i + 1}", label=f"{pol} gaze")
        a2.errorbar(x + (i - 1) * w, v, yerr=[np.subtract(v, [c[0] for c in ci]), np.subtract([c[1] for c in ci], v)],
                    fmt="none", color="k", capsize=2)
    a2.axhline(1, color="k", ls="--", lw=1)
    a2.set_xticks(x, [out[g]["game"] for g in games], rotation=30, ha="right", fontsize=8)
    a2.set_ylabel("drift with feedback / without")
    a2.set_title("One real patch per frame fed back", fontsize=10)
    a2.set_ylim(0, 1.25)
    a2.legend(fontsize=8, ncol=3, loc="upper center")
    a2.grid(axis="y", alpha=.3)
    fig.tight_layout()
    fig.savefig(os.path.join(a.results, "fig10_diamond.png"), dpi=150)
    plt.close(fig)
    print(md)


if __name__ == "__main__":
    main()
