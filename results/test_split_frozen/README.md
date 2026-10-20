# Frozen evaluation on the 72 held-out test videos

Here nothing is fit on the test videos. The error predictors, their feature scaling, the shrinkage weight and the sampling rule are fit once on the 40 clips of the 10 quick-start validation videos (`results/main/`), frozen, and applied unchanged to the 72 test videos and to the 16 clips at 2x speed.

```
python src/wm_audit.py analyze --data <wm_audit_data from notebook 06> --train-data <wm_audit_data from notebook 02> --train-cond minecraft --out results/test_split_frozen
```

Main numbers (variance relative to plain uniform sampling, 95% CI over videos):

| Audit | Fit on other test videos | Frozen, fit on 10 separate videos |
|---|---|---|
| Uniform + shrunk CV[visual+disagreement] | 0.64 (0.59-0.69) | **0.69 (0.61-0.78)** |
| Smart + CV[visual+disagreement] | 0.72 (0.63-0.83) | 0.84 (0.71-0.97) |
| Negative control | 1.01 | 1.01 |

Every audit stays exactly unbiased. The shrunk control variate barely changes when frozen, while smart sampling loses part of its gain, so the shrunk version is the one to use on new data. Used on its own as a drift estimate, the frozen regression predictor is off by +70% (CI +48 to +93), which is the point of correcting it with a real patch instead of trusting it.
