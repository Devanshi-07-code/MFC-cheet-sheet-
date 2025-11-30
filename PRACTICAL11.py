

import sympy as sp

# Step 1: Bana lo variables jinke respect me derivative lena hai
x, y, z = sp.symbols('x y z')

# Step 2: Apna scalar function define kar lo (easy example)
f = x**2 * y + x*sp.sin(z)

# Step 3: Gradient basically teen partial derivatives ka vector hota hai
grad_f = [
    sp.diff(f, x),   # df/dx
    sp.diff(f, y),   # df/dy
    sp.diff(f, z)    # df/dz
]

print("Given Function f =", f)
print("Gradient (∇f) =", grad_f)

# Step 4: Ek point choose kar ke gradient ka value nikal do
pt = (1, 2, 0.5)
grad_func = [sp.lambdify((x, y, z), g, "numpy") for g in grad_f]
value_at_pt = [g(*pt) for g in grad_func]

print("\nGradient at point", pt, "=", value_at_pt)


