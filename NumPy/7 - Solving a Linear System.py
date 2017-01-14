import numpy as np
A = np.array([[1, 2], [3, 4]])
A
b = np.array([1, 2])
b

x = np.linalg.inv(A).dot(b)
x

x = np.linalg.solve(A, b)		# always use solve() method: more efficient and accurate
x