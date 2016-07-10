import gauss_jacobi_seidel as gj
import matriz_inversa as mi


print("valor de n:")
n = int(input().strip())
A = []
b = []
for i in range(n):
    print("digite os elementos da linha", i+1, "da matriz A separados por espaço")
    A.append([int(i) for i in input().strip().split()])
print("digite os elementos de b separados por espaço")
b += [int(i) for i in input().strip().split()]
print("digite o valor da precisão")
e = float(input().strip())
inv = mi.inversa(A)
d = []
soma = 0
print("\n\n Matriz Inversa")
for i in range(len(inv)):
    print(inv[i])
for i in range(len(inv[0])):
    for j in range(len(inv)):
        soma += inv[i][j] * b[j]
    d.append(soma)
    soma = 0
print("\nd = A^(-1) * b => d =", d)
print("\nGauss-Jacobi", gj.gauss_jacobi(A, b, n, e))
print("\nGauss-Seidel", gj.gauss_seidel(A, b, n, e))
