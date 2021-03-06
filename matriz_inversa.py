"""Módulo com função que inverte matrizes"""


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
