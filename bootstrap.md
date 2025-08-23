# Bootstrap Variance Estimation

Bootstrap is a resampling method. Instead of relying on linearization, it estimates variance by repeatedly resampling and recalculating the statistic.

### Steps:
1. Resample clusters (PSUs) with replacement.
2. Compute the statistic of interest (e.g., mean).
3. Repeat many times (e.g., 500+ iterations).
4. Compute variance across replicates.

## Stata
See [`stata/bootstrap.do`](stata/bootstrap.do)

## Python
See [`python/bootstrap.py`](python/bootstrap.py)
