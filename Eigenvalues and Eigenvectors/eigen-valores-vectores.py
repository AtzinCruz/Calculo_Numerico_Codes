import numpy as np

A = np.array([[3, 2, 4],
              [2, 0, 2],
              [4, 2, 3]])

lambda_val = -1 
lambda_I = lambda_val * np.eye(A.shape[0])
eigenvalues, eigenvectors = np.linalg.eig(A)
lambda_indices = np.where(np.isclose(eigenvalues, lambda_val, atol=1e-8))[0]

if len(lambda_indices) == 0:
    print("No se encontraron eigenvectores para el eigenvalor", lambda_val)
else:
    for idx in lambda_indices:
        desired_eigenvector = eigenvectors[:, idx]
        print("El eigenvector correspondiente al eigenvalor", eigenvalues[idx], "es:", desired_eigenvector)

        result = np.dot(A - lambda_val * np.eye(A.shape[0]), desired_eigenvector)
        print("Resultado de (A - lambda * I) * v:", result)
