import numpy as np

a = np.array([1, 2])
b = np.array([2, 1])
dot = 0
for e, f in zip(a, b):
    dot += e * f;

dot

zip(a, b)       # zip() convert n lists / arrays into n-tuples

a * b           # a * b is not dot product. It only gives element-wise multiplications.

np.sum(a * b)   # if you add them up then it is equivalent to dot product

(a * b).sum()   # equivalent
np.dot(a, b)    # the numpy dot product function
a.dot(b)        # equivalent
b.dot(a)        # equivalent

# try to get norm of a using dot product of a and itself
amag = np.sqrt((a * a).sum())
amag
amag = np.linalg.norm(a)  # numpy norm() function under linalg library
amag

# calculate angle between a and b vectors
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
cosangle
angle = np.arccos(cosangle)
angle