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


def dijkstra(graph, P, d, s, e):
  n = len(graph)
  queue = PriorityQueue()
  processed = [False]*n
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0
  queue.put((distances[s], s, d))

  while not queue.empty():
    _, u, curr_d = queue.get()

    if not processed[u]:
      for v in range(n):
        if graph[u][v] > 0 and graph[u][v] <= curr_d:
          curr_dist = distances[u] + graph[u][v]

          if curr_dist < distances[v]:
            parents[v] = u
            distances[v] = curr_dist

            # mozna bin searchem, optymalniej
            if v in P:
              curr_d = d
            else:
              curr_d -= graph[u][v]

            queue.put((distances[v], v, curr_d))

      processed[u] = True

  return get_path(distances, parents, e)


def jak_dojade(G, P, d, a, b):
  return dijkstra(G, P, d, a, b)


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
