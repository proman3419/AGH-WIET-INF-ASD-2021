from math import inf


def find_cheapest_path(A):
  m = len(A)
  n = len(A[0])

  # F[i][j] - najtanszy koszt dotarcia do pola A[i][j]
  F = [[inf for _ in range(n)] for _ in range(m)]
  F[0][0] = A[0][0]

  for i in range(1, m):
    F[i][0] = F[i-1][0] + A[i][0]

  for i in range(1, n):
    F[0][i] = F[0][i-1] + A[0][i]    

  for i in range(1, m):
    for j in range(1, n):
      F[i][j] = min(F[i-1][j], F[i][j-1]) + A[i][j]

  return F[-1][-1]


A = [[3, 1, 4, 2, 3, 1, 7],
     [2, 4, 5, 2, 1, 4, 2],
     [3, 1, 5, 4, 2, 3, 1],
     [4, 1, 8, 3, 4, 1, 1],
     [1, 2, 3, 7, 3, 4, 1],
     [1, 2, 4, 2, 2, 3, 2],
     [3, 4, 1, 3, 1, 4, 1]]

print(find_cheapest_path(A))
