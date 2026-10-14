## Feeding the observed patch back into the model

32 clips from 32 videos. Baseline: 'MsPacman' without feedback (3 rollouts per clip). Drift = full-frame MSE of the model's prediction of each frame, made before that frame's patch is seen. Ratio = mean drift with feedback / without, 95% CI over videos (paired by clip).

| Frames | Feedback | Drift without | Drift with | Ratio [95% CI] | Change | Clips improved |
|---|---|---|---|---|---|---|
| all imagined frames | MsPacman: Guided gaze | 0.0006 | 0.0004 | 0.59 (0.54-0.65) | -41% | 97% |
| all imagined frames | MsPacman: Random gaze | 0.0006 | 0.0005 | 0.78 (0.72-0.84) | -22% | 94% |
| all imagined frames | MsPacman: Oracle gaze (not deployable) | 0.0006 | 0.0002 | 0.23 (0.18-0.30) | -77% | 100% |
| within trained length | MsPacman: Guided gaze | 0.0004 | 0.0003 | 0.64 (0.59-0.69) | -36% | 100% |
| within trained length | MsPacman: Random gaze | 0.0004 | 0.0003 | 0.80 (0.67-0.91) | -20% | 84% |
| within trained length | MsPacman: Oracle gaze (not deployable) | 0.0004 | 0.0001 | 0.27 (0.21-0.35) | -73% | 100% |
| beyond trained length | MsPacman: Guided gaze | 0.0009 | 0.0005 | 0.57 (0.50-0.65) | -43% | 94% |
| beyond trained length | MsPacman: Random gaze | 0.0009 | 0.0007 | 0.78 (0.73-0.83) | -22% | 94% |
| beyond trained length | MsPacman: Oracle gaze (not deployable) | 0.0009 | 0.0002 | 0.22 (0.15-0.30) | -78% | 100% |

**The same patches also measure the drift.** Horvitz-Thompson estimate of each feedback rollout's drift from the patches it was shown (no control variate). Bias: total estimate / total true drift - 1; relative error: root mean square over rollouts.

| Feedback | Rollouts | Pooled bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| MsPacman: Guided gaze | 64 | +4.9 (-9.1 to +23.4) | 76.5 (37.2-109.2) |
| MsPacman: Random gaze | 64 | +2.3 (-7.1 to +12.5) | 50.6 (39.2-61.7) |
