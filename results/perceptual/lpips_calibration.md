## Calibration with a perceptual distance (LPIPS)

Mean LPIPS(rollout, real) / mean LPIPS(rollout, other rollouts); 1 = calibrated for any distance. Bias: disagreement used as the drift estimate. 95% CI over videos.

| Condition | Frames | Error / disagreement [95% CI] | Bias of disagreement (%) [95% CI] |
|---|---|---|---|
| Minecraft | all imagined frames | 1.48 (1.38-1.60) | -32.3 (-36.2 to -27.6) |
| Minecraft | within trained length | 1.50 (1.33-1.72) | -31.6 (-38.8 to -24.5) |
| Minecraft | beyond trained length | 1.48 (1.39-1.57) | -30.4 (-34.0 to -26.7) |
| Minecraft at 2x speed | all imagined frames | 1.67 (1.52-1.91) | -41.9 (-49.0 to -36.1) |
| Minecraft at 2x speed | within trained length | 1.85 (1.61-2.23) | -47.4 (-55.4 to -39.7) |
| Minecraft at 2x speed | beyond trained length | 1.58 (1.44-1.81) | -37.8 (-45.9 to -31.3) |
