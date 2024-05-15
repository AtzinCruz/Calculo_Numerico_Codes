from scipy.optimize import newton
import numpy as np
import os

# Definir la función cuyas raíces se van a encontrar
def funcion(x):
    return -x**3 + 6*x**2 + 15*x + 8

os.system('cls')

# Aproximación inicial para el método de Newton-Raphson
x0 = float(input('Ingresa la aproximación inicial: '))

# Llamada a la función newton para encontrar la raíz de la función
resultado = newton(funcion, x0)

# Imprimir el resultado
print()
print("La raíz aproximada es:", resultado)
print()
