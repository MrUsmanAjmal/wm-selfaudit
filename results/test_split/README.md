# 72 held-out Minecraft test videos (notebook 06)

Rollouts come from `notebooks/06_scaled_test_split.ipynb` (Kaggle, 2x T4, 10.15 h). The tables and figures here were re-made locally from those rollouts with the current `src/wm_audit.py`, so they also include the shrunk control variate. Every number the notebook printed is reproduced exactly; only the max-bias column differs at the 1e-14 level (floating point).

- 72 clips from 72 different videos of the TECO Minecraft test split, one clip per video, 3 rollouts each, 18 imagined frames, 50 DDIM steps. The 10 test videos that are also in the quick-start set were left out (`sampled_test_videos.json` lists the videos used).
- The 2x speed condition is labelled "40 test videos" in the tables because that was the plan, but only 7 of its 15 jobs finished, so it covers **16 clips from 16 videos**.
- Predictors here are fit leave-one-video-out on the other test videos. For predictors fit on separate videos and frozen, see `../test_split_frozen/`.

```
python src/wm_audit.py analyze --data <wm_audit_data from notebook 06> --out results/test_split
```

`perceptual/lpips_calibration.md` is the LPIPS version of the calibration test, from the notebook.
