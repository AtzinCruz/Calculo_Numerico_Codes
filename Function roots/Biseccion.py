import sympy as sp
import os

# Definir la función a usar
def funcion(x):
    return 5*x**3 - 5*x**2 + 6*x - 2

# Definir la función para el método de bisección
def biseccion(a, b, tol, max_iter):
    x = sp.Symbol('x')  # Define el símbolo x
    f = funcion(x)  # Define la función simbólica
    
    # Comprueba si la función cambia de signo en el intervalo [a, b]
    if f.subs(x, a) * f.subs(x, b) >= 0:
        print("La función no cambia de signo en el intervalo dado.")
        return None
    
    iteracion = 0
    prev_raiz = None  # Almacenar la raíz de la iteración anterior
    
    
    while (b - a) / 2.0 > tol and iteracion < max_iter:
        c = (a + b) / 2.0  
        print("Iteración", iteracion + 1, "- Aproximación:", c, "- Error relativo:", abs((c - prev_raiz) / c) if prev_raiz else "N/A")
        
        if f.subs(x, c) == 0:
            break
        
        if f.subs(x, c) * f.subs(x, a) < 0:
            b = c
        else:
            a = c
        
        prev_raiz = c 
        iteracion += 1
        
    return c

os.system('cls')

# Solicita al usuario los límites del intervalo [a, b]
a = float(input('Ingresa el valor del intervalo a: '))
b = float(input('Ingresa el valor del intervalo b: '))
print()

tolerancia = 1e-6  # Define la tolerancia para el criterio de convergencia
max_iteraciones = 1000000  # Define el número máximo de iteraciones

# Aplica el método de bisección
resultado = biseccion(a, b, tolerancia, max_iteraciones)

# Imprime el resultado
if resultado is not None:
    print()
    print("La raíz aproximada es:", resultado)
    print()
else:
    print()
    print("El método de bisección no convergió.")
    print()
