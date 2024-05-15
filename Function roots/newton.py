import numpy as np
from scipy.optimize import newton

def f(x):
    return -x**3 + 6*x**2 + 15*x + 8

# Genera valores iniciales en el rango donde esperas encontrar raíces
initial_values = np.linspace(-10, 10, 100)

roots = []
for x0 in initial_values:
    try:
        root = newton(f, x0)
        # Redondea a 5 decimales y guarda solo raíces únicas
        if not any(np.isclose(root, r, atol=1e-5) for r in roots):
            roots.append(root)
    except RuntimeError:  # Ignora los errores de no convergencia
        pass

print(roots)

