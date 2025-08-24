# Simple Random Sampling (SRS)

In **Simple Random Sampling (SRS)**, every unit in the population has the same probability of being selected.  
Variance estimation is straightforward, using the standard formula for the variance of the sample mean.

## Formula
For a sample of size `$n$`:
```math
Var(\bar{y}) = \frac{s^2}{n}

where $s^2$ is the sample variance.

## Example (Stata)
See [`stata/srs.do`](stata/srs.do)

## Example (Python)
See [`python/srs.py`](python/srs.py)
