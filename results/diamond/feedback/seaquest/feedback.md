## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'Seaquest' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Seaquest: Guided gaze | 0.0002 | 0.0001 | 0.69 (0.59-0.78) | -31% | 94% |
| all imagined frames | Seaquest: Random gaze | 0.0002 | 0.0001 | 0.76 (0.69-0.84) | -24% | 94% |
| all imagined frames | Seaquest: Oracle gaze (not deployable) | 0.0002 | 0.0000 | 0.26 (0.21-0.33) | -74% | 100% |
| within trained length | Seaquest: Guided gaze | 0.0001 | 0.0001 | 0.79 (0.72-0.85) | -21% | 100% |
| within trained length | Seaquest: Random gaze | 0.0001 | 0.0001 | 0.88 (0.82-0.94) | -12% | 94% |
| within trained length | Seaquest: Oracle gaze (not deployable) | 0.0001 | 0.0000 | 0.38 (0.30-0.47) | -62% | 100% |
| beyond trained length | Seaquest: Guided gaze | 0.0002 | 0.0001 | 0.65 (0.53-0.77) | -35% | 91% |
| beyond trained length | Seaquest: Random gaze | 0.0002 | 0.0002 | 0.72 (0.62-0.81) | -28% | 94% |
| beyond trained length | Seaquest: Oracle gaze (not deployable) | 0.0002 | 0.0000 | 0.22 (0.16-0.28) | -78% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Seaquest: Guided gaze | 64 | -1.9 (-22.0 to +25.2) | 72.2 (43.6-102.8) |
| Seaquest: Random gaze | 64 | -1.3 (-13.2 to +11.8) | 57.9 (46.1-69.2) |
