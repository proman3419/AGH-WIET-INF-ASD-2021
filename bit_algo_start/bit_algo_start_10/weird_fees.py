from math import inf


def get_min_v(distances, processed, n):
  _min = inf
  _min_v = None

  for v in range(n):
    if not processed[v] and distances[v] < _min:
      _min = distances[v]
      _min_v = v

  return _min_v


def dijkstra(graph, s, e):
  n = len(graph)
  processed = [False]*n
  distances = [inf]*n

  distances[s] = 0
  u = s

  while u is not None:
    if not processed[u]:
      for v in range(n):
        if graph[u][v] > 0:
          curr_dist = max(distances[u], graph[u][v])

          if curr_dist < distances[v]:
            distances[v] = curr_dist

      processed[u] = True

    u = get_min_v(distances, processed, n)    

  return distances[e]


def weird_fees(graph, s, e):
  return dijkstra(graph, s, e)


graph = [[0, 60, 0, 120, 0],
         [60, 0, 80, 0, 0],
         [0, 80, 0, 0, 70],
         [120, 0, 0, 0, 150],
         [0, 0, 70, 150, 0]]

print(weird_fees(graph, 0, 4))
