from math import inf


def bin_search(A, x):
  n = len(A)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if A[c] < x:
      l = c + 1
    elif A[c] > x:
      r = c - 1
    else:
      while c > 0 and A[c-1] == x:
        c -= 1
      break

  if A[c] != x:
    return None
  return c


def get_path(parents, min_dist, t, min_f_i):
  if min_dist == inf:
    return None

  if parents[t][min_f_i] is None:
    return []

  path = []
  _v = (t, min_f_i)
  while _v is not None:
    v, f = _v
    path.append(v)
    _v = parents[v][f]

  return path[::-1]


# obliczyc minimalny koszt tankowan, zeby dojechac do t, na kazdej stacji mozna tankowac tylko do pelna
def tank_b2(L, S, P, n, t):
  # F[i][f] - minimalny koszt, zeby dostac sie do i-tego pola z f paliwa
  F = [[inf]*(L+1) for _ in range(t+1)]
  parents = [[None]*(L+1) for _ in range(t+1)]

  F[0][L] = 0 # startujemy na 0 z pelnym bakiem

  for i in range(1, t+1):
    for prev_i in range(i):
      dist = i - prev_i
      for f in range(L-dist+1):
        s_i = bin_search(S, i)
        if F[prev_i][f+dist] < F[i][f]:
          F[i][f] = F[prev_i][f+dist]
          parents[i][f] = (prev_i, f+dist)

        if s_i is not None:
          new_cost = F[prev_i][f+dist] + P[s_i]*(L-f)
          if new_cost < F[i][L]:
            F[i][L] = new_cost
            parents[i][L] = (prev_i, f+dist)

  min_f_i = 0
  for f in range(L+1):
    if F[t][f] < F[t][min_f_i]:
      min_f_i = f

  return (F[t][min_f_i], get_path(parents, F[t][min_f_i], t, min_f_i))


# zakladam, ze stacje sa w posortowanej kolejnosci

# (29, [0, 7, 15, 23]
S = [2, 7, 12, 15, 20] # odleglosci stacji od punktu 0
P = [4, 3, 10, 1, 4] # koszty paliw na poszczegolnych stacjach
L = 10 # pojemnosc baku
t = 23 # pole, do ktorego chcemy dojechac

# (18, [0, 3, 6, 9])
S = [2, 3, 6]
P = [4, 3, 3]
L = 3
t = 9

# (2, [0, 2, 20])
S = [2, 4, 8, 9, 15, 18]
P = [1, 1, 1, 1, 1, 2]
L = 19
t = 20

# (inf, None)
S = [2, 4, 8, 9, 15, 18]
P = [1, 1, 1, 1, 1, 2]
L = 4
t = 20

# (2.9, [0, 1, 2, 4, 6])
S = [1, 2, 3, 4]
P = [0.9, 1, 0.9, 0.5]
L = 2
t = 6

n = len(S) # ilosc stacji
print(tank_b2(L, S, P, n, t))
