## Breakout

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Breakout', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 50.1 | 42.3-57.3 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 69.1 | 65.3-72.9 | 1.90 | 1.46-2.70 | x0.53 | 3.2e-14 |
| Smart + CV[visual] | 69.1 | 64.7-73.7 | 1.90 | 1.46-2.64 | x0.53 | 1.5e-13 |
| Negative control: CV[shuffled proxies] | 50.6 | 43.0-57.6 | 1.02 | 1.01-1.04 | x0.98 | 3.4e-14 |
| Uniform + shrunk CV[visual] | 49.9 | 42.2-57.2 | 0.99 | 0.98-1.00 | x1.01 | 6.8e-15 |
| Uniform + CV[visual+disagreement] | 84.2 | 65.5-107.0 | 2.82 | 1.57-4.85 | x0.35 | 4.6e-14 |
| Uniform + shrunk CV[visual+disagreement] | 50.8 | 43.0-58.0 | 1.03 | 1.00-1.09 | x0.98 | 1.1e-14 |
| Smart + CV[visual+disagreement] | 75.5 | 65.0-89.2 | 2.27 | 1.54-3.45 | x0.44 | 9.4e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 86.6 | 66.1-111.1 | 2.99 | 1.60-5.21 | x0.33 | 3.5e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 74.0 | 65.4-84.7 | 2.18 | 1.54-3.16 | x0.46 | 1.0e-13 |
| Oracle Neyman (not deployable) | 31.7 | 28.2-35.6 | 0.40 | 0.29-0.58 | x2.50 | 1.0e-13 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +432.2 (+291.2 to +570.3) | 604.0 (489.5-704.2) |
| all imagined frames | Rollout disagreement (no real data) | -80.6 (-99.3 to -53.2) | 113.1 (98.4-131.8) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +423.4 (+285.8 to +555.4) | 590.8 (480.7-685.4) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 75.5 (65.0-89.2) |
| within trained length | Visual predictor (no real data) | +349.6 (+260.8 to +435.6) | 434.9 (372.0-489.3) |
| within trained length | Rollout disagreement (no real data) | -88.4 (-99.6 to -67.8) | 108.6 (97.2-126.8) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +337.3 (+252.6 to +416.9) | 417.0 (359.5-466.3) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 151.7 (140.7-161.5) |
| beyond trained length | Visual predictor (no real data) | +521.8 (+347.7 to +691.8) | 733.8 (587.4-860.6) |
| beyond trained length | Rollout disagreement (no real data) | -76.2 (-99.5 to -39.1) | 130.0 (98.9-172.9) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +513.0 (+345.0 to +675.8) | 723.0 (579.8-847.8) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 80.7 (56.2-110.9) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 15.67 | 5.70-152.62 | 0.75 | 0.71-2.09 | 0.76 |
| within trained length | 12.89 | 3.44-841.29 | 0.73 | 0.70-39.95 | 0.73 |
| beyond trained length | 16.78 | 6.34-161.14 | 0.76 | 0.70-2.45 | 0.74 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 50.1 (42.3-57.3) | 35.4 (29.9-40.5) | 28.9 (24.4-33.1) | 25.1 (21.2-28.7) |
| 1 rollout, Uniform + shrunk CV[visual] | 49.9 (42.2-57.2) | 35.3 (29.8-40.4) | 28.8 (24.3-33.0) | 25.0 (21.1-28.6) |
| 2 rollouts, Smart + CV[visual+disagreement] | 74.0 (65.4-84.7) | 52.3 (46.3-59.9) | 42.7 (37.8-48.9) | 37.0 (32.7-42.3) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 50.8 (43.0-58.0) | 35.9 (30.4-41.0) | 29.3 (24.8-33.5) | 25.4 (21.5-29.0) |


