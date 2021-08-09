from math import inf


def multiply_matrices(A):
  n = len(A)
  # F[i][j] - min koszt wymnozenia macierzy od i do j
  F = [[0 for _ in range(n)] for _ in range(n)]

  for l in range(2, n):
    for i in range(n-l):
      j = i + l
      F[i][j] = inf
      for k in range(i, j):
        F[i][j] = min(F[i][j], F[i][k] + F[k][j] + A[i]*A[k]*A[j])

  return F[0][n-1]


# 158
# 5x4, 4x6, 6x2, 2x7
# A = [5, 4, 6, 2, 7]

# 124
# 2x3, 3x6, 6x4, 4x5
A = [2, 3, 6, 4, 5]

print(multiply_matrices(A))
