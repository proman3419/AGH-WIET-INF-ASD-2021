from math import inf


def frog(A):
  n = len(A)

  # F[i][e] - min liczba skokow by dotrzec do i z zapasem e energii
  # mozemy e ograniczyc przez n poniewaz gdy mamy >= n energii to w 1 skoku mozemy osiagnac cel
  F = [[inf for _ in range(n)] for _ in range(n)]

  for i in range(A[0]+1):
    F[0][i] = 0

  for i in range(1, A[0]+1):
    for e in range(A[0]+1-i):
      F[i][e] = 1

  for i in range(1, n):
    for e in range(n):
      for k in range(1, i):
        F[i][e] = min(F[i][e], F[i-k][min(max(0, e+k-A[i]), n-k)]) + 1

  return F[n-1][0]



A = [1,2,3,4,5]
# 2
# A = [1,2,2,2,2,2]
# inf
# A = [2,2,1,0,0,0]
# 2
# A = [4,5,2,5,1,2,1,0]

print(frog(A))