## Breakout, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Breakout, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 51.6 | 43.3-59.2 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 71.4 | 67.0-75.5 | 1.91 | 1.46-2.72 | x0.52 | 2.3e-14 |
| Smart + CV[visual] | 71.2 | 66.7-75.8 | 1.90 | 1.44-2.73 | x0.53 | 9.5e-14 |
| Negative control: CV[shuffled proxies] | 51.9 | 43.9-59.5 | 1.01 | 1.00-1.03 | x0.99 | 3.3e-14 |
| Uniform + shrunk CV[visual] | 51.5 | 43.4-59.1 | 1.00 | 0.98-1.01 | x1.00 | 7.0e-15 |
| Uniform + CV[visual+disagreement] | 187.2 | 61.4-311.8 | 13.14 | 1.31-38.98 | x0.08 | 3.3e-14 |
| Uniform + shrunk CV[visual+disagreement] | 66.6 | 44.0-93.6 | 1.67 | 1.00-3.15 | x0.60 | 4.4e-15 |
| Smart + CV[visual+disagreement] | 95.8 | 61.7-139.8 | 3.44 | 1.30-7.65 | x0.29 | 9.9e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 177.3 | 62.7-293.4 | 11.79 | 1.36-34.47 | x0.08 | 3.0e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 97.1 | 63.2-141.2 | 3.54 | 1.36-7.79 | x0.28 | 1.1e-13 |
| Oracle Neyman (not deployable) | 32.9 | 28.4-37.9 | 0.41 | 0.28-0.59 | x2.47 | 7.2e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +416.4 (+280.3 to +550.8) | 583.2 (473.5-679.3) |
| all imagined frames | Rollout disagreement (no real data) | -83.8 (-97.0 to -58.9) | 130.7 (94.2-182.2) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +379.0 (+255.5 to +498.9) | 557.4 (430.1-677.3) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 95.8 (61.7-139.8) |
| within trained length | Visual predictor (no real data) | +334.5 (+247.4 to +418.0) | 419.2 (357.6-473.1) |
| within trained length | Rollout disagreement (no real data) | -92.8 (-97.8 to -84.6) | 96.7 (94.6-98.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +305.8 (+229.0 to +379.4) | 380.5 (327.2-426.2) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 149.1 (137.7-159.4) |
| beyond trained length | Visual predictor (no real data) | +504.2 (+338.7 to +669.3) | 709.5 (569.6-831.2) |
| beyond trained length | Rollout disagreement (no real data) | -77.6 (-97.2 to -39.5) | 181.1 (94.6-283.1) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +459.7 (+307.6 to +609.8) | 705.5 (514.2-904.6) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 128.8 (49.0-210.5) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 9.71 | 5.55-20.35 | 1.25 | 0.75-3.10 | 0.79 |
| within trained length | 10.78 | 7.25-24.59 | 0.94 | 0.71-2.14 | 0.77 |
| beyond trained length | 9.43 | 4.93-23.13 | 1.28 | 0.75-3.70 | 0.76 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 51.6 (43.3-59.2) | 36.5 (30.6-41.9) | 29.8 (25.0-34.2) | 25.8 (21.7-29.6) |
| 1 rollout, Uniform + shrunk CV[visual] | 51.5 (43.4-59.1) | 36.4 (30.7-41.8) | 29.7 (25.0-34.1) | 25.8 (21.7-29.5) |
| 2 rollouts, Smart + CV[visual+disagreement] | 97.1 (63.2-141.2) | 68.7 (44.7-99.8) | 56.1 (36.5-81.5) | 48.6 (31.6-70.6) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 66.6 (44.0-93.6) | 47.1 (31.1-66.2) | 38.5 (25.4-54.0) | 33.3 (22.0-46.8) |


## Pong

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Pong', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 28.7 | 18.6-37.5 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 33.5 | 26.6-40.5 | 1.37 | 1.16-2.06 | x0.73 | 7.0e-15 |
| Smart + CV[visual] | 22.3 | 16.4-28.0 | 0.60 | 0.52-0.81 | x1.66 | 1.7e-14 |
| Negative control: CV[shuffled proxies] | 28.7 | 18.7-37.6 | 1.00 | 1.00-1.00 | x1.00 | 7.6e-15 |
| Uniform + shrunk CV[visual] | 28.7 | 18.6-37.5 | 1.00 | 1.00-1.00 | x1.00 | 1.8e-15 |
| Uniform + CV[visual+disagreement] | 33.6 | 26.6-40.5 | 1.37 | 1.16-2.07 | x0.73 | 7.2e-15 |
| Uniform + shrunk CV[visual+disagreement] | 28.8 | 19.0-37.6 | 1.01 | 1.00-1.04 | x0.99 | 3.8e-15 |
| Smart + CV[visual+disagreement] | 22.3 | 16.5-28.1 | 0.61 | 0.52-0.81 | x1.65 | 1.8e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 33.5 | 26.7-40.5 | 1.37 | 1.16-2.06 | x0.73 | 1.4e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 22.4 | 16.5-28.1 | 0.61 | 0.53-0.82 | x1.64 | 1.9e-14 |
| Oracle Neyman (not deployable) | 9.2 | 7.9-10.4 | 0.10 | 0.07-0.19 | x9.81 | 1.6e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +60.2 (+44.4 to +73.6) | 74.6 (67.9-80.3) |
| all imagined frames | Rollout disagreement (no real data) | -99.5 (-99.8 to -98.9) | 99.5 (99.0-99.8) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +58.8 (+43.1 to +72.1) | 73.2 (66.6-78.8) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 22.3 (16.5-28.1) |
| within trained length | Visual predictor (no real data) | +48.6 (+34.4 to +60.0) | 62.0 (56.7-67.0) |
| within trained length | Rollout disagreement (no real data) | -99.5 (-99.8 to -99.0) | 99.5 (99.0-99.8) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +46.3 (+32.4 to +57.6) | 59.7 (54.5-64.6) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 24.7 (20.4-28.9) |
| beyond trained length | Visual predictor (no real data) | +75.4 (+56.3 to +91.3) | 91.4 (83.0-98.2) |
| beyond trained length | Rollout disagreement (no real data) | -99.5 (-99.8 to -98.8) | 99.5 (98.9-99.8) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +74.6 (+55.7 to +90.5) | 90.7 (82.5-97.3) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 30.5 (20.8-39.6) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 144.22 | 90.69-651.37 | 2.36 | 0.93-89.62 | -0.28 |
| within trained length | 103.98 | 62.92-646.15 | 1.33 | 0.97-101.73 | -0.38 |
| beyond trained length | 204.36 | 97.39-684.30 | 17.19 | 0.90-92.98 | -0.15 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 28.7 (18.6-37.5) | 20.3 (13.2-26.6) | 16.6 (10.8-21.7) | 14.3 (9.3-18.8) |
| 1 rollout, Smart + CV[visual] | 22.3 (16.4-28.0) | 15.8 (11.6-19.8) | 12.9 (9.5-16.2) | 11.1 (8.2-14.0) |
| 2 rollouts, Smart + CV[visual+disagreement] | 22.4 (16.5-28.1) | 15.8 (11.7-19.9) | 12.9 (9.5-16.2) | 11.2 (8.3-14.0) |
| 3 rollouts, Smart + CV[visual+disagreement] | 22.3 (16.5-28.1) | 15.8 (11.6-19.8) | 12.9 (9.5-16.2) | 11.2 (8.2-14.0) |


## Pong, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Pong, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 29.3 | 20.1-37.7 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 34.0 | 27.6-40.4 | 1.34 | 1.15-1.90 | x0.75 | 1.0e-14 |
| Smart + CV[visual] | 22.6 | 17.2-27.9 | 0.59 | 0.52-0.76 | x1.69 | 1.9e-14 |
| Negative control: CV[shuffled proxies] | 29.4 | 20.1-37.7 | 1.00 | 1.00-1.00 | x1.00 | 7.1e-15 |
| Uniform + shrunk CV[visual] | 29.3 | 20.1-37.7 | 1.00 | 1.00-1.00 | x1.00 | 3.2e-15 |
| Uniform + CV[visual+disagreement] | 28.8 | 20.3-36.5 | 0.97 | 0.82-1.17 | x1.04 | 5.2e-15 |
| Uniform + shrunk CV[visual+disagreement] | 27.1 | 18.4-34.8 | 0.85 | 0.72-0.97 | x1.17 | 3.1e-15 |
| Smart + CV[visual+disagreement] | 24.4 | 15.7-32.0 | 0.69 | 0.44-0.92 | x1.45 | 1.3e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 30.4 | 22.1-38.0 | 1.08 | 0.94-1.37 | x0.93 | 6.6e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 21.6 | 15.1-27.4 | 0.54 | 0.45-0.65 | x1.85 | 1.5e-14 |
| Oracle Neyman (not deployable) | 6.2 | 4.5-8.0 | 0.05 | 0.04-0.06 | x22.21 | 1.2e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +59.5 (+43.7 to +73.0) | 74.4 (67.8-80.2) |
| all imagined frames | Rollout disagreement (no real data) | -93.1 (-97.7 to -87.4) | 94.5 (90.1-97.9) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +26.2 (+15.8 to +34.9) | 39.1 (35.7-42.4) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 24.4 (15.7-32.0) |
| within trained length | Visual predictor (no real data) | +50.9 (+36.4 to +62.5) | 64.4 (58.9-69.4) |
| within trained length | Rollout disagreement (no real data) | -95.5 (-98.8 to -90.4) | 96.5 (93.1-98.8) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +21.3 (+12.1 to +28.7) | 32.9 (28.8-37.9) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 25.6 (15.5-34.0) |
| beyond trained length | Visual predictor (no real data) | +72.8 (+54.4 to +88.8) | 89.7 (81.7-96.2) |
| beyond trained length | Rollout disagreement (no real data) | -92.2 (-98.4 to -84.8) | 94.5 (89.3-98.5) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +33.7 (+21.8 to +43.6) | 47.5 (43.6-51.8) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 33.1 (20.2-44.6) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 3.94 | 2.34-44.01 | 0.97 | 0.68-0.99 | -0.15 |
| within trained length | 4.33 | 2.32-87.90 | 0.92 | 0.80-1.51 | -0.38 |
| beyond trained length | 3.69 | 2.34-58.47 | 1.01 | 0.67-1.03 | 0.23 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 29.3 (20.1-37.7) | 20.7 (14.2-26.7) | 16.9 (11.6-21.8) | 14.7 (10.0-18.8) |
| 1 rollout, Smart + CV[visual] | 22.6 (17.2-27.9) | 16.0 (12.1-19.7) | 13.0 (9.9-16.1) | 11.3 (8.6-13.9) |
| 2 rollouts, Smart + CV[visual+disagreement] | 21.6 (15.1-27.4) | 15.3 (10.7-19.4) | 12.5 (8.7-15.8) | 10.8 (7.5-13.7) |
| 3 rollouts, Smart + CV[visual+disagreement] | 24.4 (15.7-32.0) | 17.2 (11.1-22.6) | 14.1 (9.1-18.5) | 12.2 (7.8-16.0) |


## Boxing

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Boxing', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 45.3 | 43.7-47.0 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 35.7 | 33.7-37.5 | 0.62 | 0.58-0.66 | x1.62 | 6.6e-15 |
| Smart + CV[visual] | 29.0 | 27.8-30.2 | 0.41 | 0.38-0.44 | x2.44 | 1.1e-14 |
| Negative control: CV[shuffled proxies] | 45.3 | 43.7-47.0 | 1.00 | 1.00-1.00 | x1.00 | 4.9e-15 |
| Uniform + shrunk CV[visual] | 35.4 | 33.8-37.0 | 0.61 | 0.59-0.63 | x1.64 | 3.7e-15 |
| Uniform + CV[visual+disagreement] | 29.8 | 28.3-31.4 | 0.43 | 0.39-0.47 | x2.31 | 8.4e-15 |
| Uniform + shrunk CV[visual+disagreement] | 29.8 | 28.3-31.4 | 0.43 | 0.39-0.47 | x2.31 | 8.4e-15 |
| Smart + CV[visual+disagreement] | 22.0 | 20.6-23.5 | 0.24 | 0.20-0.27 | x4.23 | 1.0e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 30.9 | 29.4-32.4 | 0.47 | 0.43-0.50 | x2.15 | 6.2e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 23.5 | 22.2-24.7 | 0.27 | 0.24-0.30 | x3.73 | 1.2e-14 |
| Oracle Neyman (not deployable) | 13.2 | 12.4-14.0 | 0.08 | 0.07-0.09 | x11.80 | 1.2e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +10.8 (-2.0 to +24.1) | 41.8 (33.2-49.9) |
| all imagined frames | Rollout disagreement (no real data) | -40.3 (-49.9 to -30.9) | 50.8 (41.8-59.2) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +9.0 (-2.8 to +21.5) | 39.8 (32.4-47.9) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 22.0 (20.6-23.5) |
| within trained length | Visual predictor (no real data) | +36.8 (+4.9 to +74.7) | 112.5 (62.9-161.7) |
| within trained length | Rollout disagreement (no real data) | -55.5 (-67.1 to -43.5) | 69.7 (61.2-77.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +28.2 (+3.5 to +55.9) | 89.4 (56.8-118.5) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 38.8 (34.0-43.9) |
| beyond trained length | Visual predictor (no real data) | +10.2 (-0.6 to +21.5) | 38.2 (31.9-44.1) |
| beyond trained length | Rollout disagreement (no real data) | -30.2 (-40.6 to -19.8) | 46.4 (37.2-54.8) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +9.2 (-2.1 to +20.6) | 39.9 (33.5-46.1) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 28.5 (26.5-30.4) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 1.78 | 1.54-2.13 | 1.09 | 1.02-1.18 | 0.77 |
| within trained length | 2.60 | 2.05-3.50 | 1.25 | 1.10-1.45 | 0.73 |
| beyond trained length | 1.52 | 1.32-1.78 | 1.06 | 0.99-1.14 | 0.80 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 45.3 (43.7-47.0) | 32.1 (30.9-33.3) | 26.2 (25.2-27.2) | 22.7 (21.8-23.5) |
| 1 rollout, Smart + CV[visual] | 29.0 (27.8-30.2) | 20.5 (19.6-21.4) | 16.8 (16.0-17.4) | 14.5 (13.9-15.1) |
| 2 rollouts, Smart + CV[visual+disagreement] | 23.5 (22.2-24.7) | 16.6 (15.7-17.5) | 13.5 (12.8-14.3) | 11.7 (11.1-12.4) |
| 3 rollouts, Smart + CV[visual+disagreement] | 22.0 (20.6-23.5) | 15.6 (14.6-16.6) | 12.7 (11.9-13.6) | 11.0 (10.3-11.8) |


## Boxing, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Boxing, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 44.1 | 42.7-45.6 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 35.2 | 33.0-37.6 | 0.63 | 0.58-0.70 | x1.58 | 6.3e-15 |
| Smart + CV[visual] | 28.6 | 27.2-30.1 | 0.42 | 0.39-0.45 | x2.39 | 1.2e-14 |
| Negative control: CV[shuffled proxies] | 44.2 | 42.7-45.6 | 1.00 | 1.00-1.00 | x1.00 | 1.1e-14 |
| Uniform + shrunk CV[visual] | 34.7 | 33.0-36.5 | 0.62 | 0.59-0.65 | x1.62 | 4.7e-15 |
| Uniform + CV[visual+disagreement] | 28.9 | 27.2-30.8 | 0.43 | 0.39-0.47 | x2.33 | 7.4e-15 |
| Uniform + shrunk CV[visual+disagreement] | 28.9 | 27.2-30.8 | 0.43 | 0.39-0.47 | x2.33 | 7.4e-15 |
| Smart + CV[visual+disagreement] | 22.2 | 20.6-23.8 | 0.25 | 0.22-0.29 | x3.95 | 1.5e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 30.3 | 28.7-32.0 | 0.47 | 0.43-0.51 | x2.12 | 6.5e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 23.4 | 21.9-24.9 | 0.28 | 0.25-0.31 | x3.57 | 1.3e-14 |
| Oracle Neyman (not deployable) | 13.2 | 12.4-14.1 | 0.09 | 0.08-0.10 | x11.11 | 1.2e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +12.0 (-1.0 to +25.9) | 46.3 (35.9-56.8) |
| all imagined frames | Rollout disagreement (no real data) | -22.5 (-30.8 to -13.9) | 35.1 (28.1-41.4) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +9.7 (-1.5 to +21.1) | 38.2 (32.6-43.7) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 22.2 (20.6-23.8) |
| within trained length | Visual predictor (no real data) | +19.5 (-0.8 to +41.8) | 71.3 (47.7-92.1) |
| within trained length | Rollout disagreement (no real data) | -29.7 (-40.5 to -18.2) | 47.5 (40.0-54.6) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +13.8 (-1.3 to +30.0) | 54.5 (39.0-68.0) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 32.2 (29.6-34.6) |
| beyond trained length | Visual predictor (no real data) | +13.6 (+1.7 to +26.7) | 45.9 (37.7-53.8) |
| beyond trained length | Rollout disagreement (no real data) | -15.7 (-25.6 to -5.5) | 37.4 (30.4-44.0) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +12.1 (+0.6 to +24.2) | 43.2 (37.2-49.4) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 30.2 (27.7-32.6) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 1.38 | 1.23-1.56 | 0.99 | 0.91-1.09 | 0.80 |
| within trained length | 1.56 | 1.33-1.88 | 1.04 | 0.94-1.16 | 0.77 |
| beyond trained length | 1.29 | 1.14-1.47 | 0.97 | 0.90-1.08 | 0.80 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 44.1 (42.7-45.6) | 31.2 (30.2-32.3) | 25.5 (24.6-26.3) | 22.1 (21.3-22.8) |
| 1 rollout, Smart + CV[visual] | 28.6 (27.2-30.1) | 20.2 (19.2-21.3) | 16.5 (15.7-17.4) | 14.3 (13.6-15.0) |
| 2 rollouts, Smart + CV[visual+disagreement] | 23.4 (21.9-24.9) | 16.5 (15.5-17.6) | 13.5 (12.6-14.4) | 11.7 (10.9-12.4) |
| 3 rollouts, Smart + CV[visual+disagreement] | 22.2 (20.6-23.8) | 15.7 (14.5-16.8) | 12.8 (11.9-13.8) | 11.1 (10.3-11.9) |


## MsPacman

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'MsPacman', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 50.2 | 42.6-58.9 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 239.5 | 54.4-379.6 | 22.81 | 1.19-64.74 | x0.04 | 2.0e-13 |
| Smart + CV[visual] | 141.5 | 46.5-215.9 | 7.96 | 0.89-21.43 | x0.13 | 3.9e-13 |
| Negative control: CV[shuffled proxies] | 50.9 | 43.6-59.4 | 1.03 | 1.00-1.09 | x0.97 | 2.8e-13 |
| Uniform + shrunk CV[visual] | 50.2 | 42.6-58.9 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual+disagreement] | 187.6 | 49.7-294.6 | 13.99 | 1.02-39.23 | x0.07 | 9.8e-14 |
| Uniform + shrunk CV[visual+disagreement] | 50.2 | 42.6-58.9 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Smart + CV[visual+disagreement] | 114.4 | 43.5-172.5 | 5.20 | 0.80-13.63 | x0.19 | 5.3e-13 |
| Uniform + CV[visual+disagreement], 2 rollouts | 198.1 | 50.6-311.8 | 15.60 | 1.05-43.86 | x0.06 | 8.1e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 119.9 | 44.1-181.4 | 5.71 | 0.82-15.07 | x0.18 | 5.4e-13 |
| Oracle Neyman (not deployable) | 49.9 | 26.6-70.6 | 0.99 | 0.30-2.26 | x1.01 | 3.6e-13 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +532.8 (+68.1 to +1187.8) | 1763.6 (188.5-2791.1) |
| all imagined frames | Rollout disagreement (no real data) | -87.6 (-92.7 to -82.1) | 89.1 (84.3-93.5) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +462.2 (+58.7 to +1037.6) | 1534.0 (161.6-2439.5) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 114.4 (43.5-172.5) |
| within trained length | Visual predictor (no real data) | +697.8 (+237.2 to +1281.6) | 1647.7 (692.2-2391.3) |
| within trained length | Rollout disagreement (no real data) | -92.6 (-97.1 to -87.1) | 94.1 (90.3-97.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +671.9 (+226.8 to +1233.8) | 1584.7 (699.3-2281.6) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 259.4 (130.4-365.3) |
| beyond trained length | Visual predictor (no real data) | +591.9 (+55.7 to +1378.1) | 2050.1 (181.1-3296.3) |
| beyond trained length | Rollout disagreement (no real data) | -85.1 (-91.3 to -78.3) | 87.2 (81.6-92.3) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +495.4 (+46.0 to +1159.4) | 1721.9 (150.2-2775.4) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 125.1 (49.4-190.0) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 7.19 | 4.70-13.45 | 1.23 | 1.03-1.78 | 0.65 |
| within trained length | 14.64 | 6.69-55.09 | 1.17 | 0.99-4.45 | 0.65 |
| beyond trained length | 5.77 | 3.94-10.18 | 1.24 | 1.03-1.73 | 0.60 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 50.2 (42.6-58.9) | 35.5 (30.1-41.7) | 29.0 (24.6-34.0) | 25.1 (21.3-29.5) |
| 1 rollout, Uniform + shrunk CV[visual] | 50.2 (42.6-58.9) | 35.5 (30.1-41.7) | 29.0 (24.6-34.0) | 25.1 (21.3-29.5) |
| 2 rollouts, Smart + CV[visual+disagreement] | 119.9 (44.1-181.4) | 84.8 (31.2-128.3) | 69.2 (25.4-104.8) | 59.9 (22.0-90.7) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 50.2 (42.6-58.9) | 35.5 (30.1-41.7) | 29.0 (24.6-34.0) | 25.1 (21.3-29.5) |


## MsPacman, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'MsPacman, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 50.8 | 43.1-59.6 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 247.1 | 54.0-391.4 | 23.66 | 1.17-67.83 | x0.04 | 2.2e-13 |
| Smart + CV[visual] | 145.2 | 46.1-221.4 | 8.17 | 0.85-22.12 | x0.12 | 3.3e-13 |
| Negative control: CV[shuffled proxies] | 51.3 | 43.8-60.0 | 1.02 | 1.00-1.06 | x0.98 | 1.4e-13 |
| Uniform + shrunk CV[visual] | 50.8 | 43.1-59.6 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual+disagreement] | 153.5 | 49.7-237.5 | 9.13 | 0.99-25.03 | x0.11 | 9.0e-14 |
| Uniform + shrunk CV[visual+disagreement] | 50.8 | 43.1-59.6 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Smart + CV[visual+disagreement] | 91.3 | 42.0-133.4 | 3.23 | 0.72-7.95 | x0.31 | 3.2e-13 |
| Uniform + CV[visual+disagreement], 2 rollouts | 173.5 | 50.6-270.5 | 11.66 | 1.02-32.51 | x0.09 | 2.0e-13 |
| Smart + CV[visual+disagreement], 2 rollouts | 103.7 | 43.0-154.1 | 4.16 | 0.76-10.59 | x0.24 | 3.1e-13 |
| Oracle Neyman (not deployable) | 40.7 | 22.7-56.8 | 0.64 | 0.21-1.44 | x1.56 | 2.8e-13 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +515.6 (+61.0 to +1169.1) | 1745.4 (172.1-2768.9) |
| all imagined frames | Rollout disagreement (no real data) | -58.7 (-72.4 to -43.2) | 75.8 (68.0-82.6) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +375.3 (+48.0 to +845.6) | 1248.4 (143.7-1990.2) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 91.3 (42.0-133.4) |
| within trained length | Visual predictor (no real data) | +669.2 (+227.9 to +1228.9) | 1581.3 (670.2-2290.7) |
| within trained length | Rollout disagreement (no real data) | -70.1 (-79.5 to -59.7) | 77.6 (70.4-84.0) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +543.3 (+184.4 to +991.6) | 1273.5 (577.7-1824.6) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 196.9 (106.5-273.0) |
| beyond trained length | Visual predictor (no real data) | +585.7 (+53.6 to +1377.1) | 2065.0 (167.5-3327.5) |
| beyond trained length | Rollout disagreement (no real data) | -52.9 (-69.9 to -33.6) | 84.3 (69.9-100.8) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +411.4 (+43.2 to +952.1) | 1420.5 (149.3-2291.2) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 103.1 (49.1-151.7) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 3.00 | 2.22-4.32 | 1.09 | 0.93-1.27 | 0.77 |
| within trained length | 3.80 | 2.55-6.53 | 1.13 | 0.88-1.46 | 0.79 |
| beyond trained length | 2.73 | 2.05-3.85 | 1.07 | 0.92-1.25 | 0.72 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 50.8 (43.1-59.6) | 35.9 (30.5-42.2) | 29.3 (24.9-34.4) | 25.4 (21.5-29.8) |
| 1 rollout, Uniform + shrunk CV[visual] | 50.8 (43.1-59.6) | 35.9 (30.5-42.2) | 29.3 (24.9-34.4) | 25.4 (21.5-29.8) |
| 2 rollouts, Smart + CV[visual+disagreement] | 103.7 (43.0-154.1) | 73.3 (30.4-108.9) | 59.9 (24.8-88.9) | 51.8 (21.5-77.0) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 50.8 (43.1-59.6) | 35.9 (30.5-42.2) | 29.3 (24.9-34.4) | 25.4 (21.5-29.8) |


## Seaquest

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Seaquest', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 49.8 | 43.1-57.0 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 51.7 | 45.7-58.3 | 1.08 | 1.01-1.19 | x0.93 | 1.6e-14 |
| Smart + CV[visual] | 58.5 | 50.3-67.6 | 1.38 | 1.10-1.84 | x0.73 | 2.7e-14 |
| Negative control: CV[shuffled proxies] | 49.9 | 43.2-57.0 | 1.00 | 1.00-1.00 | x1.00 | 2.6e-14 |
| Uniform + shrunk CV[visual] | 50.0 | 43.3-57.0 | 1.00 | 1.00-1.01 | x1.00 | 5.1e-15 |
| Uniform + CV[visual+disagreement] | 51.9 | 45.0-60.1 | 1.09 | 0.99-1.20 | x0.92 | 1.6e-14 |
| Uniform + shrunk CV[visual+disagreement] | 49.7 | 43.3-56.3 | 0.99 | 0.97-1.03 | x1.01 | 8.2e-15 |
| Smart + CV[visual+disagreement] | 57.9 | 50.2-66.5 | 1.35 | 1.03-1.86 | x0.74 | 3.2e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 51.7 | 45.1-59.3 | 1.08 | 1.00-1.18 | x0.93 | 2.0e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 58.2 | 50.3-66.9 | 1.36 | 1.06-1.84 | x0.73 | 3.0e-14 |
| Oracle Neyman (not deployable) | 25.5 | 23.4-27.4 | 0.26 | 0.19-0.36 | x3.83 | 5.4e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +58.6 (+16.4 to +110.8) | 148.3 (62.1-216.9) |
| all imagined frames | Rollout disagreement (no real data) | -95.5 (-98.2 to -91.8) | 96.2 (93.3-98.3) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +55.4 (+16.1 to +104.7) | 140.2 (58.9-205.2) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 57.9 (50.2-66.5) |
| within trained length | Visual predictor (no real data) | +88.3 (+34.5 to +149.2) | 187.3 (109.8-254.5) |
| within trained length | Rollout disagreement (no real data) | -98.3 (-99.4 to -96.8) | 98.4 (97.0-99.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +86.6 (+33.5 to +146.8) | 184.5 (109.2-250.3) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 111.9 (98.7-126.5) |
| beyond trained length | Visual predictor (no real data) | +70.1 (+26.1 to +124.6) | 156.8 (73.6-226.6) |
| beyond trained length | Rollout disagreement (no real data) | -94.5 (-97.8 to -90.1) | 95.4 (92.1-97.9) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +65.2 (+25.0 to +115.7) | 145.6 (68.6-209.9) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 55.7 (49.9-62.6) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 18.76 | 10.61-54.54 | 0.93 | 0.73-3.38 | 0.53 |
| within trained length | 68.66 | 37.15-184.16 | 6.32 | 1.52-7.07 | 0.43 |
| beyond trained length | 14.64 | 8.23-45.46 | 0.90 | 0.73-3.42 | 0.56 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 49.8 (43.1-57.0) | 35.2 (30.5-40.3) | 28.8 (24.9-32.9) | 24.9 (21.6-28.5) |
| 1 rollout, Uniform + shrunk CV[visual] | 50.0 (43.3-57.0) | 35.3 (30.6-40.3) | 28.8 (25.0-32.9) | 25.0 (21.7-28.5) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 51.7 (45.1-59.3) | 36.6 (31.9-41.9) | 29.9 (26.1-34.2) | 25.9 (22.6-29.6) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 49.7 (43.3-56.3) | 35.1 (30.6-39.8) | 28.7 (25.0-32.5) | 24.9 (21.6-28.2) |


## Seaquest, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Seaquest, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 49.0 | 43.2-55.4 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 51.1 | 46.1-56.9 | 1.09 | 1.01-1.21 | x0.92 | 1.6e-14 |
| Smart + CV[visual] | 59.3 | 50.4-69.1 | 1.47 | 1.11-2.00 | x0.68 | 4.1e-14 |
| Negative control: CV[shuffled proxies] | 49.0 | 43.2-55.4 | 1.00 | 1.00-1.00 | x1.00 | 1.4e-14 |
| Uniform + shrunk CV[visual] | 49.0 | 43.2-55.3 | 1.00 | 0.99-1.01 | x1.00 | 6.2e-15 |
| Uniform + CV[visual+disagreement] | 47.4 | 41.4-53.7 | 0.94 | 0.80-1.10 | x1.07 | 8.8e-15 |
| Uniform + shrunk CV[visual+disagreement] | 46.1 | 40.5-52.2 | 0.88 | 0.80-0.97 | x1.13 | 6.7e-15 |
| Smart + CV[visual+disagreement] | 78.2 | 63.0-96.3 | 2.55 | 1.60-3.88 | x0.39 | 1.8e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 48.1 | 42.8-54.1 | 0.96 | 0.86-1.09 | x1.04 | 1.2e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 60.6 | 52.0-69.9 | 1.53 | 1.13-2.10 | x0.65 | 2.6e-14 |
| Oracle Neyman (not deployable) | 21.2 | 19.6-22.7 | 0.19 | 0.14-0.25 | x5.34 | 3.5e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +62.4 (+19.4 to +115.8) | 153.3 (67.7-222.5) |
| all imagined frames | Rollout disagreement (no real data) | -66.6 (-76.2 to -56.6) | 74.7 (67.2-81.4) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +46.6 (+16.1 to +83.1) | 111.9 (61.5-156.2) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 78.2 (63.0-96.3) |
| within trained length | Visual predictor (no real data) | +79.6 (+31.8 to +131.8) | 171.2 (105.0-230.9) |
| within trained length | Rollout disagreement (no real data) | -67.2 (-80.9 to -48.3) | 98.1 (75.2-128.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +62.6 (+25.9 to +103.1) | 149.5 (91.9-200.2) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 156.5 (135.2-177.5) |
| beyond trained length | Visual predictor (no real data) | +76.3 (+30.7 to +132.7) | 166.2 (84.7-234.8) |
| beyond trained length | Rollout disagreement (no real data) | -64.4 (-74.3 to -54.1) | 72.3 (64.0-79.7) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +57.1 (+25.3 to +95.9) | 119.7 (71.4-163.1) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 76.5 (57.6-99.1) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 3.11 | 2.44-4.16 | 0.93 | 0.78-1.23 | 0.57 |
| within trained length | 3.41 | 2.60-4.81 | 1.09 | 0.81-1.39 | 0.49 |
| beyond trained length | 3.02 | 2.29-4.16 | 0.91 | 0.77-1.27 | 0.57 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 49.0 (43.2-55.4) | 34.7 (30.5-39.1) | 28.3 (24.9-32.0) | 24.5 (21.6-27.7) |
| 1 rollout, Uniform + shrunk CV[visual] | 49.0 (43.2-55.3) | 34.6 (30.6-39.1) | 28.3 (24.9-31.9) | 24.5 (21.6-27.7) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 48.1 (42.8-54.1) | 34.0 (30.2-38.2) | 27.8 (24.7-31.2) | 24.1 (21.4-27.0) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 46.1 (40.5-52.2) | 32.6 (28.6-36.9) | 26.6 (23.4-30.1) | 23.0 (20.2-26.1) |


## Freeway

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Freeway', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 38.0 | 29.6-45.4 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 44.5 | 39.5-49.3 | 1.37 | 1.15-1.85 | x0.73 | 8.0e-15 |
| Smart + CV[visual] | 39.4 | 31.8-47.1 | 1.08 | 0.81-1.48 | x0.93 | 2.3e-14 |
| Negative control: CV[shuffled proxies] | 38.0 | 29.6-45.5 | 1.00 | 1.00-1.00 | x1.00 | 9.9e-15 |
| Uniform + shrunk CV[visual] | 37.9 | 29.8-45.1 | 0.99 | 0.98-1.01 | x1.01 | 4.3e-15 |
| Uniform + CV[visual+disagreement] | 55.0 | 39.9-73.7 | 2.09 | 1.18-4.09 | x0.48 | 1.6e-14 |
| Uniform + shrunk CV[visual+disagreement] | 37.8 | 29.7-45.1 | 0.99 | 0.98-1.01 | x1.01 | 4.5e-15 |
| Smart + CV[visual+disagreement] | 38.4 | 30.9-46.0 | 1.02 | 0.76-1.41 | x0.98 | 3.2e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 51.5 | 40.1-65.3 | 1.83 | 1.18-3.18 | x0.55 | 8.6e-15 |
| Smart + CV[visual+disagreement], 2 rollouts | 38.5 | 31.0-46.1 | 1.03 | 0.77-1.41 | x0.97 | 1.9e-14 |
| Oracle Neyman (not deployable) | 16.0 | 14.8-17.3 | 0.18 | 0.13-0.28 | x5.64 | 2.3e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +58.3 (+30.3 to +85.0) | 99.0 (84.6-111.7) |
| all imagined frames | Rollout disagreement (no real data) | -98.7 (-99.0 to -98.3) | 98.7 (98.3-99.0) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +59.5 (+32.3 to +85.0) | 97.0 (82.9-109.6) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 38.4 (30.9-46.0) |
| within trained length | Visual predictor (no real data) | +55.5 (+30.7 to +78.8) | 88.8 (77.8-99.1) |
| within trained length | Rollout disagreement (no real data) | -98.7 (-98.9 to -98.5) | 98.7 (98.5-98.9) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +56.0 (+31.2 to +79.4) | 89.3 (78.2-99.7) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 76.0 (56.4-97.4) |
| beyond trained length | Visual predictor (no real data) | +65.5 (+35.3 to +94.5) | 109.1 (92.1-124.0) |
| beyond trained length | Rollout disagreement (no real data) | -98.7 (-99.1 to -98.2) | 98.7 (98.2-99.1) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +66.2 (+36.9 to +93.7) | 105.9 (89.4-120.3) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 40.1 (32.2-47.5) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 89.87 | 54.05-154.77 | 2.76 | 2.47-137.75 | 0.35 |
| within trained length | 117.25 | 82.80-159.87 | 100.82 | 63.55-150.70 | 0.19 |
| beyond trained length | 80.74 | 44.44-171.88 | 2.73 | 2.46-156.27 | 0.42 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 38.0 (29.6-45.4) | 26.9 (20.9-32.1) | 21.9 (17.1-26.2) | 19.0 (14.8-22.7) |
| 1 rollout, Uniform + shrunk CV[visual] | 37.9 (29.8-45.1) | 26.8 (21.0-31.9) | 21.9 (17.2-26.1) | 18.9 (14.9-22.6) |
| 2 rollouts, Smart + CV[visual+disagreement] | 38.5 (31.0-46.1) | 27.2 (21.9-32.6) | 22.2 (17.9-26.6) | 19.3 (15.5-23.1) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 37.8 (29.7-45.1) | 26.7 (21.0-31.9) | 21.8 (17.1-26.0) | 18.9 (14.8-22.5) |


## Freeway, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Freeway, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 39.4 | 30.9-46.8 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 46.6 | 42.0-51.2 | 1.40 | 1.17-1.89 | x0.71 | 9.5e-15 |
| Smart + CV[visual] | 41.1 | 33.9-48.2 | 1.09 | 0.83-1.46 | x0.92 | 2.0e-14 |
| Negative control: CV[shuffled proxies] | 39.4 | 30.9-46.8 | 1.00 | 1.00-1.00 | x1.00 | 9.1e-15 |
| Uniform + shrunk CV[visual] | 39.3 | 31.1-46.5 | 1.00 | 0.98-1.02 | x1.00 | 4.4e-15 |
| Uniform + CV[visual+disagreement] | 50.0 | 38.0-64.3 | 1.61 | 1.04-2.89 | x0.62 | 8.8e-15 |
| Uniform + shrunk CV[visual+disagreement] | 38.8 | 30.5-46.0 | 0.97 | 0.94-0.99 | x1.03 | 5.4e-15 |
| Smart + CV[visual+disagreement] | 36.7 | 29.8-43.4 | 0.87 | 0.65-1.19 | x1.15 | 2.4e-14 |
| Uniform + CV[visual+disagreement], 2 rollouts | 51.5 | 39.1-66.6 | 1.71 | 1.08-3.13 | x0.59 | 1.3e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 37.8 | 30.7-44.7 | 0.92 | 0.69-1.28 | x1.08 | 2.0e-14 |
| Oracle Neyman (not deployable) | 14.3 | 13.3-15.4 | 0.13 | 0.10-0.21 | x7.56 | 1.7e-14 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +60.9 (+32.0 to +88.7) | 103.7 (88.1-117.6) |
| all imagined frames | Rollout disagreement (no real data) | -92.5 (-97.6 to -84.1) | 95.0 (91.4-97.7) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +54.2 (+27.2 to +80.6) | 97.2 (79.1-116.0) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 36.7 (29.8-43.4) |
| within trained length | Visual predictor (no real data) | +56.1 (+31.1 to +79.7) | 89.7 (78.5-100.2) |
| within trained length | Rollout disagreement (no real data) | -96.7 (-97.8 to -95.2) | 96.8 (95.4-97.8) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +51.6 (+28.2 to +73.5) | 83.1 (72.9-92.7) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 67.3 (50.1-85.7) |
| beyond trained length | Visual predictor (no real data) | +70.0 (+38.0 to +100.8) | 117.0 (98.0-133.5) |
| beyond trained length | Rollout disagreement (no real data) | -90.1 (-97.9 to -77.9) | 95.9 (92.9-98.1) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +61.6 (+31.5 to +92.1) | 111.9 (85.9-141.9) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 41.3 (31.7-50.4) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 11.22 | 5.83-45.45 | 1.19 | 0.75-5.95 | 0.29 |
| within trained length | 23.71 | 12.16-62.76 | 1.97 | 1.77-60.02 | 0.10 |
| beyond trained length | 8.97 | 4.45-47.79 | 1.10 | 0.74-5.75 | 0.44 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 39.4 (30.9-46.8) | 27.9 (21.8-33.1) | 22.7 (17.8-27.0) | 19.7 (15.4-23.4) |
| 1 rollout, Uniform + shrunk CV[visual] | 39.3 (31.1-46.5) | 27.8 (22.0-32.9) | 22.7 (18.0-26.8) | 19.7 (15.5-23.2) |
| 2 rollouts, Smart + CV[visual+disagreement] | 37.8 (30.7-44.7) | 26.8 (21.7-31.6) | 21.8 (17.7-25.8) | 18.9 (15.4-22.4) |
| 3 rollouts, Smart + CV[visual+disagreement] | 36.7 (29.8-43.4) | 25.9 (21.1-30.7) | 21.2 (17.2-25.1) | 18.3 (14.9-21.7) |


## Asterix

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Asterix', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 45.5 | 40.9-49.9 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 112.7 | 42.8-184.3 | 6.15 | 0.94-18.71 | x0.16 | 9.6e-14 |
| Smart + CV[visual] | 86.1 | 41.6-135.5 | 3.58 | 0.87-10.06 | x0.28 | 3.7e-13 |
| Negative control: CV[shuffled proxies] | 45.8 | 41.3-49.9 | 1.01 | 1.00-1.04 | x0.99 | 5.8e-14 |
| Uniform + shrunk CV[visual] | 68.3 | 42.7-99.4 | 2.25 | 1.00-5.34 | x0.44 | 4.8e-14 |
| Uniform + CV[visual+disagreement] | 112.6 | 43.1-182.4 | 6.13 | 0.94-18.15 | x0.16 | 7.2e-14 |
| Uniform + shrunk CV[visual+disagreement] | 51.5 | 42.7-62.2 | 1.29 | 1.00-1.99 | x0.78 | 1.7e-14 |
| Smart + CV[visual+disagreement] | 85.0 | 41.9-133.0 | 3.49 | 0.87-9.66 | x0.29 | 2.6e-13 |
| Uniform + CV[visual+disagreement], 2 rollouts | 113.3 | 43.1-183.5 | 6.21 | 0.94-18.39 | x0.16 | 8.4e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 85.3 | 41.8-133.7 | 3.52 | 0.87-9.78 | x0.28 | 1.9e-13 |
| Oracle Neyman (not deployable) | 43.5 | 28.5-61.7 | 0.91 | 0.42-2.03 | x1.09 | 1.6e-13 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +233.0 (+35.9 to +574.3) | 924.8 (106.8-1586.8) |
| all imagined frames | Rollout disagreement (no real data) | -94.4 (-99.7 to -84.9) | 97.8 (95.0-99.7) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +234.6 (+36.0 to +575.5) | 914.6 (105.3-1566.0) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 85.0 (41.9-133.0) |
| within trained length | Visual predictor (no real data) | +418.4 (+97.0 to +813.7) | 1122.8 (222.7-1640.5) |
| within trained length | Rollout disagreement (no real data) | -94.6 (-99.9 to -84.6) | 98.7 (96.7-99.9) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +419.6 (+101.7 to +810.1) | 1114.6 (243.0-1625.9) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 278.4 (101.0-396.6) |
| beyond trained length | Visual predictor (no real data) | +269.5 (+34.2 to +677.5) | 1108.1 (103.9-1903.9) |
| beyond trained length | Rollout disagreement (no real data) | -94.3 (-99.7 to -84.8) | 97.5 (94.5-99.7) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +269.7 (+34.7 to +673.6) | 1090.9 (101.8-1871.6) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 83.5 (47.0-126.1) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 48.86 | 21.93-262.26 | 1.51 | 0.73-4.43 | 0.70 |
| within trained length | 58.98 | 22.82-1503.78 | 2.55 | 0.68-8.66 | 0.69 |
| beyond trained length | 45.79 | 21.23-227.45 | 1.32 | 0.73-3.27 | 0.63 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 45.5 (40.9-49.9) | 32.1 (28.9-35.3) | 26.2 (23.6-28.8) | 22.7 (20.4-24.9) |
| 1 rollout, Uniform + shrunk CV[visual] | 68.3 (42.7-99.4) | 48.3 (30.2-70.3) | 39.4 (24.7-57.4) | 34.1 (21.4-49.7) |
| 2 rollouts, Smart + CV[visual+disagreement] | 85.3 (41.8-133.7) | 60.4 (29.6-94.6) | 49.3 (24.2-77.2) | 42.7 (20.9-66.9) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 51.5 (42.7-62.2) | 36.4 (30.2-44.0) | 29.8 (24.7-35.9) | 25.8 (21.4-31.1) |


## Asterix, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'Asterix, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 45.8 | 41.8-49.7 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 100.7 | 42.4-162.3 | 4.82 | 0.96-13.37 | x0.21 | 2.9e-14 |
| Smart + CV[visual] | 77.3 | 40.9-119.3 | 2.84 | 0.87-7.15 | x0.35 | 3.2e-13 |
| Negative control: CV[shuffled proxies] | 46.4 | 42.2-50.4 | 1.02 | 1.00-1.07 | x0.98 | 4.8e-14 |
| Uniform + shrunk CV[visual] | 63.7 | 42.6-90.2 | 1.93 | 1.00-4.02 | x0.52 | 1.1e-14 |
| Uniform + CV[visual+disagreement] | 108.5 | 42.7-176.5 | 5.60 | 0.94-15.86 | x0.18 | 2.4e-14 |
| Uniform + shrunk CV[visual+disagreement] | 66.5 | 42.6-96.2 | 2.11 | 1.00-4.60 | x0.47 | 9.7e-15 |
| Smart + CV[visual+disagreement] | 78.4 | 39.6-122.3 | 2.93 | 0.82-7.55 | x0.34 | 2.0e-13 |
| Uniform + CV[visual+disagreement], 2 rollouts | 110.8 | 42.3-180.9 | 5.84 | 0.94-16.68 | x0.17 | 8.7e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 77.9 | 39.9-121.2 | 2.89 | 0.83-7.40 | x0.35 | 2.0e-13 |
| Oracle Neyman (not deployable) | 38.0 | 26.8-51.9 | 0.69 | 0.38-1.29 | x1.45 | 1.9e-13 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +191.2 (+40.1 to +439.6) | 787.0 (117.7-1346.2) |
| all imagined frames | Rollout disagreement (no real data) | -66.1 (-87.3 to -38.2) | 107.2 (84.9-133.8) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +181.7 (+38.0 to +419.1) | 745.8 (117.4-1274.7) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 78.4 (39.6-122.3) |
| within trained length | Visual predictor (no real data) | +328.3 (+83.7 to +678.1) | 968.6 (206.4-1543.0) |
| within trained length | Rollout disagreement (no real data) | -60.3 (-79.3 to -38.7) | 95.4 (80.2-113.0) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +298.9 (+81.2 to +602.0) | 856.4 (206.1-1349.8) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 220.1 (88.6-330.0) |
| beyond trained length | Visual predictor (no real data) | +218.6 (+40.5 to +512.5) | 935.9 (114.9-1602.3) |
| beyond trained length | Rollout disagreement (no real data) | -64.2 (-90.4 to -26.9) | 130.5 (87.5-182.5) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +209.5 (+39.3 to +493.6) | 903.0 (120.7-1546.2) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 90.1 (45.3-140.4) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 5.22 | 2.62-13.27 | 0.83 | 0.71-1.82 | 0.74 |
| within trained length | 4.35 | 2.31-10.02 | 0.80 | 0.67-1.83 | 0.75 |
| beyond trained length | 5.68 | 2.73-16.07 | 0.84 | 0.73-1.88 | 0.65 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 45.8 (41.8-49.7) | 32.4 (29.6-35.2) | 26.5 (24.1-28.7) | 22.9 (20.9-24.9) |
| 1 rollout, Uniform + shrunk CV[visual] | 63.7 (42.6-90.2) | 45.0 (30.1-63.7) | 36.8 (24.6-52.0) | 31.8 (21.3-45.1) |
| 2 rollouts, Smart + CV[visual+disagreement] | 77.9 (39.9-121.2) | 55.1 (28.2-85.7) | 45.0 (23.0-69.9) | 39.0 (19.9-60.6) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 66.5 (42.6-96.2) | 47.0 (30.1-68.0) | 38.4 (24.6-55.5) | 33.3 (21.3-48.1) |


## RoadRunner

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'RoadRunner', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 46.5 | 41.5-51.1 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 305.6 | 212.8-396.2 | 43.20 | 21.19-72.16 | x0.02 | 1.4e-13 |
| Smart + CV[visual] | 668.3 | 420.9-916.2 | 206.58 | 85.06-383.13 | x0.00 | 2.6e-13 |
| Negative control: CV[shuffled proxies] | 317.3 | 222.0-411.1 | 46.58 | 23.04-77.40 | x0.02 | 8.0e-14 |
| Uniform + shrunk CV[visual] | 46.5 | 41.5-51.1 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual+disagreement] | 303.7 | 213.0-392.3 | 42.65 | 21.42-70.24 | x0.02 | 1.1e-13 |
| Uniform + shrunk CV[visual+disagreement] | 46.5 | 41.5-51.1 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Smart + CV[visual+disagreement] | 652.9 | 423.4-879.8 | 197.16 | 86.69-351.69 | x0.01 | 3.2e-13 |
| Uniform + CV[visual+disagreement], 2 rollouts | 304.0 | 213.1-393.0 | 42.75 | 21.43-70.54 | x0.02 | 8.5e-14 |
| Smart + CV[visual+disagreement], 2 rollouts | 656.4 | 423.1-887.7 | 199.30 | 86.55-358.63 | x0.01 | 2.5e-13 |
| Oracle Neyman (not deployable) | 239.4 | 173.9-304.1 | 26.52 | 14.06-42.06 | x0.04 | 2.7e-13 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +656.5 (+446.3 to +894.0) | 949.8 (673.7-1213.8) |
| all imagined frames | Rollout disagreement (no real data) | -74.6 (-86.3 to -61.2) | 86.8 (81.4-91.4) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +660.2 (+446.0 to +903.9) | 960.8 (676.8-1237.4) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 652.9 (423.4-879.8) |
| within trained length | Visual predictor (no real data) | +8389.6 (-4200.6 to +28878.4) | 54241.9 (710.2-93505.4) |
| within trained length | Rollout disagreement (no real data) | -69.6 (-88.2 to -42.7) | 121.5 (85.0-170.3) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +8398.8 (-4249.1 to +28960.4) | 54407.5 (737.3-93783.0) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 11223.3 (1725.1-19188.5) |
| beyond trained length | Visual predictor (no real data) | +835.2 (+598.2 to +1112.1) | 1163.2 (801.0-1504.0) |
| beyond trained length | Rollout disagreement (no real data) | -73.3 (-85.3 to -59.5) | 86.7 (80.5-91.8) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +839.4 (+599.4 to +1128.0) | 1173.1 (795.8-1529.2) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 380.9 (286.6-469.1) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 38.02 | 4.80-105.21 | 1.30 | 0.99-1.69 | 0.28 |
| within trained length | 34.80 | 3.26-140.40 | 0.88 | 0.76-1.32 | 0.39 |
| beyond trained length | 39.33 | 4.69-99.97 | 1.42 | 1.06-1.78 | 0.14 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 46.5 (41.5-51.1) | 32.9 (29.4-36.1) | 26.8 (24.0-29.5) | 23.2 (20.8-25.5) |
| 1 rollout, Uniform + shrunk CV[visual] | 46.5 (41.5-51.1) | 32.9 (29.4-36.1) | 26.8 (24.0-29.5) | 23.2 (20.8-25.5) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 304.0 (213.1-393.0) | 215.0 (150.7-277.9) | 175.5 (123.0-226.9) | 152.0 (106.5-196.5) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 46.5 (41.5-51.1) | 32.9 (29.4-36.1) | 26.8 (24.0-29.5) | 23.2 (20.8-25.5) |


## RoadRunner, stochastic sampler

32 clips from 32 videos x 3 rollouts; 30 imagined frames after 4 real context frames; 16 patches per frame, 1 inspected. Predictors fit on 'RoadRunner, stochastic sampler', leaving the evaluated video out. 95% CIs resample whole videos.

| Audit (1 real patch per frame) | Relative error (%) | 95% CI | Variance vs uniform | 95% CI | Equivalent budget | Max bias (%) |
|---|---|---|---|---|---|---|
| Uniform (Horvitz-Thompson) | 45.7 | 41.3-49.8 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual] | 249.0 | 169.0-329.4 | 29.71 | 14.40-49.22 | x0.03 | 9.8e-14 |
| Smart + CV[visual] | 485.0 | 323.5-634.2 | 112.67 | 54.59-178.38 | x0.01 | 3.6e-13 |
| Negative control: CV[shuffled proxies] | 262.4 | 179.2-345.4 | 32.98 | 16.25-53.92 | x0.03 | 7.6e-14 |
| Uniform + shrunk CV[visual] | 45.7 | 41.3-49.8 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Uniform + CV[visual+disagreement] | 249.6 | 169.2-330.8 | 29.83 | 14.44-49.60 | x0.03 | 1.0e-13 |
| Uniform + shrunk CV[visual+disagreement] | 45.7 | 41.3-49.8 | 1.00 | 1.00-1.00 | x1.00 | 0.0e+00 |
| Smart + CV[visual+disagreement] | 480.5 | 324.5-626.8 | 110.57 | 54.97-173.69 | x0.01 | 4.4e-13 |
| Uniform + CV[visual+disagreement], 2 rollouts | 249.4 | 169.1-330.3 | 29.79 | 14.42-49.45 | x0.03 | 1.4e-13 |
| Smart + CV[visual+disagreement], 2 rollouts | 481.9 | 324.3-627.7 | 111.22 | 54.86-174.89 | x0.01 | 4.4e-13 |
| Oracle Neyman (not deployable) | 204.2 | 140.3-269.0 | 19.97 | 9.97-32.91 | x0.05 | 2.7e-13 |

**Self-assessment versus audit**

| Frames | Estimator | Signed bias (%) [95% CI] | Relative error (%) [95% CI] |
|---|---|---|---|
| all imagined frames | Visual predictor (no real data) | +614.3 (+400.1 to +878.6) | 945.9 (615.4-1290.6) |
| all imagined frames | Rollout disagreement (no real data) | -37.0 (-50.4 to -24.0) | 56.3 (45.9-65.7) |
| all imagined frames | Calibrated predictor (visual+disagreement) (no real data) | +620.4 (+400.9 to +892.7) | 964.5 (616.9-1324.0) |
| all imagined frames | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 480.5 (324.5-626.8) |
| within trained length | Visual predictor (no real data) | +7664.1 (-3869.2 to +26277.7) | 49170.6 (818.2-84714.8) |
| within trained length | Rollout disagreement (no real data) | -42.8 (-56.4 to -28.8) | 61.4 (52.8-69.4) |
| within trained length | Calibrated predictor (visual+disagreement) (no real data) | +7671.9 (-3869.8 to +26290.8) | 49185.3 (835.6-84736.3) |
| within trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 10109.9 (1408.2-17327.0) |
| beyond trained length | Visual predictor (no real data) | +726.4 (+511.5 to +999.9) | 1054.5 (662.7-1430.1) |
| beyond trained length | Rollout disagreement (no real data) | -29.7 (-45.6 to -14.2) | 60.6 (50.5-69.8) |
| beyond trained length | Calibrated predictor (visual+disagreement) (no real data) | +731.0 (+511.7 to +1012.6) | 1069.6 (661.6-1459.7) |
| beyond trained length | Audit: Smart + CV[visual+disagreement], 1 patch | 0 (exact) | 305.3 (237.3-373.2) |

**Calibration of the model's disagreement** (mean real error / mean disagreement: 1 = calibrated, >1 = over-confident; the slope through the origin is dominated by the few patches with large disagreement)

| Frames | Mean error / mean disagreement | 95% CI | Slope | 95% CI | Spearman |
|---|---|---|---|---|---|
| all imagined frames | 10.61 | 1.50-26.47 | 0.90 | 0.78-1.08 | 0.46 |
| within trained length | 10.52 | 1.42-35.23 | 0.82 | 0.77-0.89 | 0.53 |
| beyond trained length | 10.64 | 1.39-25.25 | 0.93 | 0.78-1.16 | 0.35 |

**Rollouts versus real patches** (relative error %, all imagined frames)

| Configuration | 1 patch/frame | 2 patches/frame | 3 patches/frame | 4 patches/frame |
|---|---|---|---|---|
| 1 rollout, uniform | 45.7 (41.3-49.8) | 32.3 (29.2-35.2) | 26.4 (23.9-28.8) | 22.8 (20.7-24.9) |
| 1 rollout, Uniform + shrunk CV[visual] | 45.7 (41.3-49.8) | 32.3 (29.2-35.2) | 26.4 (23.9-28.8) | 22.8 (20.7-24.9) |
| 2 rollouts, Uniform + CV[visual+disagreement] | 249.4 (169.1-330.3) | 176.3 (119.6-233.6) | 144.0 (97.6-190.7) | 124.7 (84.6-165.2) |
| 3 rollouts, Uniform + shrunk CV[visual+disagreement] | 45.7 (41.3-49.8) | 32.3 (29.2-35.2) | 26.4 (23.9-28.8) | 22.8 (20.7-24.9) |


## Findings

- **Uniform + CV[visual]**: variance x1.90 of uniform (95% CI 1.46-2.70), the accuracy of 0.53 uniform patches per frame. Not distinguishable from uniform.
- **Smart + CV[visual]**: variance x1.90 of uniform (95% CI 1.46-2.64), the accuracy of 0.53 uniform patches per frame. Not distinguishable from uniform.
- **Negative control: CV[shuffled proxies]**: variance x1.02 of uniform (95% CI 1.01-1.04), the accuracy of 0.98 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + shrunk CV[visual]**: variance x0.99 of uniform (95% CI 0.98-1.00), the accuracy of 1.01 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + CV[visual+disagreement]**: variance x2.82 of uniform (95% CI 1.57-4.85), the accuracy of 0.35 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + shrunk CV[visual+disagreement]**: variance x1.03 of uniform (95% CI 1.00-1.09), the accuracy of 0.98 uniform patches per frame. Not distinguishable from uniform.
- **Smart + CV[visual+disagreement]**: variance x2.27 of uniform (95% CI 1.54-3.45), the accuracy of 0.44 uniform patches per frame. Not distinguishable from uniform.
- **Uniform + CV[visual+disagreement], 2 rollouts**: variance x2.99 of uniform (95% CI 1.60-5.21), the accuracy of 0.33 uniform patches per frame. Not distinguishable from uniform.
- **Smart + CV[visual+disagreement], 2 rollouts**: variance x2.18 of uniform (95% CI 1.54-3.16), the accuracy of 0.46 uniform patches per frame. Not distinguishable from uniform.
- **Rollouts versus patches** (best audit of each budget: Uniform + shrunk CV[visual+disagreement] for 3 rollouts, Uniform + shrunk CV[visual] for 1): with 3 rollouts and 1 patch per frame the audit is as accurate as a single-rollout audit with 0.97 patches per frame (95% CI 0.91-1.00). Variance of 3 rollouts + 1 patch relative to 1 rollout + 2 patches: 2.07 (2.00-2.20).
- **Breakout, all imagined frames, Rollout disagreement**: bias -80.6% (-99.3 to -53.2), CI excludes zero.
- **Breakout, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +423.4% (+285.8 to +555.4), CI excludes zero.
- **Breakout, within trained length, Rollout disagreement**: bias -88.4% (-99.6 to -67.8), CI excludes zero.
- **Breakout, within trained length, Calibrated predictor (visual+disagreement)**: bias +337.3% (+252.6 to +416.9), CI excludes zero.
- **Breakout, beyond trained length, Rollout disagreement**: bias -76.2% (-99.5 to -39.1), CI excludes zero.
- **Breakout, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +513.0% (+345.0 to +675.8), CI excludes zero.
- **Breakout, stochastic sampler, all imagined frames, Rollout disagreement**: bias -83.8% (-97.0 to -58.9), CI excludes zero.
- **Breakout, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +379.0% (+255.5 to +498.9), CI excludes zero.
- **Breakout, stochastic sampler, within trained length, Rollout disagreement**: bias -92.8% (-97.8 to -84.6), CI excludes zero.
- **Breakout, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +305.8% (+229.0 to +379.4), CI excludes zero.
- **Breakout, stochastic sampler, beyond trained length, Rollout disagreement**: bias -77.6% (-97.2 to -39.5), CI excludes zero.
- **Breakout, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +459.7% (+307.6 to +609.8), CI excludes zero.
- **Pong, all imagined frames, Rollout disagreement**: bias -99.5% (-99.8 to -98.9), CI excludes zero.
- **Pong, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +58.8% (+43.1 to +72.1), CI excludes zero.
- **Pong, within trained length, Rollout disagreement**: bias -99.5% (-99.8 to -99.0), CI excludes zero.
- **Pong, within trained length, Calibrated predictor (visual+disagreement)**: bias +46.3% (+32.4 to +57.6), CI excludes zero.
- **Pong, beyond trained length, Rollout disagreement**: bias -99.5% (-99.8 to -98.8), CI excludes zero.
- **Pong, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +74.6% (+55.7 to +90.5), CI excludes zero.
- **Pong, stochastic sampler, all imagined frames, Rollout disagreement**: bias -93.1% (-97.7 to -87.4), CI excludes zero.
- **Pong, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +26.2% (+15.8 to +34.9), CI excludes zero.
- **Pong, stochastic sampler, within trained length, Rollout disagreement**: bias -95.5% (-98.8 to -90.4), CI excludes zero.
- **Pong, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +21.3% (+12.1 to +28.7), CI excludes zero.
- **Pong, stochastic sampler, beyond trained length, Rollout disagreement**: bias -92.2% (-98.4 to -84.8), CI excludes zero.
- **Pong, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +33.7% (+21.8 to +43.6), CI excludes zero.
- **Boxing, all imagined frames, Rollout disagreement**: bias -40.3% (-49.9 to -30.9), CI excludes zero.
- **Boxing, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +9.0% (-2.8 to +21.5), CI includes zero.
- **Boxing, within trained length, Rollout disagreement**: bias -55.5% (-67.1 to -43.5), CI excludes zero.
- **Boxing, within trained length, Calibrated predictor (visual+disagreement)**: bias +28.2% (+3.5 to +55.9), CI excludes zero.
- **Boxing, beyond trained length, Rollout disagreement**: bias -30.2% (-40.6 to -19.8), CI excludes zero.
- **Boxing, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +9.2% (-2.1 to +20.6), CI includes zero.
- **Boxing, stochastic sampler, all imagined frames, Rollout disagreement**: bias -22.5% (-30.8 to -13.9), CI excludes zero.
- **Boxing, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +9.7% (-1.5 to +21.1), CI includes zero.
- **Boxing, stochastic sampler, within trained length, Rollout disagreement**: bias -29.7% (-40.5 to -18.2), CI excludes zero.
- **Boxing, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +13.8% (-1.3 to +30.0), CI includes zero.
- **Boxing, stochastic sampler, beyond trained length, Rollout disagreement**: bias -15.7% (-25.6 to -5.5), CI excludes zero.
- **Boxing, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +12.1% (+0.6 to +24.2), CI excludes zero.
- **MsPacman, all imagined frames, Rollout disagreement**: bias -87.6% (-92.7 to -82.1), CI excludes zero.
- **MsPacman, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +462.2% (+58.7 to +1037.6), CI excludes zero.
- **MsPacman, within trained length, Rollout disagreement**: bias -92.6% (-97.1 to -87.1), CI excludes zero.
- **MsPacman, within trained length, Calibrated predictor (visual+disagreement)**: bias +671.9% (+226.8 to +1233.8), CI excludes zero.
- **MsPacman, beyond trained length, Rollout disagreement**: bias -85.1% (-91.3 to -78.3), CI excludes zero.
- **MsPacman, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +495.4% (+46.0 to +1159.4), CI excludes zero.
- **MsPacman, stochastic sampler, all imagined frames, Rollout disagreement**: bias -58.7% (-72.4 to -43.2), CI excludes zero.
- **MsPacman, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +375.3% (+48.0 to +845.6), CI excludes zero.
- **MsPacman, stochastic sampler, within trained length, Rollout disagreement**: bias -70.1% (-79.5 to -59.7), CI excludes zero.
- **MsPacman, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +543.3% (+184.4 to +991.6), CI excludes zero.
- **MsPacman, stochastic sampler, beyond trained length, Rollout disagreement**: bias -52.9% (-69.9 to -33.6), CI excludes zero.
- **MsPacman, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +411.4% (+43.2 to +952.1), CI excludes zero.
- **Seaquest, all imagined frames, Rollout disagreement**: bias -95.5% (-98.2 to -91.8), CI excludes zero.
- **Seaquest, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +55.4% (+16.1 to +104.7), CI excludes zero.
- **Seaquest, within trained length, Rollout disagreement**: bias -98.3% (-99.4 to -96.8), CI excludes zero.
- **Seaquest, within trained length, Calibrated predictor (visual+disagreement)**: bias +86.6% (+33.5 to +146.8), CI excludes zero.
- **Seaquest, beyond trained length, Rollout disagreement**: bias -94.5% (-97.8 to -90.1), CI excludes zero.
- **Seaquest, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +65.2% (+25.0 to +115.7), CI excludes zero.
- **Seaquest, stochastic sampler, all imagined frames, Rollout disagreement**: bias -66.6% (-76.2 to -56.6), CI excludes zero.
- **Seaquest, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +46.6% (+16.1 to +83.1), CI excludes zero.
- **Seaquest, stochastic sampler, within trained length, Rollout disagreement**: bias -67.2% (-80.9 to -48.3), CI excludes zero.
- **Seaquest, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +62.6% (+25.9 to +103.1), CI excludes zero.
- **Seaquest, stochastic sampler, beyond trained length, Rollout disagreement**: bias -64.4% (-74.3 to -54.1), CI excludes zero.
- **Seaquest, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +57.1% (+25.3 to +95.9), CI excludes zero.
- **Freeway, all imagined frames, Rollout disagreement**: bias -98.7% (-99.0 to -98.3), CI excludes zero.
- **Freeway, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +59.5% (+32.3 to +85.0), CI excludes zero.
- **Freeway, within trained length, Rollout disagreement**: bias -98.7% (-98.9 to -98.5), CI excludes zero.
- **Freeway, within trained length, Calibrated predictor (visual+disagreement)**: bias +56.0% (+31.2 to +79.4), CI excludes zero.
- **Freeway, beyond trained length, Rollout disagreement**: bias -98.7% (-99.1 to -98.2), CI excludes zero.
- **Freeway, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +66.2% (+36.9 to +93.7), CI excludes zero.
- **Freeway, stochastic sampler, all imagined frames, Rollout disagreement**: bias -92.5% (-97.6 to -84.1), CI excludes zero.
- **Freeway, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +54.2% (+27.2 to +80.6), CI excludes zero.
- **Freeway, stochastic sampler, within trained length, Rollout disagreement**: bias -96.7% (-97.8 to -95.2), CI excludes zero.
- **Freeway, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +51.6% (+28.2 to +73.5), CI excludes zero.
- **Freeway, stochastic sampler, beyond trained length, Rollout disagreement**: bias -90.1% (-97.9 to -77.9), CI excludes zero.
- **Freeway, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +61.6% (+31.5 to +92.1), CI excludes zero.
- **Asterix, all imagined frames, Rollout disagreement**: bias -94.4% (-99.7 to -84.9), CI excludes zero.
- **Asterix, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +234.6% (+36.0 to +575.5), CI excludes zero.
- **Asterix, within trained length, Rollout disagreement**: bias -94.6% (-99.9 to -84.6), CI excludes zero.
- **Asterix, within trained length, Calibrated predictor (visual+disagreement)**: bias +419.6% (+101.7 to +810.1), CI excludes zero.
- **Asterix, beyond trained length, Rollout disagreement**: bias -94.3% (-99.7 to -84.8), CI excludes zero.
- **Asterix, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +269.7% (+34.7 to +673.6), CI excludes zero.
- **Asterix, stochastic sampler, all imagined frames, Rollout disagreement**: bias -66.1% (-87.3 to -38.2), CI excludes zero.
- **Asterix, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +181.7% (+38.0 to +419.1), CI excludes zero.
- **Asterix, stochastic sampler, within trained length, Rollout disagreement**: bias -60.3% (-79.3 to -38.7), CI excludes zero.
- **Asterix, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +298.9% (+81.2 to +602.0), CI excludes zero.
- **Asterix, stochastic sampler, beyond trained length, Rollout disagreement**: bias -64.2% (-90.4 to -26.9), CI excludes zero.
- **Asterix, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +209.5% (+39.3 to +493.6), CI excludes zero.
- **RoadRunner, all imagined frames, Rollout disagreement**: bias -74.6% (-86.3 to -61.2), CI excludes zero.
- **RoadRunner, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +660.2% (+446.0 to +903.9), CI excludes zero.
- **RoadRunner, within trained length, Rollout disagreement**: bias -69.6% (-88.2 to -42.7), CI excludes zero.
- **RoadRunner, within trained length, Calibrated predictor (visual+disagreement)**: bias +8398.8% (-4249.1 to +28960.4), CI includes zero.
- **RoadRunner, beyond trained length, Rollout disagreement**: bias -73.3% (-85.3 to -59.5), CI excludes zero.
- **RoadRunner, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +839.4% (+599.4 to +1128.0), CI excludes zero.
- **RoadRunner, stochastic sampler, all imagined frames, Rollout disagreement**: bias -37.0% (-50.4 to -24.0), CI excludes zero.
- **RoadRunner, stochastic sampler, all imagined frames, Calibrated predictor (visual+disagreement)**: bias +620.4% (+400.9 to +892.7), CI excludes zero.
- **RoadRunner, stochastic sampler, within trained length, Rollout disagreement**: bias -42.8% (-56.4 to -28.8), CI excludes zero.
- **RoadRunner, stochastic sampler, within trained length, Calibrated predictor (visual+disagreement)**: bias +7671.9% (-3869.8 to +26290.8), CI includes zero.
- **RoadRunner, stochastic sampler, beyond trained length, Rollout disagreement**: bias -29.7% (-45.6 to -14.2), CI excludes zero.
- **RoadRunner, stochastic sampler, beyond trained length, Calibrated predictor (visual+disagreement)**: bias +731.0% (+511.7 to +1012.6), CI excludes zero.
- **Unbiasedness**: the exact expectation of every audit equals the truth to numerical precision (max bias column), in every condition and horizon, including the negative control.
