from math import inf


def rest(N, T):
  n = len(N)
  # F[i][j] - minimalna ilosc monet potrzebnych do uzyskania wartosci j
  # przy zalozeniu, ze mozemy korzystac tylko z monet o nominalach do i-tego
  F = [[inf for _ in range(T+1)] for _ in range(n)]

  for i in range(n):
    F[i][0] = 0

  for i in range(1, (T+1)//N[0]):
    F[0][i*N[0]] = i

  for i in range(1, n):
    for j in range(1, T+1):
      F[i][j] = min(F[i-1][j], F[i][j-N[i]] + 1)

  _min = F[0][T]
  for i in range(1, n):
    if F[i][T] < _min:
      _min = F[i][T]

  return _min


N = [1, 5, 4, 8]
T = 11

print(rest(N, T))
