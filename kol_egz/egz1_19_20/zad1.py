from zad1testy import runtests
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
        if graph[u][v] > 0 and (parents[u] is None or graph[parents[u]][u] != graph[u][v]):
          curr_dist = distances[u] + graph[u][v]
          if curr_dist < distances[v]:
            parents[v] = u
            distances[v] = curr_dist
            queue.put((distances[v], v))

      processed[u] = True

  print(get_path(distances, parents, e))

  return distances[e]


def islands(G, A, B):
  return dijkstra(G, A, B)
        

runtests( islands ) 
