# 72 held-out Minecraft test videos (notebook 06)

These files are copied straight from the outputs of `notebooks/06_scaled_test_split.ipynb` (Kaggle, 2x T4, 10.15 h).

- 72 clips from 72 different videos of the TECO Minecraft test split, one clip per video, 3 rollouts each, 18 imagined frames, 50 DDIM steps. The 10 test videos that are also in the quick-start set were left out.
- The 2x speed condition is labelled "40 test videos" in the tables because that was the plan, but only 7 of its 15 jobs finished, so it actually covers **16 clips from 16 videos**.
- This was analysed with the `wm_audit.py` version inside the notebook. That version doesn't have the shrunk control variate or the pooled online bias, which were added later.

`results.md` has every table, `fig1`-`fig6` are the same figures as in `results/main/`, and `perceptual/lpips_calibration.md` is the LPIPS version of the calibration test.
