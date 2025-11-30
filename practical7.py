import numpy as np

# Vectors
v1 = np.array([1,2,3])
v2 = np.array([2,4,6])
v3 = np.array([1,0,1])

A = np.column_stack((v1,v2,v3))
print("Dependent" if np.linalg.matrix_rank(A)<3 else "Independent")

# Linear combination
print(2*v1 - v2 + 3*v3)

# Transition matrix (new basis made of given vectors)
P = np.column_stack((v1,v3,v2))
print(P)
