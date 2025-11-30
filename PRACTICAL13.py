import sympy as sp

x, y, z = sp.symbols('x y z')
P = y*z
Q = x*z
R = x*y

# Compute curl = (R_y - Q_z, P_z - R_x, Q_x - P_y)
curl = sp.Matrix([sp.diff(R, y) - sp.diff(Q, z),
                  sp.diff(P, z) - sp.diff(R, x),
                  sp.diff(Q, x) - sp.diff(P, y)])
print("Vector field F:", (P, Q, R))
print("Curl ∇×F =", curl)




