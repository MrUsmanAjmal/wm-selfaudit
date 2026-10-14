## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'RoadRunner' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | RoadRunner: Guided gaze | 0.0153 | 0.0133 | 0.87 (0.67-0.90) | -13% | 91% |
| all imagined frames | RoadRunner: Random gaze | 0.0153 | 0.0107 | 0.70 (0.57-0.90) | -30% | 97% |
| all imagined frames | RoadRunner: Oracle gaze (not deployable) | 0.0153 | 0.0084 | 0.55 (0.34-0.78) | -45% | 100% |
| within trained length | RoadRunner: Guided gaze | 0.0081 | 0.0072 | 0.89 (0.68-0.90) | -11% | 88% |
| within trained length | RoadRunner: Random gaze | 0.0081 | 0.0068 | 0.84 (0.79-0.91) | -16% | 81% |
| within trained length | RoadRunner: Oracle gaze (not deployable) | 0.0081 | 0.0058 | 0.71 (0.38-0.74) | -29% | 91% |
| beyond trained length | RoadRunner: Guided gaze | 0.0225 | 0.0194 | 0.86 (0.62-0.90) | -14% | 91% |
| beyond trained length | RoadRunner: Random gaze | 0.0225 | 0.0146 | 0.65 (0.37-0.91) | -35% | 94% |
| beyond trained length | RoadRunner: Oracle gaze (not deployable) | 0.0225 | 0.0110 | 0.49 (0.13-0.80) | -51% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| RoadRunner: Guided gaze | 64 | -7.6 (-42.7 to +61.3) | 58.2 (44.3-73.3) |
| RoadRunner: Random gaze | 64 | +4.3 (+1.2 to +10.0) | 84.4 (55.5-113.8) |
