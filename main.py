import gauss_jacobi as gj
n = int(input().strip())
A = []
b = []
for i in range(n):
    A.append([int(i) for i in input().strip().split()])

b += [int(i) for i in input().strip().split()]
e = float(input().strip())

print(gj.gauss_jacobi(A, b, n, e))
