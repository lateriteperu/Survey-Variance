import numpy as np
import statsmodels.api as sm

# Simulated data
n = 200
strata = np.repeat([1,2,3,4], n//4)
cluster = np.repeat(np.arange(n//10), 10)
weight = np.random.uniform(0.5, 2, n)
y = np.random.normal(100, 15, n)

# Declare survey design
design = sm.survey.SurveyDesignSpec(strata=strata, cluster=cluster, weights=weight)

# Estimate mean
est = sm.survey.SurveyMean(design, y)
print("Mean:", est.mean)
print("Variance:", est.var)
