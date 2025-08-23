# Common Issues in Variance Estimation

### 1. Single PSU per stratum
Some strata may only have one sampling unit. This causes variance estimation to fail or underestimate variance.

**Solutions:**
- **Centering:** Use the stratum mean.
- **Linearization tricks:** Adjust with finite population correction.
- **Bootstrap:** Resample clusters.

See [`stata/singleton.do`](stata/singleton.do) for Stata examples.

---

### 2. Weights not declared
If weights are ignored, estimates may be biased and variance underestimated.  
Always declare survey weights in Stata (`svyset`) or Python (`SurveyDesignSpec`).
