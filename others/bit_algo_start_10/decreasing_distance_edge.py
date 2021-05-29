from math import inf

# floyd-warshall
# relaksacja dla kazdej z E'

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


def decreasing_distance_edge(G, E, s, t):
  distances = floyd_warshall(G)

  _min_dist = inf
  _min_e = None
  for u, v, w in E:
    curr_dist = distances[s][u] + w + distances[v][t]
    if distances[s][t] > curr_dist:
      if curr_dist < _min_dist:
        _min_dist = curr_dist
        _min_e = [u, v]

  return _min_e


G = [[0, 10, 0, 0],
     [0, 0, 0, 2],
     [10, 0, 0, 5],
     [0, 0, 0, 0]]

E = [[2, 1, 2]]

print(decreasing_distance_edge(G, E, 2, 3))
