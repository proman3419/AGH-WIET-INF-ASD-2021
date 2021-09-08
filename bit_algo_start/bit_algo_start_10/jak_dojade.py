from math import inf


def get_path(distances, parents, v, f):
  if distances[v][f] == inf:
    return None

  if parents[v][f] is None:
    return []

  path = []

  _v = (v, f)
  while _v is not None:
    v, f = _v
    path.append(v)
    _v = parents[v][f]

  return path[::-1]


def get_min_v(distances, processed, n, d):
  _min = inf
  _min_v = None

  for v in range(n):
    for f in range(d+1):
      if (not processed[v][f]) and (distances[v][f] < _min):
        _min = distances[v][f]
        _min_v = (v, f)

  return _min_v


# O(V^2)
def dijkstra_am(graph, P, d, s, e):
  n = len(graph)
  processed = [[False]*(d+1) for _ in range(n)]
  distances = [[inf]*(d+1) for _ in range(n)]
  parents = [[None]*(d+1) for _ in range(n)]
  stations = [True if v in P else False for v in range(n)] # O(n^2)

  distances[s][d] = 0
  _u = (s, d)

  while _u is not None:
    u, f = _u
    if not processed[u][f]:
      for v in range(n):
        if graph[u][v] != -1 and f >= graph[u][v]:
          curr_dist = distances[u][f] + graph[u][v]

          if stations[v]:
            new_f = d
          else:
            new_f = f - graph[u][v]

          if curr_dist < distances[v][new_f]:
            parents[v][new_f] = _u
            distances[v][new_f] = curr_dist

      processed[u][f] = True

    _u = get_min_v(distances, processed, n, d)    

  min_dist_f_i = 0
  for f in range(1, d+1):
    if distances[e][f] < distances[e][min_dist_f_i]:
      min_dist_f_i = f

  return get_path(distances, parents, e, min_dist_f_i)


# O((V*d)^2)
def jak_dojade(G, P, d, a, b):
  return dijkstra_am(G, P, d, a, b)


G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]
P = [0, 1, 3]

# [0, 3, 2]
print(jak_dojade(G, P, 5, 0, 2))

# [0, 1, 2]
print(jak_dojade(G, P, 6, 0, 2))

# None
print(jak_dojade(G, P, 3, 0, 2))

G = [[-1, 5, -1, 2],
     [-1, -1, -1, -1],
     [5, -1, -1, 5],
     [2, 2, -1, -1]]
P = [2, 0]

# [2, 0, 3, 1]
print(jak_dojade(G, P, 6, 2, 1))
