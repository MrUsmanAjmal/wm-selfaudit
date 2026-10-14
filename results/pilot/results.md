**Data**: float dumps; 3 run(s) x 8 clips; 8 imagined frames per clip after 2 real context frames; 16 patches per frame, 1 inspected.

| Method | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 52.7 | 44.9-60.2 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 46.0 | 36.4-53.9 | 0.76 | 0.57-1.06 | x1.31 | 1.3e-14 |
| Smart + CV[visual] | 38.4 | 32.9-44.5 | 0.53 | 0.44-0.61 | x1.88 | 2.6e-14 |
| Negative control: CV[shuffled proxies] | 52.7 | 45.0-60.2 | 1.00 | 1.00-1.01 | x1.00 | 1.7e-14 |
| Uniform + CV[visual+disagreement] | 38.7 | 31.0-47.4 | 0.54 | 0.37-0.71 | x1.85 | 1.2e-14 |
| Smart + CV[visual+disagreement] | 30.9 | 24.8-37.0 | 0.35 | 0.25-0.46 | x2.90 | 1.9e-14 |
| Oracle Neyman (not deployable) | 16.1 | 12.6-20.6 | 0.09 | 0.05-0.18 | x10.67 | 2.5e-14 |

- **Uniform + CV[visual]**: variance x0.76 of uniform (95% CI 0.57-1.06), i.e. the accuracy of 1.31 uniform patches per frame. Not statistically distinguishable from uniform with this many clips.
- **Smart + CV[visual]**: variance x0.53 of uniform (95% CI 0.44-0.61), i.e. the accuracy of 1.88 uniform patches per frame. Reduction is statistically clear (CI below 1).
- **Negative control: CV[shuffled proxies]**: variance x1.00 of uniform (95% CI 1.00-1.01), i.e. the accuracy of 1.00 uniform patches per frame. Not statistically distinguishable from uniform with this many clips.
- **Uniform + CV[visual+disagreement]**: variance x0.54 of uniform (95% CI 0.37-0.71), i.e. the accuracy of 1.85 uniform patches per frame. Reduction is statistically clear (CI below 1).
- **Smart + CV[visual+disagreement]**: variance x0.35 of uniform (95% CI 0.25-0.46), i.e. the accuracy of 2.90 uniform patches per frame. Reduction is statistically clear (CI below 1).
- **Calibration**: patch-level Spearman correlation between rollout disagreement and the true error is 0.88; slope through origin 0.91 (1.0 = perfectly calibrated; >1 = the model is over-confident, its samples agree more than they match reality).
- **Unbiasedness**: the exact expectation of every estimator equals the truth to numerical precision (max bias column), including the negative control, as the theory requires.
- **Proxy relevance** (Spearman with the true patch error): disagreement 0.88, texture 0.49, motion 0.79, time 0.26
