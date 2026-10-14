## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'Breakout' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Breakout: Guided gaze | 0.0001 | 0.0001 | 0.46 (0.34-0.59) | -54% | 97% |
| all imagined frames | Breakout: Random gaze | 0.0001 | 0.0001 | 0.84 (0.67-0.98) | -16% | 88% |
| all imagined frames | Breakout: Oracle gaze (not deployable) | 0.0001 | 0.0000 | 0.15 (0.11-0.22) | -85% | 100% |
| within trained length | Breakout: Guided gaze | 0.0001 | 0.0000 | 0.57 (0.47-0.77) | -43% | 97% |
| within trained length | Breakout: Random gaze | 0.0001 | 0.0001 | 0.95 (0.69-1.10) | -5% | 91% |
| within trained length | Breakout: Oracle gaze (not deployable) | 0.0001 | 0.0000 | 0.26 (0.19-0.45) | -74% | 97% |
| beyond trained length | Breakout: Guided gaze | 0.0002 | 0.0001 | 0.43 (0.29-0.59) | -57% | 97% |
| beyond trained length | Breakout: Random gaze | 0.0002 | 0.0002 | 0.81 (0.64-0.95) | -19% | 88% |
| beyond trained length | Breakout: Oracle gaze (not deployable) | 0.0002 | 0.0000 | 0.12 (0.07-0.18) | -88% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Breakout: Guided gaze | 64 | +15.0 (-58.2 to +168.8) | 152.1 (51.2-251.3) |
| Breakout: Random gaze | 64 | -9.8 (-24.9 to +15.4) | 112.0 (55.4-169.1) |
