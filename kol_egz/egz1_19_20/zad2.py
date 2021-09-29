from zad2testy import runtests
from math import inf


def opt_sum(A):
  n = len(A)

  # F[i][j] - min abs subsuma dodajac liczby od i do j indeksu
  F = [[inf for _ in range(n)] for _ in range(n)]

  for i in range(n-1):
    F[i][i] = abs(A[i])
    F[i][i+1] = abs(A[i] + A[i+1])
  F[n-1][n-1] = abs(A[n-1])

  subsums = [0]*n
  subsums[0] = A[0]
  for i in range(1, n):
    subsums[i] = subsums[i-1] + A[i]

  def rec(i, j):
    nonlocal A, F, subsums

    if F[i][j] == inf:
      a = rec(i + 1, j)
      b = rec(i, j - 1)
      _sum = subsums[j] - subsums[i] + A[i]
      F[i][j] = max(abs(_sum), min(a, b))

    return F[i][j]

  rec(0, n-1)

  return F[0][-1]


runtests( opt_sum )
