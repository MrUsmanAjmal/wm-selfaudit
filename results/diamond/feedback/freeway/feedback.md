## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'Freeway' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Freeway: Guided gaze | 0.0000 | 0.0000 | 0.69 (0.59-0.81) | -31% | 100% |
| all imagined frames | Freeway: Random gaze | 0.0000 | 0.0000 | 0.81 (0.77-0.87) | -19% | 100% |
| all imagined frames | Freeway: Oracle gaze (not deployable) | 0.0000 | 0.0000 | 0.42 (0.33-0.54) | -58% | 100% |
| within trained length | Freeway: Guided gaze | 0.0000 | 0.0000 | 0.79 (0.68-0.92) | -21% | 100% |
| within trained length | Freeway: Random gaze | 0.0000 | 0.0000 | 0.91 (0.86-0.95) | -9% | 100% |
| within trained length | Freeway: Oracle gaze (not deployable) | 0.0000 | 0.0000 | 0.54 (0.42-0.72) | -46% | 100% |
| beyond trained length | Freeway: Guided gaze | 0.0001 | 0.0000 | 0.65 (0.53-0.77) | -35% | 100% |
| beyond trained length | Freeway: Random gaze | 0.0001 | 0.0000 | 0.77 (0.71-0.83) | -23% | 100% |
| beyond trained length | Freeway: Oracle gaze (not deployable) | 0.0001 | 0.0000 | 0.36 (0.28-0.48) | -64% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Freeway: Guided gaze | 64 | -3.7 (-17.9 to +13.4) | 36.8 (30.4-43.4) |
| Freeway: Random gaze | 64 | -0.2 (-22.2 to +26.5) | 40.6 (25.6-54.3) |
