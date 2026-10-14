## Minecraft

40 clips from 10 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Minecraft', leaving the evaluated video out. 95% CIs resample whole videos.

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


## Minecraft at 2x speed

24 clips from 10 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Minecraft', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 33.0 | 31.3-34.7 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 26.4 | 25.0-27.5 | 0.64 | 0.57-0.70 | x1.57 | 1.6e-14 |
| Smart + CV[visual] | 26.1 | 24.7-27.3 | 0.62 | 0.56-0.70 | x1.60 | 1.2e-14 |
| Negative control: CV[shuffled proxies] | 33.0 | 31.3-34.7 | 1.00 | 1.00-1.00 | x1.00 | 1.8e-14 |
| Uniform + shrunk CV[visual] | 27.1 | 25.7-28.3 | 0.68 | 0.61-0.74 | x1.48 | 6.0e-15 |
| Uniform + CV[visual+disagreement] | 25.1 | 23.5-26.4 | 0.58 | 0.50-0.65 | x1.73 | 8.5e-15 |
| Uniform + shrunk CV[visual+disagreement] | 25.9 | 24.4-27.2 | 0.62 | 0.55-0.69 | x1.62 | 3.8e-15 |
| Smart + CV[visual+disagreement] | 26.3 | 24.0-28.3 | 0.63 | 0.53-0.75 | x1.58 | 1.5e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 25.5 | 23.9-26.7 | 0.59 | 0.52-0.67 | x1.68 | 5.5e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 25.9 | 24.0-27.6 | 0.62 | 0.53-0.72 | x1.62 | 1.9e-14 |
| Oracle Neyman (not deployable) | 14.1 | 13.6-14.8 | 0.18 | 0.17-0.20 | x5.45 | 1.5e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +8.6 (-17.4 to +36.9) | 54.5 (40.0-66.6) |
| all imagined frames | Rollout disagreement (no real data) | -48.7 (-57.9 to -39.6) | 58.4 (51.7-64.0) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +5.2 (-16.0 to +28.5) | 46.2 (35.5-55.9) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 26.3 (24.0-28.3) |
| within trained length | Visual predictor (no real data) | -4.8 (-25.5 to +18.3) | 46.9 (39.3-53.5) |
| within trained length | Rollout disagreement (no real data) | -49.7 (-60.4 to -39.0) | 63.2 (54.9-70.1) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | -4.2 (-22.0 to +13.9) | 43.5 (35.9-50.9) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 46.7 (41.4-51.7) |
| beyond trained length | Visual predictor (no real data) | +21.3 (-9.4 to +54.3) | 69.3 (48.0-87.4) |
| beyond trained length | Rollout disagreement (no real data) | -45.4 (-55.2 to -35.5) | 57.4 (50.0-63.6) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +15.9 (-9.2 to +42.9) | 58.5 (41.2-73.9) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 30.7 (28.3-32.9) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 2.16 | 1.68-2.80 | 1.08 | 0.93-1.42 | 0.72 |
| within trained length | 2.23 | 1.69-3.09 | 1.07 | 0.94-1.69 | 0.77 |
| beyond trained length | 2.12 | 1.64-2.73 | 1.08 | 0.92-1.38 | 0.68 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 33.0 (31.3-34.7) | 23.3 (22.1-24.5) | 19.1 (18.1-20.0) | 16.5 (15.7-17.4) |
| 1 rollout, Smart + CV[visual] | 26.1 (24.7-27.3) | 18.4 (17.5-19.3) | 15.1 (14.3-15.7) | 13.0 (12.4-13.6) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 25.5 (23.9-26.7) | 18.0 (16.9-18.9) | 14.7 (13.8-15.4) | 12.7 (12.0-13.3) |
| 3 rollouts, Uniform + CV[visual+disagreement] | 25.1 (23.5-26.4) | 17.7 (16.6-18.6) | 14.5 (13.6-15.2) | 12.5 (11.7-13.2) |


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
- **Minecraft, all imagined frames, Rollout disagreement**: bias -32.5% (-44.8 to -18.5), CI excludes zero.
- **Minecraft, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +41.3% (+16.8 to +67.0), CI excludes zero.
- **Minecraft, within trained length, Rollout disagreement**: bias -28.1% (-42.2 to -14.3), CI excludes zero.
- **Minecraft, within trained length, Calibrated predictor (visual+disagreement)**: bias +55.2% (+17.0 to +96.2), CI excludes zero.
- **Minecraft, beyond trained length, Rollout disagreement**: bias -30.8% (-43.1 to -16.6), CI excludes zero.
- **Minecraft, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +47.5% (+24.6 to +71.9), CI excludes zero.
- **Minecraft at 2x speed, all imagined frames, Rollout disagreement**: bias -48.7% (-57.9 to -39.6), CI excludes zero.
- **Minecraft at 2x speed, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +5.2% (-16.0 to +28.5), CI includes zero.
- **Minecraft at 2x speed, within trained length, Rollout disagreement**: bias -49.7% (-60.4 to -39.0), CI excludes zero.
- **Minecraft at 2x speed, within trained length, Calibrated predictor (visual+disagreement)**: bias -4.2% (-22.0 to +13.9), CI includes zero.
- **Minecraft at 2x speed, beyond trained length, Rollout disagreement**: bias -45.4% (-55.2 to -35.5), CI excludes zero.
- **Minecraft at 2x speed, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +15.9% (-9.2 to +42.9), CI includes zero.
- **Unbiasedness**: the exact expectation of every audit equals the truth to numerical precision (max bias column), in every condition and horizon, including the negative control.
