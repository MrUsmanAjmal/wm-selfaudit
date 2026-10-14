## Minecraft, 50 steps

40 clips from 10 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Minecraft, 50 steps', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 35.0 | 33.4-36.6 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 30.2 | 28.5-32.0 | 0.74 | 0.69-0.82 | x1.34 | 2.0e-14 |
| Smart + CV[visual] | 29.8 | 28.2-31.5 | 0.73 | 0.66-0.80 | x1.38 | 3.7e-14 |
| Negative control: CV[shuffled proxies] | 35.1 | 33.5-36.7 | 1.01 | 1.00-1.01 | x0.99 | 1.9e-14 |
| Uniform + shrunk CV[visual] | 29.4 | 28.1-30.6 | 0.70 | 0.67-0.74 | x1.42 | 8.5e-15 |
| Uniform + CV[visual+disagreement] | 28.8 | 27.4-30.2 | 0.68 | 0.62-0.73 | x1.48 | 1.6e-14 |
| Uniform + shrunk CV[visual+disagreement] | 27.8 | 26.9-28.8 | 0.63 | 0.60-0.66 | x1.59 | 9.1e-15 |
| Smart + CV[visual+disagreement] | 31.6 | 28.6-35.1 | 0.81 | 0.66-1.01 | x1.23 | 2.3e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 29.5 | 27.9-31.1 | 0.71 | 0.65-0.78 | x1.41 | 1.7e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 31.0 | 28.2-34.5 | 0.78 | 0.64-0.97 | x1.27 | 2.4e-14 |
| Oracle Neyman (not deployable) | 15.0 | 14.0-15.9 | 0.18 | 0.16-0.22 | x5.41 | 2.5e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +47.1 (+20.6 to +75.7) | 103.5 (73.8-129.7) |
| all imagined frames | Rollout disagreement (no real data) | -32.5 (-44.8 to -18.5) | 54.9 (49.7-59.7) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +41.3 (+16.8 to +67.0) | 90.3 (65.7-112.4) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 31.6 (28.6-35.1) |
| within trained length | Visual predictor (no real data) | +61.0 (+20.2 to +108.0) | 139.5 (84.0-186.6) |
| within trained length | Rollout disagreement (no real data) | -28.1 (-42.2 to -14.3) | 52.4 (44.4-59.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +55.2 (+17.0 to +96.2) | 121.4 (77.5-158.0) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 81.0 (57.2-104.3) |
| beyond trained length | Visual predictor (no real data) | +55.1 (+29.3 to +84.1) | 113.8 (87.4-139.3) |
| beyond trained length | Rollout disagreement (no real data) | -30.8 (-43.1 to -16.6) | 57.3 (50.3-64.8) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +47.5 (+24.6 to +71.9) | 98.7 (76.2-119.4) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 33.2 (31.6-35.0) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 1.85 | 1.47-2.35 | 1.09 | 0.97-1.27 | 0.75 |
| within trained length | 1.81 | 1.41-2.33 | 1.13 | 0.99-1.43 | 0.81 |
| beyond trained length | 1.87 | 1.49-2.38 | 1.08 | 0.97-1.26 | 0.70 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 35.0 (33.4-36.6) | 24.8 (23.6-25.9) | 20.2 (19.3-21.1) | 17.5 (16.7-18.3) |
| 1 rollout, Uniform + shrunk CV[visual] | 29.4 (28.1-30.6) | 20.8 (19.8-21.7) | 17.0 (16.2-17.7) | 14.7 (14.0-15.3) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 29.5 (27.9-31.1) | 20.8 (19.7-22.0) | 17.0 (16.1-18.0) | 14.7 (13.9-15.6) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 27.8 (26.9-28.8) | 19.6 (19.0-20.4) | 16.0 (15.5-16.6) | 13.9 (13.5-14.4) |


## Minecraft, 100 steps

16 clips from 10 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Minecraft, 100 steps', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 35.0 | 32.7-37.5 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 29.2 | 26.8-31.7 | 0.70 | 0.58-0.80 | x1.43 | 9.8e-15 |
| Smart + CV[visual] | 29.7 | 27.2-32.1 | 0.72 | 0.59-0.84 | x1.39 | 3.3e-14 |
| Negative control: CV[shuffled proxies] | 35.1 | 32.8-37.6 | 1.00 | 1.00-1.01 | x1.00 | 8.9e-15 |
| Uniform + shrunk CV[visual] | 29.2 | 26.8-31.7 | 0.70 | 0.58-0.80 | x1.43 | 9.8e-15 |
| Uniform + CV[visual+disagreement] | 27.5 | 24.5-30.4 | 0.62 | 0.47-0.75 | x1.61 | 1.2e-14 |
| Uniform + shrunk CV[visual+disagreement] | 27.6 | 24.6-30.4 | 0.62 | 0.47-0.75 | x1.61 | 1.2e-14 |
| Smart + CV[visual+disagreement] | 29.3 | 25.6-32.4 | 0.70 | 0.52-0.88 | x1.43 | 2.0e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 28.2 | 25.6-30.7 | 0.65 | 0.52-0.77 | x1.54 | 8.6e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 29.3 | 26.1-32.2 | 0.70 | 0.54-0.87 | x1.42 | 1.7e-14 |
| Oracle Neyman (not deployable) | 15.5 | 14.0-16.9 | 0.20 | 0.16-0.23 | x5.10 | 2.7e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +50.4 (+0.8 to +107.1) | 103.7 (66.9-137.2) |
| all imagined frames | Rollout disagreement (no real data) | -36.8 (-53.0 to -15.6) | 50.8 (39.6-59.2) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +47.2 (-0.6 to +104.0) | 99.0 (61.1-136.4) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 29.3 (25.6-32.4) |
| within trained length | Visual predictor (no real data) | +91.2 (+0.7 to +197.5) | 197.3 (56.3-286.4) |
| within trained length | Rollout disagreement (no real data) | -29.7 (-55.4 to -1.1) | 59.5 (50.6-67.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +88.3 (-3.0 to +194.3) | 191.5 (48.9-281.4) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 66.2 (49.2-85.3) |
| beyond trained length | Visual predictor (no real data) | +53.0 (+4.6 to +111.3) | 109.2 (73.5-144.9) |
| beyond trained length | Rollout disagreement (no real data) | -35.1 (-52.2 to -12.4) | 51.9 (40.4-60.1) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +48.9 (+3.2 to +105.4) | 103.2 (67.7-138.1) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 34.4 (29.0-39.1) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 2.11 | 1.45-2.64 | 1.22 | 1.00-1.38 | 0.71 |
| within trained length | 1.98 | 1.35-2.68 | 1.32 | 1.02-1.64 | 0.80 |
| beyond trained length | 2.17 | 1.46-2.69 | 1.19 | 0.99-1.34 | 0.63 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 35.0 (32.7-37.5) | 24.7 (23.2-26.5) | 20.2 (18.9-21.7) | 17.5 (16.4-18.8) |
| 1 rollout, Uniform + CV[visual] | 29.2 (26.8-31.7) | 20.7 (18.9-22.4) | 16.9 (15.5-18.3) | 14.6 (13.4-15.9) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 28.2 (25.6-30.7) | 19.9 (18.1-21.7) | 16.3 (14.8-17.7) | 14.1 (12.8-15.4) |
| 3 rollouts, Uniform + CV[visual+disagreement] | 27.5 (24.5-30.4) | 19.5 (17.3-21.5) | 15.9 (14.2-17.6) | 13.8 (12.3-15.2) |


## Findings

- **Uniform + CV[visual]**: variance x0.74 of uniform (95% CI 0.69-0.82), the accuracy of 1.34 uniform patches per frame. Reduction is statistically clear.
- **Smart + CV[visual]**: variance x0.73 of uniform (95% CI 0.66-0.80), the accuracy of 1.38 uniform patches per frame. Reduction is statistically clear.
- **Negative control: CV[shuffled proxies]**: variance x1.01 of uniform (95% CI 1.00-1.01), the accuracy of 0.99 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + shrunk CV[visual]**: variance x0.70 of uniform (95% CI 0.67-0.74), the accuracy of 1.42 uniform patches per frame. Reduction is statistically clear.
- **Uniform + CV[visual+disagreement]**: variance x0.68 of uniform (95% CI 0.62-0.73), the accuracy of 1.48 uniform patches per frame. Reduction is statistically clear.
- **Uniform + shrunk CV[visual+disagreement]**: variance x0.63 of uniform (95% CI 0.60-0.66), the accuracy of 1.59 uniform patches per frame. Reduction is statistically clear.
- **Smart + CV[visual+disagreement]**: variance x0.81 of uniform (95% CI 0.66-1.01), the accuracy of 1.23 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + CV[visual+disagreement], 2 rollouts**: variance x0.71 of uniform (95% CI 0.65-0.78), the accuracy of 1.41 uniform patches per frame. Reduction is statistically clear.
- **Smart + CV[visual+disagreement], 2 rollouts**: variance x0.78 of uniform (95% CI 0.64-0.97), the accuracy of 1.27 uniform patches per frame. Reduction is statistically clear.
- **Rollouts versus patches** (best audit of each budget: Uniform + shrunk CV[visual+disagreement] for 3 rollouts, Uniform + shrunk CV[visual] for 1): with 3 rollouts and 1 patch per frame the audit is as accurate as a single-rollout audit with 1.12 patches per frame (95% CI 1.06-1.18). Variance of 3 rollouts + 1 patch relative to 1 rollout + 2 patches: 1.79 (1.70-1.89).
- **Minecraft, 50 steps, all imagined frames, Rollout disagreement**: bias -32.5% (-44.8 to -18.5), CI excludes zero.
- **Minecraft, 50 steps, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +41.3% (+16.8 to +67.0), CI excludes zero.
- **Minecraft, 50 steps, within trained length, Rollout disagreement**: bias -28.1% (-42.2 to -14.3), CI excludes zero.
- **Minecraft, 50 steps, within trained length, Calibrated predictor (visual+disagreement)**: bias +55.2% (+17.0 to +96.2), CI excludes zero.
- **Minecraft, 50 steps, beyond trained length, Rollout disagreement**: bias -30.8% (-43.1 to -16.6), CI excludes zero.
- **Minecraft, 50 steps, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +47.5% (+24.6 to +71.9), CI excludes zero.
- **Minecraft, 100 steps, all imagined frames, Rollout disagreement**: bias -36.8% (-53.0 to -15.6), CI excludes zero.
- **Minecraft, 100 steps, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +47.2% (-0.6 to +104.0), CI includes zero.
- **Minecraft, 100 steps, within trained length, Rollout disagreement**: bias -29.7% (-55.4 to -1.1), CI excludes zero.
- **Minecraft, 100 steps, within trained length, Calibrated predictor (visual+disagreement)**: bias +88.3% (-3.0 to +194.3), CI includes zero.
- **Minecraft, 100 steps, beyond trained length, Rollout disagreement**: bias -35.1% (-52.2 to -12.4), CI excludes zero.
- **Minecraft, 100 steps, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +48.9% (+3.2 to +105.4), CI excludes zero.
- **Unbiasedness**: the exact expectation of every audit equals the truth to numerical precision (max bias column), in every condition and horizon, including the negative control.
