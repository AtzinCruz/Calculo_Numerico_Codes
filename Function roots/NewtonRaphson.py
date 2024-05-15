import sympy as sp
import os

# Definición de la función a usar
def funcion(x):
    return -x**3 + 6*x**2 + 15*x + 8

# Definición de la función del método de Newton-Raphson
def newton_raphson(funcion, x0, tol, max_iter):
    x = sp.Symbol('x')  
    f = funcion(x)  
    f_derivada = sp.diff(f, x)
    
    iteracion = 0
    prev_x0 = None  
    
    while iteracion < max_iter:
        f_eval = f.subs(x, x0)
        f_derivada_eval = f_derivada.subs(x, x0) 
        

        print("Iteración", iteracion + 1, "- Aproximación:", x0, "- Error relativo:", abs((x0 - prev_x0) / x0) if prev_x0 else "N/A")
        

        if abs(f_eval) < tol:
            print()
            print("La solución convergió en la iteración", iteracion + 1)
            return x0
        
        if f_derivada_eval == 0:
            print()
            print("La derivada se anula en la iteración", iteracion + 1)
            return None
        

        x0 = x0 - f_eval / f_derivada_eval
        prev_x0 = x0  
        iteracion += 1
    
    print()
    print("El método de Newton-Raphson no convergió en", max_iter, "iteraciones.")
    return None

os.system('cls')

# Aproximación inicial para el método de Newton-Raphson
x0 = float(input('Ingresa la aproximación inicial: '))
print()

tolerancia = 1e-6  # Tolerancia: criterio de convergencia para la raíz
max_iteraciones = 1000000  # Número máximo de iteraciones permitidas

# Llamada al método de Newton-Raphson para encontrar la raíz de la función
resultado = newton_raphson(funcion, x0, tolerancia, max_iteraciones)

# Se imprime el resultado
if resultado is not None:
    print()
    print("La raíz aproximada es:", resultado)
    print()
else:
    print()
    print("El método de Newton-Raphson no convergió.")
    print()
