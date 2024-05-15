def gauss_jordan(A, b):
    n = len(b)
    
    # Concatenar matriz A con vector b
    M = [A[i] + [b[i]] for i in range(n)]

    # Eliminación hacia adelante
    for i in range(n):
        # Encontrar la fila con el pivote más grande en la columna actual
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
        # Intercambiar la fila actual con la fila con el pivote más grande
        M[i], M[max_row] = M[max_row], M[i]

        # Manejar el caso cuando el pivote es cero
        if M[i][i] == 0:
            raise ValueError("El pivote es cero. No se puede resolver el sistema.")

        # Hacer que el pivote sea 1
        pivot = M[i][i]
        for j in range(i, n + 1):
            M[i][j] /= pivot
        # Hacer ceros debajo del pivote
        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(i, n + 1):
                    M[k][j] -= factor * M[i][j]

    # Soluciones
    solutions = [M[i][n] for i in range(n)]
    return solutions

# Ejemplo de uso
A = [[3, 2, 4],
     [2, 0, 2],
     [4, 2, 3]]

b = [0, 0, 0]

try:
    soluciones = gauss_jordan(A, b)
    print("Soluciones:", soluciones)
except ValueError as e:
    print(e)