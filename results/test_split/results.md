## Minecraft, 72 test videos

72 clips from 72 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Minecraft, 72 test videos', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 35.0 | 33.4-36.6 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 33.5 | 30.8-36.2 | 0.92 | 0.80-1.04 | x1.09 | 1.6e-14 |
| Smart + CV[visual] | 31.2 | 29.2-33.4 | 0.80 | 0.72-0.89 | x1.25 | 3.1e-14 |
| Negative control: CV[shuffled proxies] | 35.1 | 33.5-36.7 | 1.01 | 1.01-1.01 | x0.99 | 1.6e-14 |
| Uniform + shrunk CV[visual] | 29.7 | 28.2-31.3 | 0.72 | 0.68-0.76 | x1.38 | 9.7e-15 |
| Uniform + CV[visual+disagreement] | 32.2 | 29.0-35.8 | 0.85 | 0.71-1.01 | x1.18 | 1.5e-14 |
| Uniform + shrunk CV[visual+disagreement] | 28.1 | 26.3-29.8 | 0.64 | 0.59-0.69 | x1.55 | 9.7e-15 |
| Smart + CV[visual+disagreement] | 29.7 | 27.3-32.4 | 0.72 | 0.63-0.83 | x1.39 | 3.8e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 33.3 | 30.0-36.7 | 0.90 | 0.76-1.06 | x1.11 | 1.4e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 30.2 | 28.0-32.6 | 0.74 | 0.66-0.84 | x1.34 | 3.3e-14 |
| Oracle Neyman (not deployable) | 13.8 | 12.8-14.8 | 0.16 | 0.14-0.17 | x6.39 | 4.4e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +67.9 (+42.9 to +94.9) | 144.7 (112.9-174.7) |
| all imagined frames | Rollout disagreement (no real data) | -13.7 (-24.5 to -2.8) | 56.8 (46.7-67.2) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +58.7 (+37.7 to +80.4) | 122.7 (98.5-145.4) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 29.7 (27.3-32.4) |
| within trained length | Visual predictor (no real data) | +81.9 (+52.9 to +113.0) | 160.6 (124.4-194.2) |
| within trained length | Rollout disagreement (no real data) | -9.2 (-20.4 to +2.7) | 58.4 (45.6-72.0) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +66.8 (+44.7 to +89.8) | 127.0 (102.7-149.4) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 54.0 (48.0-60.1) |
| beyond trained length | Visual predictor (no real data) | +75.9 (+48.9 to +104.4) | 160.5 (126.3-192.2) |
| beyond trained length | Rollout disagreement (no real data) | -11.0 (-22.8 to +1.0) | 63.5 (51.8-75.9) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +66.9 (+44.0 to +90.5) | 139.6 (111.3-166.9) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 36.5 (32.5-41.1) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 1.60 | 1.36-1.89 | 1.03 | 0.95-1.12 | 0.77 |
| within trained length | 1.49 | 1.24-1.80 | 1.01 | 0.90-1.17 | 0.84 |
| beyond trained length | 1.64 | 1.38-1.95 | 1.03 | 0.95-1.12 | 0.70 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 35.0 (33.4-36.6) | 24.7 (23.6-25.9) | 20.2 (19.3-21.1) | 17.5 (16.7-18.3) |
| 1 rollout, Uniform + shrunk CV[visual] | 29.7 (28.2-31.3) | 21.0 (20.0-22.2) | 17.2 (16.3-18.1) | 14.9 (14.1-15.7) |
| 2 rollouts, Smart + CV[visual+disagreement] | 30.2 (28.0-32.6) | 21.3 (19.8-23.1) | 17.4 (16.1-18.8) | 15.1 (14.0-16.3) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 28.1 (26.3-29.8) | 19.9 (18.6-21.1) | 16.2 (15.2-17.2) | 14.0 (13.2-14.9) |


## Minecraft at 2x speed, 40 test videos

