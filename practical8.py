import numpy as np
def gram_schmidt(vectors):
    ortho = []
    for v in vectors:
        w = v.copy()
        for u in ortho:
            w = w - (np.dot(v, u) / np.dot(u, u)) * u
        ortho.append(w)
    # Normalize
    ortho_norm = [u / np.linalg.norm(u) for u in ortho]
    return ortho_norm

# Example vectors
V = [
    np.array([1, 1, 0], dtype=float),
    np.array([1, 0, 1], dtype=float),
    np.array([0, 1, 1], dtype=float)
]

basis = gram_schmidt(V)
print("Orthonormal Basis:")
for b in basis:
    print(b) 
