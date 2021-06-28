from zad2testy import runtests


# szukamy najdluzszego podciagu rosnacego z kryterium zawierania


# O(n^2)
def lis(A):
  n = len(A)
  # F[i] - dlugosc najwyzszej wiezy konczacej sie na A[i]
  F = [1]*n
  P = [-1]*n

  for i in range(1, n):
    for j in range(i):
      if (A[j][0] <= A[i][0] and A[i][1] <= A[j][1]) and F[j] + 1 > F[i]:
        F[i] = F[j] + 1
        P[i] = j

  max_h = 0
  for i in range(n):
    if max_h < F[i]:
      max_h = F[i]

  return max_h


# O(n^2)
def tower(A):
  n = len(A)

  return lis(A)


runtests( tower )
