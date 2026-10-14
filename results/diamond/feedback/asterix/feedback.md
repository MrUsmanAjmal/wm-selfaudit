## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'Asterix' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | Asterix: Guided gaze | 0.0010 | 0.0006 | 0.55 (0.47-0.62) | -45% | 100% |
| all imagined frames | Asterix: Random gaze | 0.0010 | 0.0006 | 0.61 (0.55-0.67) | -39% | 100% |
| all imagined frames | Asterix: Oracle gaze (not deployable) | 0.0010 | 0.0001 | 0.09 (0.07-0.12) | -91% | 100% |
| within trained length | Asterix: Guided gaze | 0.0006 | 0.0004 | 0.65 (0.54-0.75) | -35% | 100% |
| within trained length | Asterix: Random gaze | 0.0006 | 0.0004 | 0.72 (0.65-0.81) | -28% | 94% |
| within trained length | Asterix: Oracle gaze (not deployable) | 0.0006 | 0.0001 | 0.16 (0.12-0.19) | -84% | 100% |
| beyond trained length | Asterix: Guided gaze | 0.0015 | 0.0007 | 0.51 (0.42-0.60) | -49% | 97% |
| beyond trained length | Asterix: Random gaze | 0.0015 | 0.0008 | 0.56 (0.50-0.63) | -44% | 100% |
| beyond trained length | Asterix: Oracle gaze (not deployable) | 0.0015 | 0.0001 | 0.07 (0.04-0.10) | -93% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| Asterix: Guided gaze | 64 | -3.4 (-24.9 to +18.9) | 97.0 (58.9-136.1) |
| Asterix: Random gaze | 64 | +10.5 (-4.2 to +24.1) | 60.9 (50.2-71.4) |
