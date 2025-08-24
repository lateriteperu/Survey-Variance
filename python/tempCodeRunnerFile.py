import numpy as np

# Simulated data
y = np.random.normal(50, 10, 100)

# Sample mean
mean_y = np.mean(y)

# Variance of mean under SRS
var_mean = np.var(y, ddof=1) / len(y)

print("Mean:", mean_y)
print("Variance of mean:", var_mean)