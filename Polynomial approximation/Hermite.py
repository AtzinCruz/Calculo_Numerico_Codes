import sympy as sp
from tabulate import tabulate
import os

# Define la función precargada
def funcion(x):
    return x**3 - 2*x**2 + x + 1

# Función para calcular las diferencias divididas de Hermite
def diferencias_divididas_hermite(x, y, y_prime):
    n = len(x)
    coef = [[None] * (2 * n) for _ in range(2 * n)]
    
    # Fill the first column with pairs of y values
    for i in range(n):
        coef[2*i][0] = y[i]
        coef[2*i + 1][0] = y[i]
    
    # Fill the second column with y' values and calculate the rest of the divided differences
    for j in range(1, 2 * n):
        for i in range(2 * n - j):
            if j == 1 and i % 2 == 0:
                coef[i][j] = y_prime[i//2]
            else:
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[(i + j) // 2] - x[i // 2])
    
    return coef

# Función para imprimir la tabla de diferencias divididas
def imprimir_tabla_diferencias(F):
    headers = [f'Dif. Orden {i}' for i in range(len(F))]
    rows = []
    for j in range(len(F)):
        col = []
        for i in range(len(F[j])):
            if F[j][i] is not None:
                col.append(F[j][i])
            else:
                break
        rows.append(col)
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    
# Función para construir el polinomio interpolante de Hermite
def construir_hermite(x, x_vals, F):
    n = len(x_vals)
    polinomio = 0
    
    for i in range(2 * n):
        termino = F[0][i]
        for j in range(i):
            termino *= (x - x_vals[j // 2])
        polinomio += termino
    
    return polinomio

# Función para evaluar el polinomio interpolante de Hermite en un punto x
def evaluar_hermite(x, polinomio):
    return polinomio.subs(sp.Symbol('x'), x)

os.system('cls')

# Modo de entrada
modo = input("Selecciona el modo de entrada ('funcion' o 'valores'): ").strip().lower()
print()

if modo == 'funcion' or modo == 'valores':        
    # Solicitar al usuario los datos de entrada
    n = int(input('Ingresa el número de puntos de datos: '))
    print()
    
    if modo == 'funcion':
        x_vals = []
        
        for i in range(n):
            x = float(input(f'Ingresa el valor de x{i}: '))
            x_vals.append(x)
        
        # Calcular las diferencias divididas de Hermite
        F = diferencias_divididas_hermite(x_vals, [funcion(x) for x in x_vals], [sp.diff(funcion(x)).evalf() for x in x_vals])
        
    if modo == 'valores':
        x_vals = []
        y_vals = []
        y_prime_vals = []
        
        for i in range(n):
            x = float(input(f'Ingresa el valor de x{i}: '))
            x_vals.append(x)
        print()
        for i in range(n):
            y = float(input(f'Ingresa el valor de y{i}: '))
            y_vals.append(y)
        print()
        for i in range(n):
            y_prime = float(input(f'Ingresa el valor de y\'{i}: '))
            y_prime_vals.append(y_prime)
        
        # Calcular las diferencias divididas de Hermite
        F = diferencias_divididas_hermite(x_vals, y_vals, y_prime_vals)
    
    # Imprimir la tabla de diferencias divididas
    print("\nTabla de diferencias divididas:")
    imprimir_tabla_diferencias(F)

    # Construir el polinomio interpolante de Hermite
    polinomio = construir_hermite(sp.Symbol('x'), x_vals, F)
    
    # Simplificar el polinomio interpolante
    polinomio_simplificado = sp.simplify(polinomio)
    
    # Imprimir el polinomio interpolante
    print("\nPolinomio interpolante de Hermite:")
    print(sp.simplify(polinomio_simplificado))
    
    # Opción de evaluar el polinomio interpolante
    evaluar = input("\n¿Quieres evaluar el polinomio interpolante? (si/no): ")
    if evaluar.lower() == 'si':
        # Solicitar al usuario el punto donde evaluar el polinomio interpolante
        x_eval = float(input('\nIngresa el valor de x donde quieres evaluar el polinomio interpolante: '))
        
        # Evaluar el polinomio interpolante de Hermite en el punto dado
        resultado_evaluado = evaluar_hermite(x_eval, polinomio)
        
        # Imprimir el resultado
        print(f'\nEl valor interpolado en x = {x_eval} es aproximadamente {resultado_evaluado}\n')
    elif evaluar.lower() == 'no':
        print("\nNo se evaluó el polinomio interpolante.\n")
    else:
        print("\nRespuesta no válida.\n")

else:
    print("Modo no válido. Debe ser 'funcion' o 'valores'\n")
