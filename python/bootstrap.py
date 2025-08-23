import numpy as np

# Simulated data
y = np.random.normal(60, 12, 100)

# Bootstrap
B = 200
means = []
n = len(y)

for b in range(B):
    sample = np.random.choice(y, n, replace=True)
    means.append(np.mean(sample))

bootstrap_var = np.var(means, ddof=1)

print("Bootstrap Variance:", bootstrap_var)
