def bricks(A):
  n = len(A)
  # F[i] - dlugosc najdluzszego podciagu klockow takiego, ze kazdy klocek zawiera sie
  # w poprzednich i konczy na klocku i-tym
  F = [1]*n

  for i in range(1, n):
    for j in range(i):
      if A[j][0] <= A[i][0] and A[i][1] <= A[j][1]:
        F[i] = max(F[i], F[j] + 1)

  return n - max(F)


# 1
A = [(0, 4), (3, 10), (5, 6)]

# 2
A = [(0, 4), (3, 10), (5, 6), (1, 4), (1, 3)]

print(bricks(A))
