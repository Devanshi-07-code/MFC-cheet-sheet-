import sympy as sp

C = sp.Matrix([[1, 3, -9, 0],
               [6, 3, -1, 0],
               [3, 4, -3, 0]])
print("Matrix C:\n", C)

rrefC, pivots = C.rref()
print("RREF of C:\n", rrefC)
print("Pivots:", pivots)

# Extract nullspace (solutions to C x = 0)
null = C.nullspace()
print("Nullspace basis (solutions of Cx=0):", null)
