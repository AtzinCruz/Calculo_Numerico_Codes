import sympy as sp
import os

# Definir la función a interpolar
def funcion(x):
    return sp.ln(x + 1)

# Definir la función de interpolación usando el método de Lagrange
def interpolacion_lagrange(x_values, y_values):
    x = sp.Symbol('x')
    n = len(x_values)
    polinomio = 0
    
    for i in range(n):
        termino = 1
        for j in range(n):
            if j != i:
                termino *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polinomio += y_values[i] * termino
    
    return polinomio

# Función para evaluar el polinomio de Lagrange
def evaluar_polinomio(polinomio, valor):
    return polinomio.subs('x', valor)

os.system('cls')

# Preguntar al usuario si desea usar valores predeterminados o ingresarlos manualmente
modo = input("Selecciona el modo de entrada ('funcion' o 'valores'): ").strip().lower()
print('')

if modo == "funcion":
    # Ingreso manual de valores de X
    cantidad_puntos = int(input("Ingrese la cantidad de puntos: "))
    x_values = []
    for i in range(cantidad_puntos):
        x = float(input(f"Ingrese el valor de x{i}: "))
        x_values.append(x)
    y_values = [funcion(x) for x in x_values]  # Calcula los valores de Y usando la función predeterminada
elif modo == "valores":
    # Ingreso manual de valores de X y Y
    cantidad_puntos = int(input("Ingrese la cantidad de puntos: "))
    x_values = []
    y_values = []
    print('')
    for i in range(cantidad_puntos):
        x = float(input(f"Ingrese el valor de X{i}: "))
        x_values.append(x)
    print('')
    for i in range(cantidad_puntos):
        y = float(input(f"Ingrese el valor de y{i}: "))
        y_values.append(y)
else:
    print("Modo no válido.")
    exit()

# Interpolación usando el polinomio de Lagrange
polinomio = interpolacion_lagrange(x_values, y_values)

# Imprime el polinomio de Lagrange
print("\nPolinomio de Lagrange:")
print(sp.simplify(polinomio))

# Preguntar si desea evaluar el polinomio
evaluar = input("\n¿Desea evaluar el polinomio en un valor? (si/no): ")

if evaluar.lower() == "si":
    valor_evaluar = float(input("Ingrese el valor en el que desea evaluar el polinomio: "))
    resultado_evaluacion = evaluar_polinomio(polinomio, valor_evaluar)
    print("\nEl polinomio evaluado en x =", valor_evaluar, "es aproximadamente:", resultado_evaluacion)
elif evaluar.lower() == "no":
    print("\nNo se evaluó el polinomio.")
else:
    print("\nOpción no válida.")
