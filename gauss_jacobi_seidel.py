"""Módulo com a função dos métodos gauss-jacobi e gauss-seidel."""
import math


def norma(arr):
    """Calcua a norma do vetor."""
    soma = 0
    for i in range(len(arr)):
        soma += arr[i] * arr[i]
    norma = math.sqrt(soma)
    return norma


def gauss_jacobi(A, b, n, e):
    """Executa as iterações gauss-jacobi."""
    x = []
    X = []
    nint = 0  # contador de iterações
    maxint = 1000000  # número máximo de iterações
    for k in range(n):  # laço preenche o vetor X com uma possivel resposta
        X.append(1)
        x.append(0)  # no caso do vetor x, é apenas alocação de índices
    while nint < maxint:
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * X[j] / A[i][i]
                x[i] = ((b[i]/A[i][i]) - soma)  # calcula a iteração
        if abs(norma(x) - norma(X)) < e:  # verifica se a diferença absoluta
            return X  # das normas é menor que a precisão
        else:
            X = x[:]  # X recebe o valor de x para comparar na proxima iteração
        nint += 1  # incrementa o contador
    return X


def gauss_seidel(A, b, n, e):
    """Executa as iterações gauss-seidel."""
    X = []
    x = []
    nint = 0
    maxint = 1000000
    for k in range(n):
        X.append(1)
        x.append(0)
    while nint < maxint:
        for i in range(n):
            soma = 0
            for j in range(i):
                soma += A[i][j] * x[j]
            for j in range(i+1, n, 1):
                soma += A[i][j] * X[j]
        x[i] = (b[i] - soma) / A[i][i]
        if abs(norma(x) - norma(X)) < e:
            return x
        else:
            X = x[:]
        nint += 1
    return x
