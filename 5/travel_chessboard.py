from math import inf


def travel_chessboard(A, n):
  # F[i][j] - minimalny koszt potrzebny by dostac sie
  # na pole (i, j) z pola (0, 0)
  F = [[inf for _ in range(n)] for _ in range(n)]

  # na to pole nie wchodzimy => koszt = 0
  F[0][0] = 0

  for i in range(1, n):
    F[0][i] = F[0][i-1] + A[0][i]
    F[i][0] = F[i-1][0] + A[i][0]

  for i in range(1, n):
    for j in range(1, n):
      F[i][j] = min(F[i-1][j], F[i][j-1]) + A[i][j]

  return F[-1][-1]


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(travel_chessboard(A, len(A)))
