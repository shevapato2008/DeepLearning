import numpy as np
A = np.array([[1, 2], [3, 4]])
Ainv = np.linalg.inv(A)		# matrix inverse
Ainv
Ainv.dot(A)
A.dot(Ainv)

np.linalg.det(A)		# matrix determination
np.diag(A)
np.diag([1, 2])

a = np.array([1, 2])
b = np.array([3, 4])
np.outer(a, b)			# outer product
np.inner(a, b)			# inner product
a.dot(b)				# inner product = dot product

np.trace(A)				# trace
np.diag(A).sum()		# check

X = np.random.randn(100, 3)
cov = np.cov(X)			# covariance matrix: wrong way
cov.shape
cov = np.cov(X.T)		# covariance matrix: right way. Need to put in the transpose form.
cov

np.linalg.eigh(cov)		# eigenvalue & eigenvectors of a nXn matrix
np.linalg.eig(cov)		# eigenvalue & eigenvectors of a general matrix