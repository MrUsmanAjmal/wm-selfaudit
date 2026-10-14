## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'Pong' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Pong: Guided gaze | 0.0000 | 0.0000 | 0.75 (0.63-0.96) | -25% | 100% |
| all imagined frames | Pong: Random gaze | 0.0000 | 0.0000 | 0.90 (0.85-0.97) | -10% | 100% |
| all imagined frames | Pong: Oracle gaze (not deployable) | 0.0000 | 0.0000 | 0.60 (0.39-0.94) | -40% | 100% |
| within trained length | Pong: Guided gaze | 0.0000 | 0.0000 | 0.82 (0.72-0.99) | -18% | 97% |
| within trained length | Pong: Random gaze | 0.0000 | 0.0000 | 0.93 (0.88-0.99) | -7% | 100% |
| within trained length | Pong: Oracle gaze (not deployable) | 0.0000 | 0.0000 | 0.70 (0.52-0.99) | -30% | 100% |
| beyond trained length | Pong: Guided gaze | 0.0000 | 0.0000 | 0.70 (0.57-0.94) | -30% | 100% |
| beyond trained length | Pong: Random gaze | 0.0000 | 0.0000 | 0.88 (0.83-0.96) | -12% | 100% |
| beyond trained length | Pong: Oracle gaze (not deployable) | 0.0000 | 0.0000 | 0.52 (0.29-0.93) | -48% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Pong: Guided gaze | 64 | -4.5 (-22.8 to +18.0) | 45.7 (38.6-52.0) |
| Pong: Random gaze | 64 | -7.5 (-22.4 to +15.5) | 28.9 (16.4-39.4) |
