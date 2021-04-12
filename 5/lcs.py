def find_lcs(A, B, n):
  F = [[0 for _ in range(n+1)] for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, n+1):
      if A[i-1] == B[j-1]:
        F[i][j] = F[i-1][j-1] + 1
      else:
        F[i][j] = max(F[i-1][j], F[i][j-1])

  return F[n][n]


A = [1, 2, 3, 2, 5, 6]
B = [1, 2, 3, 5, 6, 10]
n = len(A)

print(find_lcs(A, B, n))
