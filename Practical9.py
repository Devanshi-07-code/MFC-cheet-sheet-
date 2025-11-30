import sympy as sp

E = sp.Matrix([[3, 7, 6],
               [0, 9, 0],
               [0, 0, 4]])
print("Matrix E:\n", E)

eigs = E.eigenvects()
print("Eigenvalues and eigenvectors:", eigs)

# Check diagonalizable: number of independent eigenvectors == size
is_diag = E.is_diagonalizable()
print("Diagonalizable?", is_diag)

# If diagonalizable, get P and D
if is_diag:
    P, D = E.diagonalize()
    print("P (eigenvectors):\n", P)
    print("D (diagonal):\n", D)
# Cayley-Hamilton: polynomial p(E) = 0 matrix for characteristic polynomial p
x = sp.symbols('x')
charpoly = E.charpoly(x).as_expr()
print("Characteristic polynomial p(x):", charpoly)
pE = sp.expand(charpoly.subs(x, E))
print("p(E) is:\n", pE)   # should be zero matrix
