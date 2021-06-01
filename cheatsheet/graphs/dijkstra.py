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


# O(V + E*log(V))
def dijkstra_nl(graph, s):
  n = len(graph)
  queue = PriorityQueue()
  processed = [False]*n
  distances = [inf]*n
  # parents = [None]*n

  distances[s] = 0
  queue.put((distances[s], s))

  while not queue.empty():
    u = queue.get()[1]

    if not processed[u]:
      for v, weight in graph[u]:
        curr_dist = distances[u] + weight

        if curr_dist < distances[v]:
          # parents[v] = u
          distances[v] = curr_dist
          queue.put((distances[v], v))

      processed[u] = True

  # print(get_path(distances, parents, n-1))

  return distances


def get_min_v(distances, processed, n):
  _min = inf
  _min_v = None

  for v in range(n):
    if not processed[v] and distances[v] < _min:
      _min = distances[v]
      _min_v = v

  return _min_v


# O(V^2)
def dijkstra_am(graph, s):
  n = len(graph)
  processed = [False]*n
  distances = [inf]*n
  # parents = [None]*n

  distances[s] = 0
  u = s

  while u is not None:
    if not processed[u]:
      for v in range(n):
        if graph[u][v] > 0:
          curr_dist = distances[u] + graph[u][v]

          if curr_dist < distances[v]:
            # parents[v] = u
            distances[v] = curr_dist

      processed[u] = True

    u = get_min_v(distances, processed, n)    

  # print(get_path(distances, parents, n-1))

  return distances


# [0, 2, 3, 8, 6, 9]
# [[(neighbor, weight), ...], ...]
graph_nl = [[(1, 2), (2, 4)],
            [(2, 1), (3, 7)],
            [(4, 3)],
            [(5, 1)],
            [(3, 2), (5, 5)],
            []]

# [0, 2, 3, 8, 6, 9]
# 0 - brak krawedzi, >= 1 - waga krawedzi
graph_am = [[0, 2, 4, 0, 0, 0],
            [0, 0, 1, 7, 0, 0],
            [0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 2, 0, 5],
            [0, 0, 0, 0, 0, 0]]

# [0, 4, 4, 2, 1, 4]
graph_am = [[0, 5, 4, 2, 1, 6],
            [1, 0, 6, 3, 4, 2],
            [2, 9, 0, 4, 3, 5],
            [9, 2, 7, 0, 6, 2],
            [8, 6, 4, 7, 0, 8],
            [2, 1, 3, 7, 3, 0]]

# from random import randint
# n = 2000
# rr = (1, n)
# graph_am = [[0 if i == j else randint(rr[0], rr[1]) for i in range(n)] for j in range(n)]

print(dijkstra_nl(graph_nl, 0))
print(dijkstra_am(graph_am, 0))
