"""Run Diffusion Forcing's `python -m main ...` on a fixed list of validation clips with closed-loop gaze: after each
imagined frame, one real patch of that frame is pasted into the rollout, so every later frame is generated with it
in view. The model's prediction of each frame (made before its patch is seen), the chosen patches and their
sampling probabilities are saved.

The sampling loop is the repository's own DiffusionForcingBase.validation_step, unchanged except for the paste."""
import json
import os
import runpy
import sys

import numpy as np

sys.path.insert(0, os.getcwd())
OUT = os.environ["DF_DUMP_FILE"]
CLIPS = json.loads(os.environ["DF_CLIPS"])
GAZE = os.environ["DF_GAZE"]
PATCH = int(os.environ.get("DF_PATCH", "32"))
EPS = float(os.environ.get("DF_GAZE_EPS", "0.1"))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
if GAZE not in ("random", "guided", "oracle"):
    raise SystemExit(f"unknown gaze policy '{GAZE}'")

import torch
import torch.nn.functional as F
from tqdm import tqdm

import algorithms.diffusion_forcing.df_base as dfb
import datasets.video.base_video_dataset as bv
import utils.logging_utils as lu

_original_log = lu.log_video
_original_init = bv.BaseVideoDataset.__init__
_gen = torch.Generator().manual_seed(int(os.environ.get("DF_GAZE_SEED", "0")))
_gaze = {"gaze": [], "q": []}


def init_with_fixed_clips(self, cfg, split="training"):
    """Put the requested (video, start frame) windows first in the validation order."""
    _original_init(self, cfg, split)
    if split == "training":
        return
    first = np.concatenate([[0], self.cum_clips_per_video[:-1]])
    chosen = []
    for v, s in CLIPS:
        if v >= len(first) or s >= self.clips_per_video[v]:
            raise SystemExit(f"clip (video {v}, start {s}) is not in the {split} set")
        chosen.append(int(first[v] + s))
    taken = set(chosen)
    self.idx_remap = chosen + [i for i in self.idx_remap if i not in taken]


def patch_means(x):
    """(B, C, H, W) -> (B, J): mean over each P x P patch and the channels."""
    B, C, H, W = x.shape
    return x.reshape(B, C, H // PATCH, PATCH, W // PATCH, PATCH).mean(dim=(1, 3, 5)).reshape(B, -1)


def choose(prev, cur, real):
    """Pick one patch per clip, using only the imagined frames (except the oracle). Returns indices and probabilities."""
    B = cur.shape[0]
    J = (cur.shape[-2] // PATCH) * (cur.shape[-1] // PATCH)
    if GAZE == "oracle":
        return patch_means((cur - real).float() ** 2).argmax(1).cpu(), torch.ones(B)
    if GAZE == "random":
        q = torch.full((B, J), 1.0 / J)
    else:
        s = patch_means((cur - prev).float() ** 2).sqrt().cpu() + 1e-12
        q = (1 - EPS) * s / s.sum(1, keepdim=True) + EPS / J
    j = torch.multinomial(q, 1, generator=_gen).squeeze(1)
    return j, q.gather(1, j[:, None]).squeeze(1)


@torch.no_grad()
def validation_step_with_gaze(self, batch, batch_idx, namespace="validation"):
    if self.frame_stack != 1:
        raise SystemExit("closed-loop gaze assumes frame_stack == 1")
    xs, conditions, masks = self._preprocess_batch(batch)
    n_frames, batch_size, *_ = xs.shape
    curr_frame = 0

    n_context_frames = self.context_frames // self.frame_stack
    xs_pred = xs[:n_context_frames].clone()
    curr_frame += n_context_frames
    imagined = []

    pbar = tqdm(total=n_frames, initial=curr_frame, desc="Sampling")
    while curr_frame < n_frames:
        if self.chunk_size > 0:
            horizon = min(n_frames - curr_frame, self.chunk_size)
        else:
            horizon = n_frames - curr_frame
        assert horizon <= self.n_tokens, "horizon exceeds the number of tokens."
        scheduling_matrix = self._generate_scheduling_matrix(horizon)

        chunk = torch.randn((horizon, batch_size, *self.x_stacked_shape), device=self.device)
        chunk = torch.clamp(chunk, -self.clip_noise, self.clip_noise)
        xs_pred = torch.cat([xs_pred, chunk], 0)

        start_frame = max(0, curr_frame + horizon - self.n_tokens)
        pbar.set_postfix({"start": start_frame, "end": curr_frame + horizon})

        for m in range(scheduling_matrix.shape[0] - 1):
            from_noise_levels = np.concatenate((np.zeros((curr_frame,), dtype=np.int64), scheduling_matrix[m]))[
                :, None
            ].repeat(batch_size, axis=1)
            to_noise_levels = np.concatenate(
                (np.zeros((curr_frame,), dtype=np.int64), scheduling_matrix[m + 1])
            )[:, None].repeat(batch_size, axis=1)
            from_noise_levels = torch.from_numpy(from_noise_levels).to(self.device)
            to_noise_levels = torch.from_numpy(to_noise_levels).to(self.device)
            xs_pred[start_frame:] = self.diffusion_model.sample_step(
                xs_pred[start_frame:],
                conditions[start_frame : curr_frame + horizon],
                from_noise_levels[start_frame:],
                to_noise_levels[start_frame:],
            )

        # closed loop: keep the model's prediction, then show it one real patch of each new frame
        w = xs.shape[-1] // PATCH
        for f in range(curr_frame, curr_frame + horizon):
            imagined.append(xs_pred[f].clone())
            j, q = choose(xs_pred[f - 1], xs_pred[f], xs[f])
            for b in range(batch_size):
                r, c = divmod(int(j[b]), w)
                rows, cols = slice(r * PATCH, (r + 1) * PATCH), slice(c * PATCH, (c + 1) * PATCH)
                xs_pred[f, b, :, rows, cols] = xs[f, b, :, rows, cols]
            _gaze["gaze"].append(j.numpy())
            _gaze["q"].append(q.numpy())

        curr_frame += horizon
        pbar.update(horizon)

    out = torch.cat([xs_pred[:n_context_frames], torch.stack(imagined)], 0)
    loss = F.mse_loss(out, xs, reduction="none")
    loss = self.reweight_loss(loss, masks)

    xs = self._unstack_and_unnormalize(xs)
    out = self._unstack_and_unnormalize(out)
    self.validation_step_outputs.append((out.detach().cpu(), xs.detach().cpu()))
    return loss


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
                            clips=np.array(CLIPS[:pred.shape[1]], dtype=np.int64),
                            gaze=np.stack(_gaze["gaze"]).astype(np.int16), q=np.stack(_gaze["q"]).astype(np.float32))
        os.replace(tmp, OUT)
        print(f"[dump] saved {OUT} with shape {pred.shape}, gaze '{GAZE}'", flush=True)
    return _original_log(*args, **kwargs)


bv.BaseVideoDataset.__init__ = init_with_fixed_clips
dfb.DiffusionForcingBase.validation_step = validation_step_with_gaze
lu.log_video = log_video_and_dump
# importing df_base already imported df_video, which holds its own reference to the original logger
for mod in list(sys.modules.values()):
    if getattr(mod, "log_video", None) is _original_log:
        mod.log_video = log_video_and_dump
sys.argv = ["main.py"] + sys.argv[1:]
runpy.run_module("main", run_name="__main__", alter_sys=True)
if not os.path.exists(OUT):
    raise SystemExit(f"validation finished but nothing was saved to {OUT}")
