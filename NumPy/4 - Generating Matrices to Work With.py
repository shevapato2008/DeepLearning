import numpy as np
np.array([1, 2, 3])

Z = np.zeros(10)
Z

Z = np.zeros((10, 10))
Z

O = np.ones((10, 10))
O

R = np.random.random((10, 10))
R

G = np.random.randn((10, 10))   # wrong

G = np.random.randn(10, 10)
G
G.mean()
G.var()
