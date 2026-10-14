## Calibration with a perceptual distance (LPIPS)

Mean LPIPS(rollout, real) / mean LPIPS(rollout, other rollouts); 1 = calibrated for any distance. Bias: disagreement used as the drift estimate. 95% CI over videos.

| Condition | Frames | Error / disagreement [95% CI] | Bias of disagreement (%) [95% CI] |
|---|---|---|---|
| Minecraft, 72 test videos | all imagined frames | 1.34 (1.23-1.46) | -20.1 (-26.3 to -13.9) |
| Minecraft, 72 test videos | within trained length | 1.32 (1.20-1.46) | -20.3 (-27.0 to -13.3) |
| Minecraft, 72 test videos | beyond trained length | 1.34 (1.23-1.48) | -18.5 (-25.2 to -11.9) |
| Minecraft at 2x speed, 40 test videos | all imagined frames | 1.77 (1.48-2.19) | -43.5 (-54.0 to -32.9) |
| Minecraft at 2x speed, 40 test videos | within trained length | 1.94 (1.50-2.60) | -47.8 (-60.7 to -32.4) |
| Minecraft at 2x speed, 40 test videos | beyond trained length | 1.69 (1.43-2.08) | -40.5 (-51.7 to -29.7) |
