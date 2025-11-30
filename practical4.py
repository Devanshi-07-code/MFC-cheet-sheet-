import numpy as np
import sympy as sp

# Example non-homogeneous system Ax = b
A = sp.Matrix([[1, -2, 3],
               [4, 2, -5],
               [3, 1, 6]])
b = sp.Matrix([2, -4, 7])
print("Solve Ax=b with A:\n", A, "\nb =", b)

# Solve with sympy (exact)
x = A.LUsolve(b)
print("Solution x:", x)

# Example homogeneous system Ax = 0
A2 = sp.Matrix([[1, 2, 3],
                [2, 4, 6],
                [1, 1, 1]])
ns = A2.nullspace()   # nullspace gives basis of solutions
print("\nNullspace basis for A2 (Ax=0):", ns)
