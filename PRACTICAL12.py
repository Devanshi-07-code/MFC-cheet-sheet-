import sympy as sp

x, y, z = sp.symbols('x y z')
P = x*y**2
Q = sp.sin(x*z)
R = sp.exp(y*z)
divF = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)
print("Vector field F = (P,Q,R):", (P, Q, R))
print("Divergence ∇·F =", sp.simplify(divF))





SSS