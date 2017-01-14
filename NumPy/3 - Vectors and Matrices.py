import numpy as np
M = np.array([[1, 2], [3, 4]])
M

L = [[1, 2], [3, 4]]
L

L[0]
L[0][0]
M[0][0]
M[0, 0]				# equivalent but simpler

M2 = np.matrix([[1, 2], [3, 4]])
M2
A = np.array(M2)
A
A.T					# Array can do the same thing as matrix.
					# It is not recommended to use matrix.