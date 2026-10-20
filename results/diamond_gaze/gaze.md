## Which patch to look at: gaze policies on DIAMOND

New episodes, 2 rollouts per window, every policy under the same random numbers. Drift ratios are total drift with feedback over total drift of the comparison, 95% CI over episodes (paired). Online bias: pooled bias of the drift estimate from the patches that were shown.

| Game | Gaze | Patches/frame | vs open loop | vs random gaze | Episodes better than random | Online bias (%) |
|---|---|---|---|---|---|---|
| Asterix | Random | 1 | 0.79 (0.71-0.88) |  |  | -0.9 (-10.8 to +10.3) |
| Asterix | Motion | 1 | 0.59 (0.45-0.72) | 0.74 (0.62-0.84) | 88% | -1.5 (-21.2 to +26.2) |
| Asterix | Disagreement | 1 | 0.58 (0.46-0.69) | 0.73 (0.63-0.80) | 100% | -5.3 (-22.2 to +19.9) |
| Asterix | Predicted error (visual) | 1 | 0.72 (0.62-0.83) | 0.91 (0.83-0.98) | 78% | -6.1 (-14.7 to +4.3) |
| Asterix | Predicted error (visual + disagreement) | 1 | 0.66 (0.54-0.78) | 0.84 (0.73-0.92) | 91% | -7.9 (-17.4 to +3.9) |
| Asterix | Disagreement, 30% floor | 1 | 0.58 (0.46-0.70) | 0.74 (0.64-0.81) | 97% | +1.3 (-8.1 to +14.4) |
| Asterix | Motion x disagreement | 1 | 0.53 (0.39-0.66) | 0.67 (0.53-0.77) | 97% | -4.8 (-27.1 to +30.3) |
| Asterix | Motion x disagreement, 30% floor | 1 | 0.61 (0.46-0.75) | 0.77 (0.64-0.87) | 88% | -5.6 (-18.9 to +12.1) |
| Asterix | Oracle (not deployable) | 1 | 0.28 (0.14-0.43) | 0.35 (0.18-0.52) | 100% |  |
| Asterix | Random | 2 | 0.56 (0.48-0.64) |  |  |  |
| Asterix | Motion | 2 | 0.42 (0.29-0.57) | 0.76 (0.55-0.96) | 84% |  |
| Asterix | Predicted error (visual + disagreement) | 2 | 0.48 (0.36-0.60) | 0.86 (0.72-0.97) | 78% |  |
| Asterix | Oracle (not deployable) | 2 | 0.11 (0.07-0.17) | 0.20 (0.13-0.29) | 100% |  |
| Asterix | Random | 4 | 0.37 (0.27-0.49) |  |  |  |
| Asterix | Motion | 4 | 0.22 (0.15-0.31) | 0.60 (0.47-0.72) | 91% |  |
| Asterix | Predicted error (visual + disagreement) | 4 | 0.24 (0.17-0.34) | 0.65 (0.55-0.79) | 94% |  |
| Asterix | Oracle (not deployable) | 4 | 0.09 (0.05-0.16) | 0.25 (0.17-0.35) | 100% |  |
| Boxing | Random | 1 | 0.78 (0.73-0.82) |  |  | -0.8 (-9.4 to +8.2) |
| Boxing | Motion | 1 | 0.52 (0.48-0.58) | 0.67 (0.62-0.73) | 97% | -12.6 (-22.5 to -2.0) |
| Boxing | Disagreement | 1 | 0.43 (0.40-0.48) | 0.56 (0.51-0.61) | 100% | +0.4 (-4.9 to +6.3) |
| Boxing | Predicted error (visual) | 1 | 0.56 (0.51-0.61) | 0.72 (0.66-0.78) | 94% | -11.4 (-19.9 to -2.8) |
| Boxing | Predicted error (visual + disagreement) | 1 | 0.47 (0.42-0.52) | 0.60 (0.55-0.66) | 97% | -4.9 (-10.9 to +0.8) |
| Boxing | Disagreement, 30% floor | 1 | 0.50 (0.46-0.55) | 0.64 (0.59-0.70) | 100% | -5.1 (-10.5 to +0.6) |
| Boxing | Motion x disagreement | 1 | 0.45 (0.41-0.49) | 0.57 (0.53-0.62) | 100% | -4.2 (-10.6 to +2.2) |
| Boxing | Motion x disagreement, 30% floor | 1 | 0.50 (0.46-0.55) | 0.65 (0.60-0.70) | 97% | -0.8 (-7.3 to +5.5) |
| Boxing | Oracle (not deployable) | 1 | 0.24 (0.21-0.26) | 0.30 (0.27-0.34) | 100% |  |
| Boxing | Random | 2 | 0.65 (0.61-0.69) |  |  |  |
| Boxing | Motion | 2 | 0.33 (0.29-0.37) | 0.50 (0.46-0.56) | 97% |  |
| Boxing | Predicted error (visual + disagreement) | 2 | 0.32 (0.29-0.36) | 0.49 (0.45-0.54) | 100% |  |
| Boxing | Oracle (not deployable) | 2 | 0.17 (0.15-0.20) | 0.26 (0.23-0.30) | 100% |  |
| Boxing | Random | 4 | 0.49 (0.44-0.54) |  |  |  |
| Boxing | Motion | 4 | 0.19 (0.17-0.22) | 0.40 (0.36-0.45) | 100% |  |
| Boxing | Predicted error (visual + disagreement) | 4 | 0.21 (0.18-0.24) | 0.43 (0.38-0.48) | 100% |  |
| Boxing | Oracle (not deployable) | 4 | 0.16 (0.14-0.18) | 0.32 (0.29-0.36) | 100% |  |
| Breakout | Random | 1 | 0.72 (0.57-0.90) |  |  | +5.4 (-21.1 to +35.5) |
| Breakout | Motion | 1 | 0.37 (0.27-0.51) | 0.52 (0.39-0.70) | 41% | -25.6 (-49.7 to +8.8) |
| Breakout | Disagreement | 1 | 0.30 (0.20-0.44) | 0.42 (0.29-0.59) | 100% | +58.0 (-0.5 to +125.7) |
| Breakout | Predicted error (visual) | 1 | 0.61 (0.44-0.82) | 0.85 (0.74-0.95) | 91% | -10.3 (-29.1 to +13.5) |
| Breakout | Predicted error (visual + disagreement) | 1 | 0.40 (0.29-0.56) | 0.56 (0.45-0.70) | 100% | -3.5 (-28.0 to +24.1) |
| Breakout | Disagreement, 30% floor | 1 | 0.33 (0.21-0.50) | 0.46 (0.32-0.63) | 97% | +46.5 (+11.2 to +87.4) |
| Breakout | Motion x disagreement | 1 | 0.26 (0.18-0.38) | 0.36 (0.26-0.51) | 94% | +22.9 (-9.8 to +56.0) |
| Breakout | Motion x disagreement, 30% floor | 1 | 0.27 (0.19-0.40) | 0.38 (0.27-0.53) | 84% | +24.1 (-0.9 to +48.9) |
| Breakout | Oracle (not deployable) | 1 | 0.15 (0.11-0.22) | 0.21 (0.16-0.29) | 100% |  |
| Breakout | Random | 2 | 0.42 (0.34-0.55) |  |  |  |
| Breakout | Motion | 2 | 0.26 (0.18-0.38) | 0.62 (0.44-0.91) | 41% |  |
| Breakout | Predicted error (visual + disagreement) | 2 | 0.26 (0.17-0.39) | 0.61 (0.47-0.77) | 94% |  |
| Breakout | Oracle (not deployable) | 2 | 0.12 (0.09-0.18) | 0.29 (0.24-0.38) | 100% |  |
| Breakout | Random | 4 | 0.33 (0.25-0.44) |  |  |  |
| Breakout | Motion | 4 | 0.15 (0.11-0.23) | 0.46 (0.32-0.71) | 56% |  |
| Breakout | Predicted error (visual + disagreement) | 4 | 0.16 (0.12-0.23) | 0.49 (0.37-0.68) | 94% |  |
| Breakout | Oracle (not deployable) | 4 | 0.11 (0.08-0.15) | 0.32 (0.24-0.45) | 100% |  |
| Freeway | Random | 1 | 0.71 (0.57-0.86) |  |  | +3.0 (-13.1 to +20.3) |
| Freeway | Motion | 1 | 0.68 (0.57-0.80) | 0.96 (0.88-1.05) | 69% | +12.7 (-15.1 to +65.7) |
| Freeway | Disagreement | 1 | 0.62 (0.49-0.79) | 0.87 (0.78-0.97) | 75% | +18.0 (+3.9 to +34.6) |
| Freeway | Predicted error (visual) | 1 | 0.68 (0.61-0.76) | 0.95 (0.84-1.14) | 78% | +7.9 (-5.0 to +24.7) |
| Freeway | Predicted error (visual + disagreement) | 1 | 0.59 (0.50-0.70) | 0.83 (0.70-0.99) | 81% | +13.1 (-0.3 to +31.0) |
| Freeway | Disagreement, 30% floor | 1 | 0.63 (0.52-0.78) | 0.89 (0.80-1.00) | 72% | +12.1 (-1.4 to +25.8) |
| Freeway | Motion x disagreement | 1 | 0.64 (0.53-0.78) | 0.90 (0.81-1.00) | 78% | +3.5 (-13.7 to +26.5) |
| Freeway | Motion x disagreement, 30% floor | 1 | 0.64 (0.53-0.78) | 0.89 (0.81-0.99) | 75% | +6.7 (-11.3 to +26.6) |
| Freeway | Oracle (not deployable) | 1 | 0.40 (0.31-0.54) | 0.56 (0.46-0.70) | 100% |  |
| Freeway | Random | 2 | 0.63 (0.50-0.77) |  |  |  |
| Freeway | Motion | 2 | 0.52 (0.42-0.66) | 0.83 (0.71-0.95) | 66% |  |
| Freeway | Predicted error (visual + disagreement) | 2 | 0.47 (0.37-0.60) | 0.74 (0.64-0.87) | 94% |  |
| Freeway | Oracle (not deployable) | 2 | 0.37 (0.28-0.49) | 0.58 (0.47-0.73) | 100% |  |
| Freeway | Random | 4 | 0.46 (0.37-0.58) |  |  |  |
| Freeway | Motion | 4 | 0.43 (0.34-0.54) | 0.93 (0.87-1.00) | 72% |  |
| Freeway | Predicted error (visual + disagreement) | 4 | 0.38 (0.30-0.49) | 0.83 (0.77-0.90) | 100% |  |
| Freeway | Oracle (not deployable) | 4 | 0.33 (0.26-0.45) | 0.72 (0.63-0.83) | 100% |  |
| MsPacman | Random | 1 | 0.84 (0.79-0.88) |  |  | -7.0 (-16.4 to +1.3) |
| MsPacman | Motion | 1 | 0.65 (0.58-0.72) | 0.78 (0.70-0.86) | 84% | -8.3 (-24.8 to +13.7) |
| MsPacman | Disagreement | 1 | 0.59 (0.52-0.65) | 0.70 (0.62-0.78) | 94% | -6.8 (-17.5 to +4.6) |
| MsPacman | Predicted error (visual) | 1 | 0.74 (0.67-0.81) | 0.88 (0.83-0.94) | 75% | -4.4 (-16.0 to +9.1) |
| MsPacman | Predicted error (visual + disagreement) | 1 | 0.65 (0.59-0.71) | 0.78 (0.73-0.83) | 84% | -5.2 (-12.7 to +2.8) |
| MsPacman | Disagreement, 30% floor | 1 | 0.62 (0.56-0.68) | 0.75 (0.67-0.81) | 94% | -6.1 (-14.7 to +2.9) |
| MsPacman | Motion x disagreement | 1 | 0.56 (0.49-0.63) | 0.67 (0.60-0.73) | 97% | +4.4 (-10.2 to +20.8) |
| MsPacman | Motion x disagreement, 30% floor | 1 | 0.61 (0.54-0.69) | 0.74 (0.66-0.81) | 97% | -0.6 (-11.2 to +11.4) |
| MsPacman | Oracle (not deployable) | 1 | 0.28 (0.22-0.33) | 0.33 (0.27-0.39) | 100% |  |
| MsPacman | Random | 2 | 0.68 (0.61-0.75) |  |  |  |
| MsPacman | Motion | 2 | 0.40 (0.34-0.48) | 0.59 (0.50-0.68) | 91% |  |
| MsPacman | Predicted error (visual + disagreement) | 2 | 0.42 (0.37-0.48) | 0.61 (0.56-0.68) | 100% |  |
| MsPacman | Oracle (not deployable) | 2 | 0.17 (0.13-0.22) | 0.25 (0.19-0.31) | 100% |  |
| MsPacman | Random | 4 | 0.46 (0.39-0.54) |  |  |  |
| MsPacman | Motion | 4 | 0.24 (0.19-0.29) | 0.51 (0.43-0.60) | 94% |  |
| MsPacman | Predicted error (visual + disagreement) | 4 | 0.26 (0.21-0.31) | 0.56 (0.48-0.63) | 97% |  |
| MsPacman | Oracle (not deployable) | 4 | 0.14 (0.10-0.18) | 0.30 (0.24-0.35) | 100% |  |
| Pong | Random | 1 | 0.96 (0.93-0.98) |  |  | +5.7 (-0.8 to +13.9) |
| Pong | Motion | 1 | 0.94 (0.89-0.98) | 0.98 (0.95-1.00) | 66% | +6.4 (-3.9 to +17.8) |
| Pong | Disagreement | 1 | 0.96 (0.91-0.98) | 0.99 (0.97-1.02) | 94% | -3.1 (-17.8 to +12.5) |
| Pong | Predicted error (visual) | 1 | 0.96 (0.93-0.98) | 1.00 (1.00-1.00) | 38% | -0.5 (-5.4 to +5.0) |
| Pong | Predicted error (visual + disagreement) | 1 | 0.95 (0.90-0.98) | 0.99 (0.96-1.00) | 38% | -1.7 (-5.6 to +1.9) |
| Pong | Disagreement, 30% floor | 1 | 0.96 (0.92-0.98) | 1.00 (0.97-1.02) | 94% | +0.4 (-12.4 to +11.3) |
| Pong | Motion x disagreement | 1 | 0.94 (0.90-0.98) | 0.98 (0.95-1.01) | 97% | -1.7 (-16.9 to +13.3) |
| Pong | Motion x disagreement, 30% floor | 1 | 0.96 (0.92-0.98) | 1.00 (0.97-1.02) | 88% | -6.2 (-17.8 to +3.6) |
| Pong | Oracle (not deployable) | 1 | 0.90 (0.83-0.96) | 0.93 (0.88-0.98) | 56% |  |
| Pong | Random | 2 | 0.95 (0.92-0.97) |  |  |  |
| Pong | Motion | 2 | 0.90 (0.84-0.95) | 0.95 (0.91-0.98) | 88% |  |
| Pong | Predicted error (visual + disagreement) | 2 | 0.93 (0.89-0.97) | 0.98 (0.96-1.00) | 59% |  |
| Pong | Oracle (not deployable) | 2 | 0.89 (0.84-0.95) | 0.94 (0.90-0.98) | 25% |  |
| Pong | Random | 4 | 0.93 (0.90-0.95) |  |  |  |
| Pong | Motion | 4 | 0.87 (0.82-0.93) | 0.94 (0.90-0.98) | 100% |  |
| Pong | Predicted error (visual + disagreement) | 4 | 0.90 (0.85-0.94) | 0.97 (0.94-0.99) | 66% |  |
| Pong | Oracle (not deployable) | 4 | 0.88 (0.83-0.94) | 0.95 (0.91-0.99) | 22% |  |
| RoadRunner | Random | 1 | 0.90 (0.81-0.94) |  |  | -8.8 (-31.0 to +1.9) |
| RoadRunner | Motion | 1 | 0.74 (0.55-0.85) | 0.83 (0.65-0.91) | 84% | -18.3 (-24.3 to -2.2) |
| RoadRunner | Disagreement | 1 | 0.72 (0.50-0.84) | 0.80 (0.59-0.90) | 88% | -22.5 (-32.2 to +7.8) |
| RoadRunner | Predicted error (visual) | 1 | 0.89 (0.78-0.95) | 1.00 (0.90-1.06) | 50% | -23.4 (-40.0 to +16.6) |
| RoadRunner | Predicted error (visual + disagreement) | 1 | 0.91 (0.80-0.96) | 1.01 (0.92-1.08) | 47% | -34.7 (-53.1 to +7.7) |
| RoadRunner | Disagreement, 30% floor | 1 | 0.73 (0.52-0.84) | 0.82 (0.61-0.91) | 81% | +1.9 (-26.7 to +12.8) |
| RoadRunner | Motion x disagreement | 1 | 0.69 (0.48-0.82) | 0.77 (0.57-0.88) | 94% | +5.6 (-17.5 to +13.2) |
| RoadRunner | Motion x disagreement, 30% floor | 1 | 0.73 (0.53-0.84) | 0.82 (0.63-0.91) | 88% | -9.7 (-22.7 to +0.6) |
| RoadRunner | Oracle (not deployable) | 1 | 0.52 (0.21-0.71) | 0.58 (0.24-0.77) | 100% |  |
| RoadRunner | Random | 2 | 0.73 (0.54-0.83) |  |  |  |
| RoadRunner | Motion | 2 | 0.62 (0.38-0.76) | 0.85 (0.67-0.93) | 88% |  |
| RoadRunner | Predicted error (visual + disagreement) | 2 | 0.83 (0.71-0.89) | 1.15 (1.06-1.42) | 28% |  |
| RoadRunner | Oracle (not deployable) | 2 | 0.45 (0.14-0.66) | 0.62 (0.24-0.80) | 100% |  |
| RoadRunner | Random | 4 | 0.56 (0.36-0.68) |  |  |  |
| RoadRunner | Motion | 4 | 0.47 (0.20-0.66) | 0.85 (0.52-0.98) | 88% |  |
| RoadRunner | Predicted error (visual + disagreement) | 4 | 0.70 (0.54-0.79) | 1.26 (1.13-1.72) | 22% |  |
| RoadRunner | Oracle (not deployable) | 4 | 0.32 (0.10-0.47) | 0.57 (0.27-0.70) | 100% |  |
| Seaquest | Random | 1 | 0.73 (0.67-0.79) |  |  | +10.1 (-4.0 to +22.7) |
| Seaquest | Motion | 1 | 0.65 (0.56-0.75) | 0.90 (0.77-1.04) | 50% | +12.2 (-27.2 to +57.5) |
| Seaquest | Disagreement | 1 | 0.56 (0.47-0.68) | 0.77 (0.65-0.93) | 75% | -21.6 (-35.5 to -4.8) |
| Seaquest | Predicted error (visual) | 1 | 0.70 (0.64-0.77) | 0.97 (0.93-1.00) | 53% | +8.2 (-8.4 to +23.3) |
| Seaquest | Predicted error (visual + disagreement) | 1 | 0.63 (0.55-0.73) | 0.86 (0.77-0.97) | 56% | -5.6 (-16.0 to +4.5) |
| Seaquest | Disagreement, 30% floor | 1 | 0.61 (0.49-0.71) | 0.83 (0.69-0.95) | 78% | -15.1 (-27.8 to +2.0) |
| Seaquest | Motion x disagreement | 1 | 0.56 (0.47-0.68) | 0.77 (0.66-0.91) | 56% | -0.4 (-25.8 to +23.3) |
| Seaquest | Motion x disagreement, 30% floor | 1 | 0.56 (0.46-0.68) | 0.77 (0.64-0.91) | 66% | -3.2 (-21.4 to +17.1) |
| Seaquest | Oracle (not deployable) | 1 | 0.19 (0.15-0.26) | 0.27 (0.21-0.35) | 100% |  |
| Seaquest | Random | 2 | 0.61 (0.55-0.68) |  |  |  |
| Seaquest | Motion | 2 | 0.51 (0.42-0.61) | 0.83 (0.67-1.00) | 69% |  |
| Seaquest | Predicted error (visual + disagreement) | 2 | 0.43 (0.36-0.54) | 0.70 (0.59-0.85) | 78% |  |
| Seaquest | Oracle (not deployable) | 2 | 0.14 (0.11-0.20) | 0.23 (0.18-0.30) | 100% |  |
| Seaquest | Random | 4 | 0.36 (0.29-0.47) |  |  |  |
| Seaquest | Motion | 4 | 0.27 (0.21-0.36) | 0.73 (0.62-0.86) | 75% |  |
| Seaquest | Predicted error (visual + disagreement) | 4 | 0.27 (0.21-0.35) | 0.73 (0.65-0.82) | 84% |  |
| Seaquest | Oracle (not deployable) | 4 | 0.11 (0.08-0.15) | 0.30 (0.25-0.35) | 100% |  |

