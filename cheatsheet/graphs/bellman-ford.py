from math import inf


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

# ==============================================================================

# czy posiada ujemny cykl
def verification_am(graph, distances):
  n = len(graph)
  for u in range(n):
    for v in range(n):
      if graph[u][v] != 0:
        if distances[v] > distances[u] + graph[u][v]:
          return True

  return False


# O(V^3)
def bellman_ford_am(graph, s):
  n = len(graph)
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0

  for i in range(n-1):
    for u in range(n):
      for v in range(n):
        curr_dist = inf
        if graph[u][v] != 0:
          curr_dist = distances[u] + graph[u][v]

          if curr_dist < distances[v]:
            distances[v] = curr_dist
            parents[v] = u

  if verification_am(graph, distances):
    return None

  # print(get_path(distances, parents, n-1))

  return distances


# [0, 5, 5, 7, 9, 8]
graph_am = [[0, 0, 10, 0, 0, 8],
            [0, 0, 0, 2, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, -2, 0, 0, 0],
            [0, -4, 0, -1, 0, 0],
            [0, 0, 0, 0, 1, 0]]

# None
# graph_am = [[0, -1, -1],
#             [-1, 0, 0],
#             [1, 0, 0]]

print(bellman_ford_am(graph_am, 0))

# ==============================================================================

# czy posiada ujemny cykl
def verification_ml(graph, distances):
  n = len(graph)
  for u in range(n):
    for v, w in graph[u]:
      if distances[v] > distances[u] + w:
        return True

  return False


# O(V*E)
def bellman_ford_ml(graph, s):
  n = len(graph)
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0

  for i in range(n-1):
    for u in range(n):
      for v, w in graph[u]:
        curr_dist = distances[u] + w

        if curr_dist < distances[v]:
          distances[v] = curr_dist
          parents[v] = u

  if verification_ml(graph, distances):
    return None

  # print(get_path(distances, parents, n-1))

  return distances


# [0, 5, 5, 7, 9, 8]
graph_ml = [[[5, 8], [2, 10]],
            [[3, 2]],
            [[1, 1]],
            [[2, -2]],
            [[1, -4], [3, -1]],
            [[4, 1]]]

# None
# graph_ml = [[[1, -1], [2, -1]], 
#             [[0, -1]],
#             [[0, 1]]]

# None
# graph_ml = [[[1, -4]],
#             [[2, -5]],
#             [[0, -2]],
#             [[4, 2]],
#             [[2, 1]]]

print(bellman_ford_ml(graph_ml, 0))
