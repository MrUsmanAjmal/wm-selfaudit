## Feeding the observed patch back into the model

16 clips from 10 videos. Baseline: 'Minecraft, 50 steps' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Motion x disagreement gaze | 0.0486 | 0.0361 | 0.74 (0.68-0.83) | -26% | 88% |
| all imagined frames | Random gaze | 0.0486 | 0.0397 | 0.82 (0.72-0.93) | -18% | 75% |
| all imagined frames | Disagreement gaze | 0.0486 | 0.0366 | 0.75 (0.67-0.86) | -25% | 94% |
| all imagined frames | Motion gaze | 0.0486 | 0.0363 | 0.75 (0.68-0.85) | -25% | 88% |
| within trained length | Motion x disagreement gaze | 0.0300 | 0.0272 | 0.91 (0.82-0.99) | -9% | 75% |
| within trained length | Random gaze | 0.0300 | 0.0281 | 0.94 (0.86-1.02) | -6% | 69% |
| within trained length | Disagreement gaze | 0.0300 | 0.0271 | 0.90 (0.82-1.00) | -10% | 75% |
| within trained length | Motion gaze | 0.0300 | 0.0272 | 0.90 (0.83-0.98) | -10% | 75% |
| beyond trained length | Motion x disagreement gaze | 0.0634 | 0.0432 | 0.68 (0.61-0.80) | -32% | 100% |
| beyond trained length | Random gaze | 0.0634 | 0.0490 | 0.77 (0.65-0.94) | -23% | 75% |
| beyond trained length | Disagreement gaze | 0.0634 | 0.0442 | 0.70 (0.60-0.83) | -30% | 94% |
| beyond trained length | Motion gaze | 0.0634 | 0.0436 | 0.69 (0.61-0.82) | -31% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Motion x disagreement gaze | 32 | -4.5 (-19.1 to +7.8) | 37.2 (20.9-53.9) |
| Random gaze | 32 | +3.2 (-8.3 to +12.4) | 36.4 (27.9-44.4) |
| Disagreement gaze | 32 | -4.7 (-18.9 to +12.4) | 35.9 (17.2-53.9) |
| Motion gaze | 32 | -3.3 (-15.9 to +6.3) | 43.0 (22.2-62.5) |
