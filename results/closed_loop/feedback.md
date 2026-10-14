## Feeding the observed patch back into the model

16 clips from 10 videos. Baseline: 'Minecraft, 50 steps' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Guided gaze | 0.0486 | 0.0386 | 0.80 (0.69-0.93) | -20% | 75% |
| all imagined frames | Random gaze | 0.0486 | 0.0402 | 0.83 (0.76-0.94) | -17% | 62% |
| all imagined frames | Oracle gaze (not deployable) | 0.0486 | 0.0302 | 0.62 (0.55-0.73) | -38% | 100% |
| within trained length | Guided gaze | 0.0300 | 0.0288 | 0.96 (0.90-1.06) | -4% | 56% |
| within trained length | Random gaze | 0.0300 | 0.0304 | 1.01 (0.94-1.11) | +1% | 56% |
| within trained length | Oracle gaze (not deployable) | 0.0300 | 0.0214 | 0.71 (0.61-0.83) | -29% | 94% |
| beyond trained length | Guided gaze | 0.0634 | 0.0464 | 0.73 (0.60-0.89) | -27% | 88% |
| beyond trained length | Random gaze | 0.0634 | 0.0480 | 0.76 (0.69-0.90) | -24% | 69% |
| beyond trained length | Oracle gaze (not deployable) | 0.0634 | 0.0373 | 0.59 (0.51-0.69) | -41% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Guided gaze | 32 | -16.6 (-23.1 to -5.0) | 27.9 (22.1-33.0) |
| Random gaze | 32 | +1.0 (-10.6 to +15.6) | 33.2 (28.6-37.6) |
