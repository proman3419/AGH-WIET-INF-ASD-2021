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

  return path


def dijkstra(graph, s, e):
  n = len(graph)
  queue = PriorityQueue()
  processed = [False]*n
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0
  queue.put((distances[s], s))

  while not queue.empty():
    u = queue.get()[1]

    if not processed[u]:
      for v in range(n):
        if graph[v][u] > 0:
          if parents[u] is None or graph[v][u] > graph[u][parents[u]]:
            curr_dist = distances[u] + graph[v][u]

            if curr_dist < distances[v]:
              parents[v] = u
              distances[v] = curr_dist
              queue.put((distances[v], v))

      processed[u] = True

  return get_path(distances, parents, e)


def decreasing_edges_path(graph, x, y):
  return dijkstra(graph, y, x)


# zal graf nieskierowany
graph = [[0, 10, 5, 0, 0, 0],
         [10, 0, 1, 3, 2, 0],
         [5, 1, 0, 6, 4, 0],
         [0, 3, 6, 0, 3, 2],
         [0, 2, 4, 3, 0, 1],
         [0, 0, 0, 2, 1, 0]]

x = 0
y = len(graph) - 1

print(decreasing_edges_path(graph, x, y))
