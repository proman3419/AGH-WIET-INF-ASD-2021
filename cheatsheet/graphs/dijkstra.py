from queue import PriorityQueue
from math import inf


def get_path(distances, parents, v):
  def get_path_rec(v):
    nonlocal parents, path

    if v == None:
      return

    get_path_rec(parents[v])
    path.append(v)

  if distances[v] == inf:
    return None

  path = []
  get_path_rec(v)

  return path


def djikstra(graph, s):
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
      # for v in range(n):
      #   if graph[u][v] > 0:
        curr_dist = distances[u] + weight
        # curr_dist = distances[u] + graph[u][v]
        if curr_dist < distances[v]:
          # parents[v] = u
          distances[v] = curr_dist
          queue.put((distances[v], v))

      processed[u] = True

  # print(get_path(distances, parents, n-1))

  return distances


# [0, 2, 3, 8, 6, 9]
# [[(neighbor, weight), ...], ...]
graph = [[(1, 2), (2, 4)],
         [(2, 1), (3, 7)],
         [(4, 3)],
         [(5, 1)],
         [(3, 2), (5, 5)],
         []]

# [0, 2, 3, 8, 6, 9]
# 0 - brak krawedzi, >= 1 - waga krawedzi
# graph = [[0, 2, 4, 0, 0, 0],
#          [0, 0, 1, 7, 0, 0],
#          [0, 0, 0, 0, 3, 0],
#          [0, 0, 0, 0, 0, 1],
#          [0, 0, 0, 2, 0, 5],
#          [0, 0, 0, 0, 0, 0]]

# [0, 4, 4, 2, 1, 4]
# graph = [[0, 5, 4, 2, 1, 6],
#          [1, 0, 6, 3, 4, 2],
#          [2, 9, 0, 4, 3, 5],
#          [9, 2, 7, 0, 6, 2],
#          [8, 6, 4, 7, 0, 8],
#          [2, 1, 3, 7, 3, 0]]

# from random import randint
# n = 2000
# rr = (1, n)
# graph = [[0 if i == j else randint(rr[0], rr[1]) for i in range(n)] for j in range(n)]

print(djikstra(graph, 0))