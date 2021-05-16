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

  for r in F:
    print(r)

  for l in range(2, n):
    for i in range(n-l):
      j = i + l
      for k in range(i+1, j):
        print(F[i][k], F[k][j], abs(subsums[j]-subsums[i]+A[i]))
        F[i][j] = min(max(F[i][k], F[k][j]), abs(subsums[j]-subsums[i]+A[i]))

  return F[0][-1]


# 3
# A = [1, -5, 2]

# 4
# A = [1, -5, 2, -1, 7]

# 2
A = [2, 4, -2, -4]

print(opt_sum(A))