**Against random gaze, over games** (clearly better: CI below 1; clearly worse: CI above 1)

| Gaze | Patches/frame | Games | Clearly better | Clearly worse | Geometric mean ratio |
|---|---|---|---|---|---|
| Motion | 1 | 8 | 6 | 0 | 0.78 |
| Motion | 2 | 8 | 8 | 0 | 0.73 |
| Motion | 4 | 8 | 7 | 0 | 0.65 |
| Disagreement | 1 | 8 | 7 | 0 | 0.71 |
| Predicted error (visual) | 1 | 8 | 4 | 0 | 0.91 |
| Predicted error (visual + disagreement) | 1 | 8 | 6 | 0 | 0.79 |
| Predicted error (visual + disagreement) | 2 | 8 | 7 | 1 | 0.74 |
| Predicted error (visual + disagreement) | 4 | 8 | 7 | 1 | 0.70 |
| Disagreement, 30% floor | 1 | 8 | 7 | 0 | 0.75 |
| Motion x disagreement | 1 | 8 | 7 | 0 | 0.68 |
| Motion x disagreement, 30% floor | 1 | 8 | 7 | 0 | 0.73 |
| Oracle (not deployable) | 1 | 8 | 8 | 0 | 0.39 |
| Oracle (not deployable) | 2 | 8 | 8 | 0 | 0.36 |
| Oracle (not deployable) | 4 | 8 | 8 | 0 | 0.42 |
