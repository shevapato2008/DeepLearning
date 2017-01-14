import numpy as np
from scipy.stats import multivariate_normal as mvn
import matplotlib.pyplot as plt

cov = np.array([[1, 0.8], [0.8, 3]])
mu = np.array([0, 2])
mu

r = mvn.rvs(mean = mu, cov = cov, size = 1000)
plt.scatter(r[:, 0], r[:, 1])

r = np.random.multivariate_normal(mean = mu, cov = cov, size = 1000)
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')