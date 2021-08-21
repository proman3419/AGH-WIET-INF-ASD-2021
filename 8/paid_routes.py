from queue import PriorityQueue
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


def get_min_v(distances, processed, n):
  _min = inf
  _min_v = None

  for v in range(n):
    if not processed[v] and distances[v] < _min:
      _min = distances[v]
      _min_v = v

  return _min_v


# O(V^2)
def dijkstra_am(graph, s, t):
  n = len(graph)
  processed = [False]*n
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0
  u = s

  while u is not None:
    if not processed[u]:
      for v in range(n):
        if graph[u][v] > 0:
          curr_dist = distances[u] + graph[u][v]

          if curr_dist < distances[v]:
            parents[v] = u
            distances[v] = curr_dist

      processed[u] = True

    u = get_min_v(distances, processed, n)   

  return get_path(distances, parents, t)


# nadpisujemy graf tak, zeby platne drogi mialy wage n**2 + 1 czyli
# wiecej niz jakbysmy przeszli wszystkimi darmowymi krawedziami dla grafu pelnego,
# dzieki temu darmowe beda priorytetyzowane
def modify_graph(graph):
  n = len(graph)
  m = n**2 + 1

  for u in range(n):
    for v in range(n):
      if graph[u][v] == 2:
        graph[u][v] = m

  return graph


def paid_routes(graph, s, t):
  graph = modify_graph(graph)

  return dijkstra_am(graph, s, t)


# droga:
# 0 - brak, 1 - darmowa, 2 - platna

# [0, 2, 4, 3]
graph = [[0, 2, 1, 0, 0],
         [0, 0, 0, 2, 0],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0]]
s = 0; t = 3

# [0, 2, 3, 1]
graph = [[0, 2, 1, 0],
         [2, 0, 0, 1],
         [1, 0, 0, 1],
         [0, 1, 1, 0]]
s = 0; t = 1

# [0, 6, 5, 3]
graph = [[0, 1, 0, 0, 2, 0, 1], 
         [1, 0, 2, 0, 0, 0, 0], 
         [0, 2, 0, 2, 0, 0, 0], 
         [0, 0, 2, 0, 2, 1, 0], 
         [2, 0, 0, 2, 0, 0, 0], 
         [0, 0, 0, 1, 0, 0, 2], 
         [1, 0, 0, 0, 0, 2, 0]]
s = 0; t = 3

print(paid_routes(graph, s, t))
