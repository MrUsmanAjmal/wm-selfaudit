## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'Boxing' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Boxing: Guided gaze | 0.0035 | 0.0018 | 0.50 (0.46-0.54) | -50% | 100% |
| all imagined frames | Boxing: Random gaze | 0.0035 | 0.0027 | 0.77 (0.73-0.82) | -23% | 91% |
| all imagined frames | Boxing: Oracle gaze (not deployable) | 0.0035 | 0.0008 | 0.24 (0.21-0.27) | -76% | 100% |
| within trained length | Boxing: Guided gaze | 0.0025 | 0.0015 | 0.59 (0.53-0.65) | -41% | 97% |
| within trained length | Boxing: Random gaze | 0.0025 | 0.0021 | 0.84 (0.78-0.90) | -16% | 81% |
| within trained length | Boxing: Oracle gaze (not deployable) | 0.0025 | 0.0008 | 0.34 (0.29-0.38) | -66% | 100% |
| beyond trained length | Boxing: Guided gaze | 0.0045 | 0.0021 | 0.45 (0.41-0.50) | -55% | 100% |
| beyond trained length | Boxing: Random gaze | 0.0045 | 0.0033 | 0.74 (0.68-0.79) | -26% | 91% |
| beyond trained length | Boxing: Oracle gaze (not deployable) | 0.0045 | 0.0009 | 0.19 (0.15-0.23) | -81% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Boxing: Guided gaze | 64 | +5.4 (-10.9 to +25.9) | 52.3 (35.1-69.5) |
| Boxing: Random gaze | 64 | +5.7 (-4.3 to +16.4) | 51.1 (38.6-64.5) |
