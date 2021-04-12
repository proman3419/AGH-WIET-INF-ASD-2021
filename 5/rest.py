from math import inf


def rest(N, T):
  n = len(N)
  F = [[inf for _ in range(T+1)] for _ in range(n)]

  for i in range(n):
    N[i][0] = 0


N = [1, 5, 8]
T = 15
