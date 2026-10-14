## Calibration with a perceptual distance (LPIPS)

Mean LPIPS(rollout, real) / mean LPIPS(rollout, other rollouts); 1 = calibrated for any distance. Bias: disagreement used as the drift estimate. 95% CI over videos.

| Condition | Frames | Error / disagreement [95% CI] | Bias of disagreement (%) [95% CI] |
|---|---|---|---|
| Breakout | all imagined frames | 8.14 (3.43-52.77) | -42.3 (-98.2 to +59.2) |
| Breakout | within trained length | 9.92 (2.59-1681.51) | -83.6 (-99.6 to -54.4) |
| Breakout | beyond trained length | 7.73 (3.46-50.64) | -18.2 (-98.5 to +133.3) |
| Pong | all imagined frames | 153.69 (49.26-1548.23) | -98.1 (-99.7 to -95.0) |
| Pong | within trained length | 90.57 (19.90-820.63) | -97.6 (-99.6 to -93.6) |
| Pong | beyond trained length | 699.86 (64.99-2621.67) | -98.4 (-99.7 to -95.9) |
| Boxing | all imagined frames | 1.60 (1.35-1.94) | -27.4 (-41.0 to -13.0) |
| Boxing | within trained length | 2.71 (2.03-3.86) | -52.6 (-67.1 to -36.8) |
| Boxing | beyond trained length | 1.32 (1.13-1.58) | -10.2 (-25.3 to +5.3) |
| MsPacman | all imagined frames | 8.46 (5.41-15.22) | -86.5 (-92.4 to -79.7) |
| MsPacman | within trained length | 14.77 (7.08-48.26) | -90.1 (-95.8 to -83.1) |
| MsPacman | beyond trained length | 7.05 (4.63-12.32) | -84.4 (-91.3 to -76.3) |
| Seaquest | all imagined frames | 24.16 (10.50-93.99) | -94.6 (-98.5 to -87.9) |
| Seaquest | within trained length | 136.30 (57.83-382.60) | -97.7 (-99.4 to -95.2) |
| Seaquest | beyond trained length | 19.04 (8.16-80.99) | -93.8 (-98.1 to -86.6) |
| Freeway | all imagined frames | 110.42 (66.01-191.80) | -98.2 (-98.8 to -97.4) |
| Freeway | within trained length | 129.32 (81.00-187.46) | -98.3 (-98.7 to -97.9) |
| Freeway | beyond trained length | 104.91 (57.68-219.43) | -98.2 (-98.9 to -97.1) |
| Asterix | all imagined frames | 64.00 (23.41-815.05) | -84.6 (-99.9 to -55.4) |
| Asterix | within trained length | 71.68 (22.21-5660.39) | -87.7 (-99.9 to -63.8) |
| Asterix | beyond trained length | 61.62 (23.54-755.38) | -82.9 (-99.9 to -50.4) |
| RoadRunner | all imagined frames | 24.08 (7.17-60.37) | -79.7 (-88.8 to -69.2) |
| RoadRunner | within trained length | 22.59 (4.66-75.38) | -74.5 (-88.3 to -56.4) |
| RoadRunner | beyond trained length | 24.68 (7.45-57.34) | -78.6 (-88.3 to -67.3) |
