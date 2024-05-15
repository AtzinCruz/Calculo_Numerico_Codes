import sympy as sp
import os
from tabulate import tabulate

# Definir la función a interpolar
def funcion(x):
    return sp.ln(x)

# Calcular las diferencias divididas de Newton
def diferencias_divididas_newton(x_vals, y_vals=None, func=None):
    if func is not None:
        n = len(x_vals)
        F = [[None] * n for _ in range(n)]
        for i in range(n):
            F[i][0] = func(x_vals[i])
        for j in range(1, n):
            for i in range(n - j):
                F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_vals[i + j] - x_vals[i])
    elif y_vals is not None:
        n = len(x_vals)
        F = [[None] * n for _ in range(n)]
        for i in range(n):
            F[i][0] = y_vals[i]
        for j in range(1, n):
            for i in range(n - j):
                F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_vals[i + j] - x_vals[i])
    else:
        raise ValueError("Debe proporcionar valores de 'y' o una función")

    return F

# Imprimir la tabla de diferencias divididas
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

# Evaluar el polinomio interpolante de Newton en un punto x
def evaluar_newton(x, x_vals, F):
    n = len(x_vals)
    result = F[0][0]
    polinomio = F[0][0]
    for i in range(1, n):
        term = F[0][i]
        for j in range(i):
            term *= (x - x_vals[j])
        result += term
        polinomio += term
    return result, polinomio

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
        
        # Calcular las diferencias divididas de Newton
        F = diferencias_divididas_newton(x_vals, func=funcion)
        
    if modo == 'valores':
        x_vals = []
        y_vals = []
        
        for i in range(n):
            x = float(input(f'Ingresa el valor de x{i}: '))
            x_vals.append(x)
        print()
        for i in range(n):
            y = float(input(f'Ingresa el valor de y{i}: '))
            y_vals.append(y)
        
        # Calcular las diferencias divididas de Newton
        F = diferencias_divididas_newton(x_vals, y_vals=y_vals)
    
    # Imprimir la tabla de diferencias divididas
    print("\nTabla de diferencias divididas:")
    imprimir_tabla_diferencias(F)
    
    # Evaluar el polinomio interpolante de Newton en un punto dado
    resultado, polinomio = evaluar_newton(sp.Symbol('x'), x_vals, F)
    
    # Simplificar el polinomio interpolante
    polinomio_simplificado = sp.simplify(polinomio)
    
    # Imprimir el polinomio interpolante
    print("\nPolinomio interpolante de Newton:")
    print(polinomio_simplificado)
    
    # Opción de evaluar el polinomio interpolante
    evaluar = input("\n¿Quieres evaluar el polinomio interpolante? (si/no): ")
    if evaluar.lower() == 'si':
        # Solicitar al usuario el punto donde evaluar el polinomio interpolante
        x_eval = float(input('\nIngresa el valor de x donde quieres evaluar el polinomio interpolante: '))
        
        # Evaluar el polinomio interpolante de Newton en el punto dado
        resultado_evaluado = resultado.subs(sp.Symbol('x'), x_eval)
        
        # Imprimir el resultado
        print(f'\nEl valor interpolado en x = {x_eval} es aproximadamente {resultado_evaluado}\n')
    elif evaluar.lower() == 'no':
        print("\nNo se evaluó el polinomio interpolante.\n")
    else:
        print("\nRespuesta no válida.\n")

else:
    print("Modo no válido. Debe ser 'funcion' o 'valores'\n")
