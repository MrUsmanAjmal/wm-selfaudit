"""Run Diffusion Forcing's `python -m main ...` unchanged on a fixed list of validation clips, and save the raw float predictions and real videos that the repo passes to its video logger (utils.logging_utils.log_video)."""
import json
import os
import runpy
import sys

import numpy as np

sys.path.insert(0, os.getcwd())
OUT = os.environ["DF_DUMP_FILE"]
CLIPS = json.loads(os.environ["DF_CLIPS"])
os.makedirs(os.path.dirname(OUT), exist_ok=True)

import datasets.video.base_video_dataset as bv
import utils.logging_utils as lu

if not hasattr(lu, "log_video"):
    raise SystemExit("utils.logging_utils.log_video not found: the repository layout changed.")
_original_log = lu.log_video
_original_init = bv.BaseVideoDataset.__init__


def init_with_fixed_clips(self, cfg, split="training"):
    """Put the requested (video, start frame) windows first in the validation order."""
    _original_init(self, cfg, split)
    if split == "training":
        return
    first = np.concatenate([[0], self.cum_clips_per_video[:-1]])
    chosen = []
    for v, s in CLIPS:
        if v >= len(first) or s >= self.clips_per_video[v]:
            raise SystemExit(f"clip (video {v}, start {s}) is not in the {split} set "
                             f"({len(first)} videos, window of {self.n_frames} frames)")
        chosen.append(int(first[v] + s))
    taken = set(chosen)
    self.idx_remap = chosen + [i for i in self.idx_remap if i not in taken]


def _to_numpy(x):
    if hasattr(x, "detach"):
        return x.detach().float().cpu().numpy()
    return np.asarray(x, dtype=np.float32)


def log_video_and_dump(*args, **kwargs):
    named = [kwargs.get("observation_hat"), kwargs.get("observation_gt")]
    arrays = [a for a in list(args) + named if a is not None and len(getattr(a, "shape", ())) == 5]
    if len(arrays) >= 2 and not os.path.exists(OUT):
        pred, gt = _to_numpy(arrays[0]), _to_numpy(arrays[1])
        tmp = OUT[:-4] + ".part.npz"
        np.savez_compressed(tmp, pred=pred.astype(np.float16), gt=gt.astype(np.float16),
                            clips=np.array(CLIPS[:pred.shape[1]], dtype=np.int64))
        os.replace(tmp, OUT)
        print(f"[dump] saved {OUT} with shape {pred.shape}", flush=True)
    return _original_log(*args, **kwargs)


bv.BaseVideoDataset.__init__ = init_with_fixed_clips
lu.log_video = log_video_and_dump
sys.argv = ["main.py"] + sys.argv[1:]
runpy.run_module("main", run_name="__main__", alter_sys=True)
