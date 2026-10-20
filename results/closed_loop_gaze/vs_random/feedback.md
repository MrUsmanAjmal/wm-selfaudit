## Feeding the observed patch back into the model

16 clips from 10 videos. Baseline: 'Random gaze' without feedback (2 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Motion x disagreement gaze | 0.0397 | 0.0361 | 0.91 (0.85-0.96) | -9% | 62% |
| all imagined frames | Disagreement gaze | 0.0397 | 0.0366 | 0.92 (0.88-0.96) | -8% | 81% |
| all imagined frames | Motion gaze | 0.0397 | 0.0363 | 0.91 (0.86-0.97) | -9% | 75% |
| within trained length | Motion x disagreement gaze | 0.0281 | 0.0272 | 0.97 (0.92-1.00) | -3% | 56% |
| within trained length | Disagreement gaze | 0.0281 | 0.0271 | 0.96 (0.93-1.00) | -4% | 62% |
| within trained length | Motion gaze | 0.0281 | 0.0272 | 0.97 (0.92-1.00) | -3% | 69% |
| beyond trained length | Motion x disagreement gaze | 0.0490 | 0.0432 | 0.88 (0.81-0.95) | -12% | 75% |
| beyond trained length | Disagreement gaze | 0.0490 | 0.0442 | 0.90 (0.86-0.95) | -10% | 88% |
| beyond trained length | Motion gaze | 0.0490 | 0.0436 | 0.89 (0.82-0.97) | -11% | 69% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Motion x disagreement gaze | 32 | -4.5 (-19.1 to +7.8) | 37.2 (20.9-53.9) |
| Disagreement gaze | 32 | -4.7 (-18.9 to +12.4) | 35.9 (17.2-53.9) |
| Motion gaze | 32 | -3.3 (-15.9 to +6.3) | 43.0 (22.2-62.5) |
