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


# True - posiada ujemny cykl
# False - nie
def verification(graph, distances):
  n = len(graph)
  for u in range(n):
    for v, w in graph[u]:
      if distances[v] > distances[u] + w:
        return True
    # for v in range(n):
    #   if graph[u][v] != 0:
    #     if distances[v] > distances[u] + graph[u][v]:
    #       return True

  return False


def bellman_ford(graph, vertices_w, s):
  n = len(graph)
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0

  for i in range(n):
    for u in range(n):
      for v, w in graph[u]:
        curr_dist = distances[u] + w + vertices_w[u] + vertices_w[v]

        if curr_dist < distances[v]:
          distances[v] = curr_dist
          parents[v] = u

  return distances


def shortest_paths(graph, vertices_w, s):
  return bellman_ford(graph, vertices_w, s)


# [0, 8, 6, 24, 27, 14]
graph = [[[5, 8], [2, 10]],
         [[3, 2]],
         [[1, 1]],
         [[2, -2]],
         [[1, -4], [3, -1]],
         [[4, 1]]]

vertices_w = [-1, 4, -3, 10, 5, 7]

# print(shortest_paths(graph, vertices_w, 0))

graph = [[[1, 2]],
         [[2, -1]],
         [[3, -1]],
         [[1, 1]]]

vertices_w = [0, 1, 2, 1]

print(shortest_paths(graph, vertices_w, 0))
