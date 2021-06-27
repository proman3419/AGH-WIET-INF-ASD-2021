from math import inf


def frog(A):
  n = len(A)

  # F[i][e] - min liczba skokow by dotrzec do i z zapasem e energii
  # mozemy e ograniczyc przez n poniewaz gdy mamy >= n energii to w 1 skoku mozemy osiagnac cel
  F = [[inf for e in range(n+1)] for i in range(n)]

  for i in range(min(A[0]+1, n+1)):
    F[0][i] = 0

  def rec(i, e):
    nonlocal A, F

    if F[i][e] != inf:
      return F[i][e]

    for k in range(i):
      _e = min(e+(i-k)-A[i], n)
      if e >= i-k and 0 <= _e <= n:
        F[i][e] = min(F[i][e], rec(k, _e)+1)

    return F[i][e]

  _min = inf
  for e in range(n+1):
    _min = min(_min, rec(n-1, e))

  return _min


# 3
A = [1, 2, 3, 4, 5]

# 3
A = [1, 2, 2, 2, 2, 2]

# inf
A = [2, 2, 1, 0, 0, 0]

# 2
A = [4, 5, 2, 5, 1, 2, 1, 0]

# 4
A = [2, 2, 1, 0, 0]

print(frog(A))
