"""Módulo com a função do método gauss-jacobi."""
import math


def norma(arr):
    """Calcua a norma do vetor."""
    soma = 0
    for i in range(len(arr)):
        soma += arr[i] * arr[i]
    norma = math.sqrt(soma)
    return norma


def gauss_jacobi(A, b, n, e):
    """Executa as iterações."""
    x = []
    X = []
    nint = 0
    for k in range(n):
        X.append(1)
        x.append(0)
    while(nint < 10000):
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * X[j] / A[i][i]
                x[i] = ((b[i]/A[i][i]) - soma)
        if abs(norma(x) - norma(X)) < e:
            return X
        else:
            X = x[:]
        nint += 1
    return X
