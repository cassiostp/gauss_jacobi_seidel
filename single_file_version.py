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
    maxint = 100000  # número máximo de iterações
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
    maxint = 100000
    for k in range(n):
        X.append(1)
        x.append(0)
    while nint < maxint:
        for i in range(0, n, 1):
            soma = 0
            for j in range(0, i, 1):
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

# some helpers
def id_matriz(tamanho):
    id = []
    for i in range(tamanho):
        id.append([0]*tamanho)
    for i in range(tamanho):
        id[i][i] = 1
    return(id)


def transposta(inMtx):
    tMtx = []
    for row in range(0, len(inMtx[0])):
        tRow = []
        for col in range(0, len(inMtx)):
            ele = inMtx[col][row]
            tRow.append(ele)
        tMtx.append(tRow)
    return(tMtx)


def matriz_round(matx):
    for col in range(len(matx)):
        for row in range(len(matx[0])):
            matx[col][row] = round(matx[col][row], 5)


def inversa(A, decPts=4):

  identidade = id_matriz(len(A))
  A_plus_id = A[:]
  for col in range(len(identidade)):
    A_plus_id.append(identidade[col])
  transposta_Aid = transposta(A_plus_id)
  m = transposta_Aid[:]

  (eqns, colrange, augCol) = (len(A), len(A), len(m[0]))

  # coloca os maiores elementos nas diagonais
  # assume x[1,1] como maior elemento e troca caso contrário
  for col in range(0, colrange):
    bigrow = col
    for row in range(col+1, colrange):
      if abs(m[row][col]) > abs(m[bigrow][col]):
        bigrow = row
        (m[col], m[bigrow]) = (m[bigrow], m[col])

  for rrcol in range(0, colrange):
    for rr in range(rrcol+1, eqns):
      cc = -(float(m[rr][rrcol])/float(m[rrcol][rrcol]))
      for j in range(augCol):
        m[rr][j] = m[rr][j] + cc*m[rrcol][j]

  for rb in reversed(range(eqns)):
      for backCol in reversed(range(rb, augCol)):
        m[rb][backCol] = float(m[rb][backCol]) / float(m[rb][rb])

      for kup in reversed(range(rb)):
        for kleft in reversed(range(rb, augCol)):
          kk = -float(m[kup][rb]) / float(m[rb][rb])
          m[kup][kleft] += kk*float(m[rb][kleft])

  mOut = []
  for row in range(len(m)):
    rOut = []
    for col in range(int(augCol/2), augCol):
      rOut.append(m[row][col])
    mOut.append(rOut)
  return transposta(mOut)

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
inv = inversa(A)
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
print("\nGauss-Jacobi", gauss_jacobi(A, b, n, e))
print("\nGauss-Seidel", gauss_seidel(A, b, n, e))
