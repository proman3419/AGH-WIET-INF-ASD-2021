from math import inf


def bellman_ford(graph, s):
  n = len(graph)
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0

  for i in range(n):
    for u in range(n):
      # for v, w in graph[u]:
      #   curr_dist = distances[u] + w
      for v in range(n):
        curr_dist = inf
        if graph[u][v] != 0:
          curr_dist = distances[u] + graph[u][v]

        if curr_dist < distances[v]:
          distances[v] = curr_dist
          parents[v] = u

  return distances


# [0, 5, 5, 7, 9, 8]
graph = [[[5, 8], [2, 10]],
         [[3, 2]],
         [[1, 1]],
         [[2, -2]],
         [[1, -4], [3, -1]],
         [[4, 1]]]

# [0, 5, 5, 7, 9, 8]
graph = [[0, 0, 10, 0, 0, 8],
         [0, 0, 0, 2, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, -2, 0, 0, 0],
         [0, -4, 0, -1, 0, 0],
         [0, 0, 0, 0, 1, 0]]

print(bellman_ford(graph, 0))
