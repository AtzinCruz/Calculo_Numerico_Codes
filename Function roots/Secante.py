import sympy as sp
import os

# Definir la función a usar
def funcion(x):
    return -x**3 + 6*x**2 + 15*x + 8

# Definir la función para el método de secante
def secante(x0, x1, tol, max_iter):
    x = sp.Symbol('x') 
    f = funcion(x)  
    
    iteracion = 0
    prev_x_next = None  
    
    while iteracion < max_iter:
        x_next = x1 - (f.subs(x, x1) * (x1 - x0)) / (f.subs(x, x1) - f.subs(x, x0))
        
        error_relativo = abs((x_next - prev_x_next) / x_next) if prev_x_next else "N/A"
        
        print("Iteración", iteracion + 1, "- Aproximación:", x_next, "- Error relativo:", error_relativo)
        
        if abs(x_next - x1) < tol:
            return x_next
        
        x0 = x1
        x1 = x_next
        prev_x_next = x_next  
        iteracion += 1
    
    print("El método de la secante no convergió.")
    return None

os.system('cls')

# Solicita al usuario las dos aproximaciones iniciales
x0 = float(input('Ingresa la primera aproximación inicial: '))
x1 = float(input('Ingresa la segunda aproximación inicial: '))
print()

tolerancia = 1e-6  # Define la tolerancia para el criterio de convergencia
max_iteraciones = 1000000  # Define el número máximo de iteraciones

# Aplica el método de la secante
resultado = secante(x0, x1, tolerancia, max_iteraciones)

# Imprime el resultado
if resultado is not None:
    print()
    print("La raíz aproximada es:", resultado)
    print()
else:
    print()
    print("El método de la secante no convergió.")
    print()