16 clips from 16 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Minecraft, 72 test videos', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 33.5 | 31.0-36.1 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 26.7 | 24.9-28.2 | 0.63 | 0.55-0.74 | x1.58 | 7.8e-15 |
| Smart + CV[visual] | 26.3 | 24.5-27.8 | 0.61 | 0.52-0.73 | x1.63 | 1.6e-14 |
| Negative control: CV[shuffled proxies] | 33.6 | 31.0-36.1 | 1.00 | 1.00-1.00 | x1.00 | 8.6e-15 |
| Uniform + shrunk CV[visual] | 29.0 | 27.1-30.7 | 0.75 | 0.68-0.82 | x1.34 | 3.4e-15 |
| Uniform + CV[visual+disagreement] | 25.7 | 23.4-27.7 | 0.59 | 0.48-0.70 | x1.71 | 6.7e-15 |
| Uniform + shrunk CV[visual+disagreement] | 28.4 | 26.3-30.3 | 0.72 | 0.65-0.80 | x1.39 | 3.5e-15 |
| Smart + CV[visual+disagreement] | 25.1 | 22.8-27.1 | 0.56 | 0.45-0.68 | x1.79 | 1.4e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 26.0 | 23.9-27.8 | 0.60 | 0.50-0.71 | x1.66 | 5.4e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 25.5 | 23.4-27.3 | 0.58 | 0.48-0.70 | x1.73 | 8.6e-15 |
| Oracle Neyman (not deployable) | 15.0 | 13.2-16.8 | 0.20 | 0.17-0.23 | x4.96 | 1.3e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | -3.8 (-25.3 to +19.0) | 46.1 (33.7-57.9) |
| all imagined frames | Rollout disagreement (no real data) | -52.3 (-63.5 to -41.2) | 57.7 (47.9-67.0) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | -9.9 (-27.6 to +7.7) | 38.5 (29.8-46.8) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 25.1 (22.8-27.1) |
| within trained length | Visual predictor (no real data) | +3.4 (-24.3 to +33.0) | 59.6 (42.3-75.0) |
| within trained length | Rollout disagreement (no real data) | -44.7 (-68.1 to -11.7) | 79.5 (58.6-104.8) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | -2.6 (-30.1 to +27.0) | 63.5 (39.0-90.1) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 39.6 (33.9-45.3) |
| beyond trained length | Visual predictor (no real data) | -2.5 (-23.0 to +18.8) | 44.0 (33.1-54.7) |
| beyond trained length | Rollout disagreement (no real data) | -50.5 (-62.4 to -38.6) | 57.4 (47.6-66.9) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | -7.4 (-24.6 to +9.6) | 37.6 (29.2-45.5) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 30.6 (27.6-33.3) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 2.40 | 1.85-3.26 | 1.26 | 1.09-1.52 | 0.69 |
| within trained length | 2.87 | 1.75-4.35 | 1.48 | 1.00-2.43 | 0.74 |
| beyond trained length | 2.25 | 1.71-3.10 | 1.23 | 1.06-1.48 | 0.65 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 33.5 (31.0-36.1) | 23.7 (21.9-25.5) | 19.3 (17.9-20.8) | 16.8 (15.5-18.0) |
| 1 rollout, Smart + CV[visual] | 26.3 (24.5-27.8) | 18.6 (17.4-19.6) | 15.2 (14.2-16.0) | 13.1 (12.3-13.9) |
| 2 rollouts, Smart + CV[visual+disagreement] | 25.5 (23.4-27.3) | 18.0 (16.5-19.3) | 14.7 (13.5-15.8) | 12.7 (11.7-13.7) |
| 3 rollouts, Smart + CV[visual+disagreement] | 25.1 (22.8-27.1) | 17.7 (16.1-19.2) | 14.5 (13.1-15.7) | 12.5 (11.4-13.6) |


## Findings

- **Uniform + CV[visual]**: variance x0.92 of uniform (95% CI 0.80-1.04), the accuracy of 1.09 uniform patches per frame. Not distinguishable from uniform.
- **Smart + CV[visual]**: variance x0.80 of uniform (95% CI 0.72-0.89), the accuracy of 1.25 uniform patches per frame. Reduction is statistically clear.
- **Negative control: CV[shuffled proxies]**: variance x1.01 of uniform (95% CI 1.01-1.01), the accuracy of 0.99 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + shrunk CV[visual]**: variance x0.72 of uniform (95% CI 0.68-0.76), the accuracy of 1.38 uniform patches per frame. Reduction is statistically clear.
- **Uniform + CV[visual+disagreement]**: variance x0.85 of uniform (95% CI 0.71-1.01), the accuracy of 1.18 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + shrunk CV[visual+disagreement]**: variance x0.64 of uniform (95% CI 0.59-0.69), the accuracy of 1.55 uniform patches per frame. Reduction is statistically clear.
- **Smart + CV[visual+disagreement]**: variance x0.72 of uniform (95% CI 0.63-0.83), the accuracy of 1.39 uniform patches per frame. Reduction is statistically clear.
- **Uniform + CV[visual+disagreement], 2 rollouts**: variance x0.90 of uniform (95% CI 0.76-1.06), the accuracy of 1.11 uniform patches per frame. Not distinguishable from uniform.
- **Smart + CV[visual+disagreement], 2 rollouts**: variance x0.74 of uniform (95% CI 0.66-0.84), the accuracy of 1.34 uniform patches per frame. Reduction is statistically clear.
- **Rollouts versus patches** (best audit of each budget: Uniform + shrunk CV[visual+disagreement] for 3 rollouts, Uniform + shrunk CV[visual] for 1): with 3 rollouts and 1 patch per frame the audit is as accurate as a single-rollout audit with 1.12 patches per frame (95% CI 1.08-1.17). Variance of 3 rollouts + 1 patch relative to 1 rollout + 2 patches: 1.78 (1.70-1.86).
- **Minecraft, 72 test videos, all imagined frames, Rollout disagreement**: bias -13.7% (-24.5 to -2.8), CI excludes zero.
- **Minecraft, 72 test videos, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +58.7% (+37.7 to +80.4), CI excludes zero.
- **Minecraft, 72 test videos, within trained length, Rollout disagreement**: bias -9.2% (-20.4 to +2.7), CI includes zero.
- **Minecraft, 72 test videos, within trained length, Calibrated predictor (visual+disagreement)**: bias +66.8% (+44.7 to +89.8), CI excludes zero.
- **Minecraft, 72 test videos, beyond trained length, Rollout disagreement**: bias -11.0% (-22.8 to +1.0), CI includes zero.
- **Minecraft, 72 test videos, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +66.9% (+44.0 to +90.5), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, all imagined frames, Rollout disagreement**: bias -52.3% (-63.5 to -41.2), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, all imagined frames, Calibrated predictor (visual+disagreement)**: bias -9.9% (-27.6 to +7.7), CI includes zero.
- **Minecraft at 2x speed, 40 test videos, within trained length, Rollout disagreement**: bias -44.7% (-68.1 to -11.7), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, within trained length, Calibrated predictor (visual+disagreement)**: bias -2.6% (-30.1 to +27.0), CI includes zero.
- **Minecraft at 2x speed, 40 test videos, beyond trained length, Rollout disagreement**: bias -50.5% (-62.4 to -38.6), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, beyond trained length, Calibrated predictor (visual+disagreement)**: bias -7.4% (-24.6 to +9.6), CI includes zero.
- **Unbiasedness**: the exact expectation of every audit equals the truth to numerical precision (max bias column), in every condition and horizon, including the negative control.
