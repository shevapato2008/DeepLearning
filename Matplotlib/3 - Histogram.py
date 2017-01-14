import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

A = pd.read_csv('data_1d.csv', header = None).as_matrix()
x = A[:, 0]
y = A[:, 1]
plt.hist(x)

R = np.random.random(10000)
plt.hist(R)

plt.hist(R, bins = 20)

y_actual = 2 * x + 1
residuals = y - y_actual
plt.hist(residuals)