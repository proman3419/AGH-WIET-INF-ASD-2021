from math import inf


def floyd_warshall(graph):
  n = len(graph)

  distances = [[inf for _ in range(n)] for _ in range(n)]

  for v in range(n):
    distances[v][v] = 0

  for v in range(n):
    for u in range(n):
      if graph[u][v] != 0:
        distances[u][v] = graph[u][v]

  for k in range(n):
    for v in range(n):
      for u in range(n):
        curr_dist = distances[u][k] + distances[k][v]
        if distances[u][v] > curr_dist:
          distances[u][v] = curr_dist

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
