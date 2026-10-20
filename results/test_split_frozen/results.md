## Minecraft, 72 test videos

72 clips from 72 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on Minecraft (10 separate videos, frozen). 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 35.0 | 33.4-36.6 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 32.6 | 30.2-35.0 | 0.87 | 0.77-0.98 | x1.15 | 2.1e-14 |
| Smart + CV[visual] | 31.6 | 29.4-33.8 | 0.81 | 0.73-0.91 | x1.23 | 3.1e-14 |
| Negative control: CV[shuffled proxies] | 35.1 | 33.5-36.7 | 1.01 | 1.01-1.01 | x0.99 | 2.1e-14 |
| Uniform + shrunk CV[visual] | 30.1 | 28.5-31.9 | 0.74 | 0.69-0.80 | x1.35 | 1.7e-14 |
| Uniform + CV[visual+disagreement] | 32.8 | 29.4-36.7 | 0.88 | 0.73-1.05 | x1.14 | 1.4e-14 |
| Uniform + shrunk CV[visual+disagreement] | 29.0 | 26.7-31.5 | 0.69 | 0.61-0.78 | x1.45 | 1.8e-14 |
| Smart + CV[visual+disagreement] | 32.0 | 29.1-34.9 | 0.84 | 0.71-0.97 | x1.20 | 2.8e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 33.5 | 30.2-37.1 | 0.92 | 0.77-1.09 | x1.09 | 2.8e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 31.8 | 29.1-34.7 | 0.83 | 0.71-0.96 | x1.21 | 4.7e-14 |
| Oracle Neyman (not deployable) | 14.1 | 13.0-15.1 | 0.16 | 0.14-0.18 | x6.16 | 2.9e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +73.2 (+47.5 to +100.8) | 150.3 (117.4-181.1) |
| all imagined frames | Rollout disagreement (no real data) | -13.7 (-24.5 to -2.8) | 56.8 (46.7-67.2) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +70.0 (+47.6 to +93.4) | 135.3 (108.6-160.2) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 32.0 (29.1-34.9) |
| within trained length | Visual predictor (no real data) | +87.1 (+57.7 to +118.8) | 165.3 (128.2-199.9) |
| within trained length | Rollout disagreement (no real data) | -9.2 (-20.4 to +2.7) | 58.4 (45.6-72.0) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +83.5 (+58.8 to +109.3) | 146.4 (118.8-172.5) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 75.8 (64.2-87.0) |
| beyond trained length | Visual predictor (no real data) | +81.6 (+53.9 to +111.0) | 166.9 (131.3-199.8) |
| beyond trained length | Rollout disagreement (no real data) | -11.0 (-22.8 to +1.0) | 63.5 (51.8-75.9) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +77.2 (+52.8 to +102.4) | 151.5 (120.9-180.7) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 36.4 (32.9-40.4) |

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
| 1 rollout, Uniform + shrunk CV[visual] | 30.1 (28.5-31.9) | 21.3 (20.1-22.6) | 17.4 (16.4-18.4) | 15.1 (14.2-16.0) |
| 2 rollouts, Smart + CV[visual+disagreement] | 31.8 (29.1-34.7) | 22.5 (20.6-24.5) | 18.4 (16.8-20.0) | 15.9 (14.6-17.3) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 29.0 (26.7-31.5) | 20.5 (18.9-22.3) | 16.7 (15.4-18.2) | 14.5 (13.4-15.8) |


## Minecraft at 2x speed, 40 test videos

16 clips from 16 videos x 3 rollouts; 18 imagined frames after 2 real context frames; 16 patches per frame, 1 inspected. Predictors fit on Minecraft (10 separate videos, frozen). 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 33.5 | 31.0-36.1 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 26.8 | 25.0-28.3 | 0.64 | 0.56-0.74 | x1.56 | 5.3e-15 |
| Smart + CV[visual] | 26.6 | 24.8-28.2 | 0.63 | 0.54-0.74 | x1.58 | 8.5e-15 |
| Negative control: CV[shuffled proxies] | 33.6 | 31.0-36.1 | 1.00 | 1.00-1.00 | x1.00 | 6.9e-15 |
| Uniform + shrunk CV[visual] | 27.7 | 25.9-29.3 | 0.68 | 0.61-0.77 | x1.46 | 4.9e-15 |
| Uniform + CV[visual+disagreement] | 25.6 | 23.4-27.6 | 0.58 | 0.48-0.70 | x1.72 | 7.3e-15 |
| Uniform + shrunk CV[visual+disagreement] | 26.5 | 24.4-28.5 | 0.63 | 0.54-0.73 | x1.59 | 5.5e-15 |
| Smart + CV[visual+disagreement] | 26.0 | 23.7-28.2 | 0.60 | 0.50-0.72 | x1.66 | 1.2e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 26.0 | 23.9-27.8 | 0.60 | 0.50-0.71 | x1.66 | 4.3e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 26.2 | 24.1-28.2 | 0.61 | 0.52-0.72 | x1.63 | 8.9e-15 |
| Oracle Neyman (not deployable) | 15.6 | 13.7-17.4 | 0.22 | 0.18-0.25 | x4.62 | 1.4e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | -0.8 (-23.0 to +22.6) | 47.2 (34.0-59.8) |
| all imagined frames | Rollout disagreement (no real data) | -52.3 (-63.5 to -41.2) | 57.7 (47.9-67.0) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | -3.4 (-22.4 to +15.7) | 40.2 (31.6-47.8) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 26.0 (23.7-28.2) |
| within trained length | Visual predictor (no real data) | +6.5 (-21.9 to +36.7) | 61.7 (43.3-77.9) |
| within trained length | Rollout disagreement (no real data) | -44.7 (-68.1 to -11.7) | 79.5 (58.6-104.8) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +7.4 (-23.2 to +40.0) | 70.5 (43.2-100.6) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 47.8 (41.2-54.0) |
| beyond trained length | Visual predictor (no real data) | +0.6 (-20.3 to +22.5) | 45.1 (33.6-56.8) |
| beyond trained length | Rollout disagreement (no real data) | -50.5 (-62.4 to -38.6) | 57.4 (47.6-66.9) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | -1.5 (-19.8 to +16.6) | 39.1 (30.9-46.3) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 30.8 (27.6-33.7) |

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
| 1 rollout, Smart + CV[visual] | 26.6 (24.8-28.2) | 18.8 (17.5-19.9) | 15.4 (14.3-16.3) | 13.3 (12.4-14.1) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 26.0 (23.9-27.8) | 18.4 (16.9-19.7) | 15.0 (13.8-16.1) | 13.0 (12.0-13.9) |
| 3 rollouts, Uniform + CV[visual+disagreement] | 25.6 (23.4-27.6) | 18.1 (16.5-19.5) | 14.8 (13.5-15.9) | 12.8 (11.7-13.8) |


