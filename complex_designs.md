# Complex Survey Designs

In practice, surveys use stratification, clustering, and weights. Variance estimation must take these into account.  

### Key elements:
- **Weights:** adjust for unequal probabilities of selection.
- **Strata:** improve precision by ensuring subgroup representation.
- **Clusters (PSUs):** often increase variance due to intra-cluster correlation.

## Stata
Use `svyset` with weight, strata, and PSU variables.  
See [`stata/complex.do`](stata/complex.do)

## Python
Use `statsmodels`'s `SurveyDesignSpec`.  
See [`python/complex.py`](python/complex.py)
