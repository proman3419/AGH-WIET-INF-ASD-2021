from zad1testy import runtests
from math import inf


def zbigniew( A ):
  n = len(A)

  # zeby nie miec energii zaleznej od sumy energii
  for i in range(n):
    to_end = (n - 1) - i
    if A[i] > to_end:
      A[i] = to_end

  # F[i][e] - min liczba skokow by dotrzec do i z zapasem e energii
  # mozemy e ograniczyc przez n poniewaz gdy mamy >= n - 1 energii to w 1 skoku mozemy osiagnac cel
  F = [[inf for e in range(n)] for i in range(n)]

  F[0][A[0]] = 0

  for i in range(1, n):
    for e in range(A[i], n):
      for prev_i in range(i):
        prev_e = e + (i - prev_i) - A[i]
        if 0 <= prev_e < n:
          F[i][e] = min(F[i][e], F[prev_i][prev_e]+1)

  return min(F[-1])
       

runtests( zbigniew ) 
