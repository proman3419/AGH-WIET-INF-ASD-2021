def find_lcs(A, B, n, m):
  # F - najdluzszy wspolny podciag do i-tego indeksu w A oraz j-tego w B
  F = [[0 for _ in range(m+1)] for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      if A[i-1] == B[j-1]:
        F[i][j] = F[i-1][j-1] + 1
      else:
        F[i][j] = max(F[i-1][j], F[i][j-1])

  return (F[n][m], F)


def print_solution(A, B, F, n, m, _len):
  i = n
  j = m
  res = [None]*_len

  while i >= 0 and j >= 0:
    if j > 0 and F[i][j-1] == F[i][j]:
      j -= 1
    elif j <= 0:
      i -= 1
      j = m - 1
    else:
      res[F[i][j]-1] = B[j-1]
      i -= 1
      j -= 1

  for i in range(_len):
    print(res[i], end=' ')
  print()

# 1 2 3 5 6
# A = [1, 2, 3, 2, 5, 6]
# B = [1, 2, 3, 5, 6, 10, 11]

# 1 17 2 5
A = [999, 1, 14, 17, 89, 2, 16, 5, 4]
B = [-1, -7, 1, 3, 17, 2, 5]

n = len(A)
m = len(B)
_len, F = find_lcs(A, B, n, m)
print_solution(A, B, F, n, m, _len)
