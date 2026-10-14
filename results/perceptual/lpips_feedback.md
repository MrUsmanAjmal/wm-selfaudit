## Feedback measured with LPIPS

Perceptual drift of the model's prediction of each frame (LPIPS to the real frame), with feedback / without, on 16 clips; 95% CI over videos.

| Feedback | Frames | LPIPS without | LPIPS with | Ratio [95% CI] | Clips improved |
|---|---|---|---|---|---|
| Guided gaze | all imagined frames | 0.345 | 0.308 | 0.89 (0.83-0.97) | 75% |
| Guided gaze | within trained length | 0.256 | 0.250 | 0.98 (0.92-1.06) | 62% |
| Guided gaze | beyond trained length | 0.416 | 0.355 | 0.85 (0.77-0.94) | 81% |
| Random gaze | all imagined frames | 0.345 | 0.322 | 0.93 (0.88-1.02) | 62% |
| Random gaze | within trained length | 0.256 | 0.260 | 1.02 (0.96-1.10) | 62% |
| Random gaze | beyond trained length | 0.416 | 0.371 | 0.89 (0.82-1.00) | 69% |
| Oracle gaze (not deployable) | all imagined frames | 0.345 | 0.281 | 0.82 (0.75-0.89) | 94% |
| Oracle gaze (not deployable) | within trained length | 0.256 | 0.222 | 0.87 (0.80-0.94) | 81% |
| Oracle gaze (not deployable) | beyond trained length | 0.416 | 0.329 | 0.79 (0.70-0.88) | 94% |