## Findings

- **Uniform + CV[visual]**: variance x0.87 of uniform (95% CI 0.77-0.98), the accuracy of 1.15 uniform patches per frame. Reduction is statistically clear.
- **Smart + CV[visual]**: variance x0.81 of uniform (95% CI 0.73-0.91), the accuracy of 1.23 uniform patches per frame. Reduction is statistically clear.
- **Negative control: CV[shuffled proxies]**: variance x1.01 of uniform (95% CI 1.01-1.01), the accuracy of 0.99 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + shrunk CV[visual]**: variance x0.74 of uniform (95% CI 0.69-0.80), the accuracy of 1.35 uniform patches per frame. Reduction is statistically clear.
- **Uniform + CV[visual+disagreement]**: variance x0.88 of uniform (95% CI 0.73-1.05), the accuracy of 1.14 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + shrunk CV[visual+disagreement]**: variance x0.69 of uniform (95% CI 0.61-0.78), the accuracy of 1.45 uniform patches per frame. Reduction is statistically clear.
- **Smart + CV[visual+disagreement]**: variance x0.84 of uniform (95% CI 0.71-0.97), the accuracy of 1.20 uniform patches per frame. Reduction is statistically clear.
- **Uniform + CV[visual+disagreement], 2 rollouts**: variance x0.92 of uniform (95% CI 0.77-1.09), the accuracy of 1.09 uniform patches per frame. Not distinguishable from uniform.
- **Smart + CV[visual+disagreement], 2 rollouts**: variance x0.83 of uniform (95% CI 0.71-0.96), the accuracy of 1.21 uniform patches per frame. Reduction is statistically clear.
- **Rollouts versus patches** (best audit of each budget: Uniform + shrunk CV[visual+disagreement] for 3 rollouts, Uniform + shrunk CV[visual] for 1): with 3 rollouts and 1 patch per frame the audit is as accurate as a single-rollout audit with 1.08 patches per frame (95% CI 0.99-1.18). Variance of 3 rollouts + 1 patch relative to 1 rollout + 2 patches: 1.85 (1.70-2.02).
- **Minecraft, 72 test videos, all imagined frames, Rollout disagreement**: bias -13.7% (-24.5 to -2.8), CI excludes zero.
- **Minecraft, 72 test videos, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +70.0% (+47.6 to +93.4), CI excludes zero.
- **Minecraft, 72 test videos, within trained length, Rollout disagreement**: bias -9.2% (-20.4 to +2.7), CI includes zero.
- **Minecraft, 72 test videos, within trained length, Calibrated predictor (visual+disagreement)**: bias +83.5% (+58.8 to +109.3), CI excludes zero.
- **Minecraft, 72 test videos, beyond trained length, Rollout disagreement**: bias -11.0% (-22.8 to +1.0), CI includes zero.
- **Minecraft, 72 test videos, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +77.2% (+52.8 to +102.4), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, all imagined frames, Rollout disagreement**: bias -52.3% (-63.5 to -41.2), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, all imagined frames, Calibrated predictor (visual+disagreement)**: bias -3.4% (-22.4 to +15.7), CI includes zero.
- **Minecraft at 2x speed, 40 test videos, within trained length, Rollout disagreement**: bias -44.7% (-68.1 to -11.7), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, within trained length, Calibrated predictor (visual+disagreement)**: bias +7.4% (-23.2 to +40.0), CI includes zero.
- **Minecraft at 2x speed, 40 test videos, beyond trained length, Rollout disagreement**: bias -50.5% (-62.4 to -38.6), CI excludes zero.
- **Minecraft at 2x speed, 40 test videos, beyond trained length, Calibrated predictor (visual+disagreement)**: bias -1.5% (-19.8 to +16.6), CI includes zero.
- **Unbiasedness**: the exact expectation of every audit equals the truth to numerical precision (max bias column), in every condition and horizon, including the negative control.
