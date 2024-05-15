def polinomio_hermite(x0, xn, y0, y1, y0_prima, y1_prima):
    """
    Calcula el polinomio de Hermite que interpola los valores y sus derivadas en los puntos x0 y xn.

    Parámetros:
        x0: El primer punto de interpolación.
        xn: El segundo punto de interpolación.
        y0: El valor de la función en x0.
        y1: El valor de la función en xn.
        y0_prima: El valor de la derivada de la función en x0.
        y1_prima: El valor de la derivada de la función en xn.

    Retorno:
        Una cadena que representa el polinomio de Hermite.
    """
    # Paso 1: Calcular el valor de h
    h = xn - x0
    df1 = diferencia_divide(y0, y1, xn, x0)
    df2 = diferencia_divide(df1 , y0_prima, xn, x0)
    df3 = diferencia_divide(y1_prima, df1, xn, x0)
    df4 = diferencia_divide(df3, df2, xn, x0)
    # Paso 2: Calcular los coeficientes de la interpolación
    c0 = y0
    c1 = y0_prima
    c2 = df2
    c3 = df4

    # Paso 3: Construir la expresión del polinomio
    polynomial = f"{c0} + {c1} * (x - {x0}) + {c2} * (x - {x0})**2 + {c3} * (x - {x0})**3"
    
    return polynomial


def diferencia_divide(x0, x1, y0, y1):
    return (x0 - x1)/ (y0 - y1)
# Datos de ejemplo
x0 = -1
xn = 2
y0 = -11
y1 = 14
y0_prima = 4
y1_prima = 5

polynomial = polinomio_hermite(x0, xn, y0, y1, y0_prima, y1_prima)

print("Polinomio de Hermite:")
print(polynomial)
