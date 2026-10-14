## Minecraft, 50 steps versus Minecraft, 100 steps

16 identical clips from 10 videos, 3 rollouts each. Bootstrap over videos, paired.

| Frames | Setting | Mean patch error | Mean error / mean disagreement [95% CI] | Disagreement as drift estimate: bias (%) [95% CI] | Uniform + CV[visual+disagreement]: variance vs uniform [95% CI] |
|---|---|---|---|---|---|
| all imagined frames | Minecraft, 50 steps | 0.0486 | 2.17 (1.43-2.82) | -38.0 (-52.8 to -20.0) | 0.63 (0.48-0.77) |
| all imagined frames | Minecraft, 100 steps | 0.0493 | 2.11 (1.45-2.64) | -36.8 (-53.0 to -15.6) | 0.62 (0.47-0.75) |
| all imagined frames | difference (second - first) |  | -0.06 (-0.38 to +0.26) | +1.2 (-12.5 to +14.9) |  |
| within trained length | Minecraft, 50 steps | 0.0300 | 1.95 (1.27-2.60) | -24.4 (-48.3 to +2.6) | 0.91 (0.67-1.31) |
| within trained length | Minecraft, 100 steps | 0.0311 | 1.98 (1.35-2.68) | -29.7 (-55.4 to -1.1) | 0.90 (0.57-1.39) |
| within trained length | difference (second - first) |  | +0.03 (-0.38 to +0.59) | -5.3 (-24.6 to +8.6) |  |
| beyond trained length | Minecraft, 50 steps | 0.0634 | 2.27 (1.48-2.99) | -39.3 (-53.4 to -21.2) | 0.62 (0.44-0.77) |
| beyond trained length | Minecraft, 100 steps | 0.0638 | 2.17 (1.46-2.69) | -35.1 (-52.2 to -12.4) | 0.62 (0.47-0.77) |
| beyond trained length | difference (second - first) |  | -0.10 (-0.53 to +0.27) | +4.3 (-9.7 to +19.7) |  |

**Verdict.** The over-confidence does not depend on the setting: the difference in error/disagreement is statistically indistinguishable from zero. Mean real error is 2.17x the model's disagreement with 'Minecraft, 50 steps' and 2.11x with 'Minecraft, 100 steps'; 1.00 would be a calibrated model.
