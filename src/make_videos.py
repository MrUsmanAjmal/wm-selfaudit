"""Side-by-side videos of the real clip, the open-loop rollout and the closed-loop rollouts (one real patch per frame
fed back), written as animated GIFs.

    python src/make_videos.py --data <wm_audit_data> --out videos
"""
import argparse
import glob
import json
import os

import numpy as np

COLUMNS = [("minecraft", "No feedback"), ("feedback_guided", "Guided gaze"),
           ("feedback_random", "Random gaze"), ("feedback_oracle", "Oracle gaze")]


def load(cdir, run=0):
    """{(video, start): (pred, gt, gaze or None)} for one rollout of one condition, frames as (T, H, W, 3) in [0, 1]."""
    out = {}
    for f in sorted(glob.glob(os.path.join(cdir, f"run_{run}", "batch_*.npz"))):
        z = np.load(f)
        pred = np.clip(z["pred"].astype(np.float32).transpose(1, 0, 3, 4, 2), 0, 1)
        gt = np.clip(z["gt"].astype(np.float32).transpose(1, 0, 3, 4, 2), 0, 1)
        gaze = z["gaze"].T if "gaze" in z.files else None
        for i, (v, s) in enumerate(z["clips"]):
            out[(int(v), int(s))] = (pred[i], gt[i], None if gaze is None else gaze[i])
    return out


def make_gif(path, panels, n_ctx, patch, fps=4, scale=2):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation, PillowWriter
    from matplotlib.patches import Rectangle

    T = panels[0][1].shape[0]
    fig, axs = plt.subplots(1, len(panels), figsize=(2.2 * scale * len(panels) / 2, 3.0 * scale / 2))
    axs = np.atleast_1d(axs)
    ims, boxes, titles = [], [], []
    for a, (title, frames, gaze) in zip(axs, panels):
        ims.append(a.imshow(frames[0], interpolation="nearest"))
        titles.append(a.set_title(title, fontsize=9))
        box = Rectangle((0, 0), patch, patch, fill=False, edgecolor="red", lw=1.5, visible=False)
        a.add_patch(box)
        boxes.append(box)
        a.axis("off")
    caption = fig.suptitle("", fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.9))

    def draw(t):
        for im, box, (title, frames, gaze) in zip(ims, boxes, panels):
            im.set_data(frames[t])
            if gaze is not None and t >= n_ctx:
                r, c = divmod(int(gaze[t - n_ctx]), frames.shape[2] // patch)
                box.set_xy((c * patch - 0.5, r * patch - 0.5))
                box.set_visible(True)
            else:
                box.set_visible(False)
        caption.set_text("real context frame" if t < n_ctx else
                         f"imagined frame {t - n_ctx + 1}   (red box: real patch shown to the model)")
        return ims + boxes + [caption]

    FuncAnimation(fig, draw, frames=T, blit=False).save(path, writer=PillowWriter(fps=fps), dpi=100)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="videos")
    ap.add_argument("--run", type=int, default=0)
    ap.add_argument("--clips", type=int, default=0, help="number of clips to render (0 = all shared clips)")
    ap.add_argument("--base", default="minecraft", help="condition without feedback (DIAMOND: the game, e.g. breakout)")
    ap.add_argument("--context", type=int, default=2)
    ap.add_argument("--scale", type=int, default=2)
    ap.add_argument("--video", type=int, default=None, help="render only this video index")
    ap.add_argument("--still", type=int, default=None, help="also save this frame index as a PNG figure")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    plan = json.load(open(os.path.join(a.data, "plan.json")))
    patch = plan["conditions"][a.base]["patch"]
    columns = COLUMNS if a.base == "minecraft" else [(a.base, "No feedback")] + [
        (f"{a.base}_fb_{g}", f"{g.capitalize()} gaze") for g in ("guided", "random", "oracle")]
    cols = [(name, label, load(os.path.join(a.data, name), a.run)) for name, label in columns
            if os.path.isdir(os.path.join(a.data, name))]
    cols = [c for c in cols if c[2]]
    if not cols:
        raise SystemExit(f"no rollouts found in {a.data}")
    keys = sorted(set.intersection(*[set(c[2]) for c in cols]))
    if a.video is not None:
        keys = [k for k in keys if k[0] == a.video]
    if a.clips:
        keys = keys[:a.clips]
    n_ctx = a.context
    for k in keys:
        gt = cols[0][2][k][1]
        panels = [("Real video", gt, None)] + [(label, d[k][0], d[k][2]) for _, label, d in cols]
        err = "  ".join(f"{label}: {((d[k][0][n_ctx:] - gt[n_ctx:]) ** 2).mean():.3g}" for _, label, d in cols)
        path = os.path.join(a.out, f"{'' if a.base == 'minecraft' else a.base + '_'}video{k[0]}_start{k[1]:03d}.gif")
        make_gif(path, panels, n_ctx, patch, scale=a.scale)
        print(f"{path}   drift (MSE) {err}")
        if a.still is not None:
            make_still(path[:-4] + f"_frame{a.still - n_ctx + 1}.png", panels, n_ctx, patch, a.still)


def make_still(path, panels, n_ctx, patch, t):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    fig, axs = plt.subplots(1, len(panels), figsize=(2.3 * len(panels), 2.6))
    for a, (title, frames, gaze) in zip(axs, panels):
        a.imshow(frames[t], interpolation="nearest")
        if gaze is not None and t > n_ctx:
            r, c = divmod(int(gaze[t - n_ctx - 1]), frames.shape[2] // patch)
            a.add_patch(Rectangle((c * patch - 0.5, r * patch - 0.5), patch, patch, fill=False, edgecolor="red", lw=1.5))
        a.set_title(title, fontsize=9)
        a.axis("off")
    fig.suptitle(f"imagined frame {t - n_ctx + 1} (red box: real patch shown after the previous frame)", fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
