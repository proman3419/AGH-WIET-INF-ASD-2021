from math import inf


def get_path(distances, _next, u, v):
  if distances[u][v] == inf:
    return None

  if _next[u][v] is None:
    return []

  path = [u]

  while u != v:
    u = _next[u][v]
    path.append(u)

  return path


def floyd_warshall(graph):
  n = len(graph)

  distances = [[inf for _ in range(n)] for _ in range(n)]
  # _next = [[None for _ in range(n)] for _ in range(n)]

  for v in range(n):
    distances[v][v] = 0
    # _next[v][v] = v

  for v in range(n):
    for u in range(n):
      if graph[u][v] != 0:
        distances[u][v] = graph[u][v]
        # _next[u][v] = v

  for k in range(n):
    for v in range(n):
      for u in range(n):
        curr_dist = distances[u][k] + distances[k][v]
        if distances[u][v] > curr_dist:
          distances[u][v] = curr_dist
          # _next[u][v] = _next[u][k]

  # print(f'{get_path(distances, _next, 0, n-1)}\n')

  return distances


# [0, -1, -2, 0]
# [4, 0, 2, 4]
# [5, 1, 0, 2]
# [3, -1, 1, 0]
graph = [[0, 0, -2, 0],
         [4, 0, 3, 0],
         [0, 0, 0, 2],
         [0, -1, 0, 0]]

for r in floyd_warshall(graph):
  print(r)
