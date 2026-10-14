## DIAMOND (Atari), one window per real episode

Error / disagreement: mean real error over mean disagreement between 3 rollouts (1 = calibrated), with the default deterministic sampler and with a stochastic sampler. Bias: disagreement used as the drift estimate (%). CV: variance of uniform sampling with the visual+disagreement control variate, relative to plain uniform sampling (1 real 16x16 patch per frame); shrunk CV: the same with the control-variate weight chosen on the other episodes. Feedback: drift with one real patch per frame fed back / without. 95% CIs resample episodes.

| Game | Episodes | Error / disagreement | Error / disagreement, stochastic sampler | Bias of disagreement (%) | CV variance vs uniform | Shrunk CV variance vs uniform | Feedback: guided | Feedback: random | Feedback: oracle |
|---|---|---|---|---|---|---|---|---|---|
| Breakout | 32 | 15.7 [5.7, 152.6] | 9.7 [5.5, 20.3] | -80.6 | 2.82 [1.57, 4.85] | 1.03 [1.00, 1.09] | 0.46 [0.34, 0.59] | 0.84 [0.67, 0.98] | 0.15 [0.11, 0.22] |
| Pong | 32 | 144 [91, 651] | 3.9 [2.3, 44.0] | -99.5 | 1.37 [1.16, 2.07] | 1.01 [1.00, 1.04] | 0.75 [0.63, 0.96] | 0.90 [0.85, 0.97] | 0.60 [0.39, 0.94] |
| Boxing | 32 | 1.8 [1.5, 2.1] | 1.4 [1.2, 1.6] | -40.3 | 0.43 [0.39, 0.47] | 0.43 [0.39, 0.47] | 0.50 [0.46, 0.54] | 0.77 [0.73, 0.82] | 0.24 [0.21, 0.27] |
| MsPacman | 32 | 7.2 [4.7, 13.4] | 3.0 [2.2, 4.3] | -87.6 | 13.99 [1.02, 39.23] | 1.00 [1.00, 1.00] | 0.59 [0.54, 0.65] | 0.78 [0.72, 0.84] | 0.23 [0.18, 0.30] |
| Seaquest | 32 | 18.8 [10.6, 54.5] | 3.1 [2.4, 4.2] | -95.5 | 1.09 [0.99, 1.20] | 0.99 [0.97, 1.03] | 0.69 [0.59, 0.78] | 0.76 [0.69, 0.84] | 0.26 [0.21, 0.33] |
| Freeway | 32 | 90 [54, 155] | 11.2 [5.8, 45.5] | -98.7 | 2.09 [1.18, 4.09] | 0.99 [0.98, 1.01] | 0.69 [0.59, 0.81] | 0.81 [0.77, 0.87] | 0.42 [0.33, 0.54] |
| Asterix | 32 | 49 [22, 262] | 5.2 [2.6, 13.3] | -94.4 | 6.13 [0.94, 18.15] | 1.29 [1.00, 1.99] | 0.55 [0.47, 0.62] | 0.61 [0.55, 0.67] | 0.09 [0.07, 0.12] |
| RoadRunner | 32 | 38 [5, 105] | 10.6 [1.5, 26.5] | -74.6 | 42.65 [21.42, 70.24] | 1.00 [1.00, 1.00] | 0.87 [0.67, 0.90] | 0.70 [0.57, 0.90] | 0.55 [0.34, 0.78] |

Across 8 games: error / disagreement 2–144 with the default sampler and 1.4–11.2 with the stochastic sampler; control-variate variance ratio 0.43–42.65 (shrunk: 0.43–1.29); feedback ratio 0.46–0.87 (guided), 0.61–0.90 (random), 0.09–0.60 (oracle).
