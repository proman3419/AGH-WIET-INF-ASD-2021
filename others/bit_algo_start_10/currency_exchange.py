from math import inf, log


def get_path(distances, parents, v):
  if distances[v] == inf:
    return None

  if parents[v] is None:
    return []

  path = []

  while v is not None:
    path.append(v)
    v = parents[v]

  return path[::-1]


# True - posiada ujemny cykl
# False - nie
def verification(graph, distances):
  for u, v, w in graph:
    if distances[v] > distances[u] + log(w):
      return True

  return False


def bellman_ford(graph, s, e, max_v):
  n = len(graph)
  distances = [inf]*(max_v+1)
  parents = [None]*(max_v+1)

  distances[s] = 0

  for i in range(max_v-1):
    for u, v, w in graph:
      # zamieniamy na na log, zeby operowac na +/- zamiast *//
      curr_dist = distances[u] + log(w)

      if curr_dist < distances[v]:
        distances[v] = curr_dist
        parents[v] = u

  if verification(graph, distances):
    return (None, True)

  return (get_path(distances, parents, e), False)


def currency_exchange(T, A, B):
  n = len(T)
  max_v = max(max(e[0], e[1]) for e in T)

  path, has_negative_cycle = bellman_ford(T, A, B, max_v)

  print(f'1: {path}')
  print(f'2: {has_negative_cycle}')

# 1: None
# 2: True
T = [(0, 1, 4.49),
     (0, 2, 4.00),
     (2, 0, 0.25),
     (1, 2, 0.75),
     (3, 2, 100),
     (0, 3, 0.4)]

# currency_exchange(T, 0, 3)

# 1: [0, 1]
# 2: False
T = [(0, 1, 1),
     (1, 0, 1)]

# currency_exchange(T, 0, 1)

# 1: None
# 2: True
T = [(0, 1, 1),
     (1, 2, 0.5),
     (2, 3, 0.25),
     (3, 0, 0.125)]

# currency_exchange(T, 0, 3)

# dwa cykle ujemne
# 1: None
# 2: True
T = [(0, 1, 1),
     (1, 2, 0.5),
     (2, 0, 0.25),
     (2, 3, 1),
     (3, 4, 0.5),
     (4, 5, 0.25),
     (5, 3, 0.125)]

# currency_exchange(T, 0, 5)

# {0: PLN, 1: EUR, 2: USD, 3: CHF, 4: GBP}
# 1: [4, 0, 1, 3]
# 2: False
T = [(0, 1, 4.4838),
     (0, 2, 3.6774),
     (0, 4, 5.2179),
     (1, 2, 1.2142),
     (1, 3, 1.0960),
     (2, 4, 1.420029),
     (3, 4, 1.282),
     (4, 0, 0.23)]

# currency_exchange(T, 4, 3)

# nie jestem pewien czy do konca poprawne, ciezko pisac rozbudowane testy
# bez cykli ujemnych
