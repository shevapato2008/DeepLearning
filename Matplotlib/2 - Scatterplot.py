import pandas as pd
import matplotlib as plt
import numpy as np

A = pd.read_csv('data_1d.csv', header = None).as_matrix()
x = A[:, 1]
x = A[:, 0]
y = A[:, 1]
plt.scatter(x, y)

x_line = np.linspace(0, 100, 100)
y_line = 2*x_line + 1
plt.scatter(x_line, y_line)