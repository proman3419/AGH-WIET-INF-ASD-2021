from math import inf


def mentos(A):
  n = len(A)

  # F[i][j] - max sumaryczny zysk dla przedzialu [i, j] zakladajac, ze
  # gracze graja optymalnie
  F = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n-1):
    F[i][i] = A[i]
    F[i][i+1] = max(A[i], A[i+1])
  F[n-1][n-1] = A[n-1]

  def calculate_profits(i, j):
    nonlocal A, F

    if F[i][j] != 0:
      return F[i][j]

    i_i = i_j = j_i = j_j = inf
    if i + 2 < n: i_i = F[i+2][j]
    if i + 1 < n and j - 1 >= 0: i_j = j_i = F[i+1][j-1]
    if j - 2 >= 0: j_j = F[i][j-2]

    F[i][j] = max(A[i] + min(i_i, i_j), A[j] + min(j_i, j_j))

  for j in range(2, n):
    for i in range(n-j):
      calculate_profits(i, j+i)

  return F[0][-1]


A = [1, 7, 2, 4, 3, 4]
print(mentos(A))
