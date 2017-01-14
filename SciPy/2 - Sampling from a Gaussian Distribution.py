import matplotlib.pyplot as plt
import numpy as np

r = np.random.randn(10000)
plt.hist(r, bins = 100)
r = 10 * np.random.randn(10000) + 5
plt.hist(r, bins = 100)

r = np.random.randn(10000, 2)
plt.scatter(r[:, 0], r[:, 1])
plt.show()

r[:, 1] = 5 * r[:, 1] + 2
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')

