# Survey Variance Estimation

Understanding how survey design affects variance is essential for correct statistical inference.  
Complex surveys rarely resemble simple random samples. Instead, they often use **stratification, clustering, and unequal probabilities of selection**. These features alter the sampling variability:

- If you **ignore design** and only apply weights, you often **underestimate standard errors** in clustered designs or sometimes **overestimate them** in well-executed stratification.
- Correctly declaring the design ensures valid **SEs, confidence intervals, p-values**, and clear **documentation**.

---

## Why Survey Design Matters for Variance

- **Weights (pweight):** Inverse of selection probability × adjustments (nonresponse, post-stratification).  
  Affect both point estimates and variance.  
- **Strata:** Groups sampled independently. Typically reduce variance. Must always be declared.  
- **Clusters / PSUs:** Primary sampling units (e.g., schools, enumeration areas). They induce intra-cluster correlation, inflating variance.  
- **FPC (Finite Population Correction):** Applied when sampling fraction is large (not negligible).  

---

## Variance Estimation Approaches

- **Taylor linearization (default in Stata’s `svy:`):**  
  Analytic approximation using residuals across PSUs.  
- **Replicate weights (BRR, JK1/JK2, bootstrap):**  
  Compute estimates repeatedly across replicates, then combine results.  
- **Single-unit strata:** Strata with only one PSU in the sample require explicit handling (e.g., centered variance, scaled variance, certainty PSU).  

---

## Key Resources in This Repo

- [Simple Random Sampling](srs.md) – baseline case, intuition.  
- [Complex Designs](complex_designs.md) – stratification, clustering, weights.  
- [Practical Issues](issues.md) – singletons, FPCs, software defaults.  
- [Bootstrap & Replication](bootstrap.md) – bootstrap, jackknife, BRR.  

Code examples:  
- **Stata:** [`stata/`](stata/)  
- **Python:** [`python/`](python/)  

