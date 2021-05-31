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


def bellman_ford(graph, s, e, max_v):
  distances = [inf]*(max_v+1)
  parents = [None]*(max_v+1)
  prev_ws = [inf]*(max_v+1)

  distances[s] = 0

  for u, v, w in graph:
    curr_dist = distances[u] + w

    if curr_dist < distances[v] and prev_ws[u] != w:
      distances[v] = curr_dist
      parents[v] = u
      prev_ws[v] = w

  return (get_path(distances, parents, e), distances[e])


# zal graf nieskierowany
def decreasing_edges_path(graph, x, y):
  graph.sort(key=lambda x: x[2], reverse=True)
  max_v = max(max(e[0], e[1]) for e in graph)

  return bellman_ford(graph, x, y, max_v)


# ([0, 2, 4, 3], 12)
graph = [[0, 1, 10],
         [0, 2, 5],
         [1, 0, 10],
         [1, 2, 1],
         [1, 3, 3],
         [1, 4, 2],
         [2, 0, 5],
         [2, 1, 1],
         [2, 3, 6],
         [2, 4, 4],
         [3, 1, 3],
         [3, 2, 6],
         [3, 4, 3],
         [3, 5, 2],
         [4, 1, 2],
         [4, 2, 4],
         [4, 3, 3],
         [4, 5, 1],
         [5, 3, 2],
         [5, 4, 1]]

# print(decreasing_edges_path(graph, 0, 3))

# ([0, 3, 2], 7)
graph = [[0, 1, 10],
         [1, 2, 10],
         [0, 3, 4],
         [3, 2, 3]]

# print(decreasing_edges_path(graph, 0, 2))

# ([0, 1, 6, 5, 4, 3, 2], 39)
graph = [[0, 1, 9],
         [1, 0, 9],
         [1, 2, 10],
         [1, 6, 8],
         [2, 1, 10],
         [2, 3, 4],
         [3, 2, 4],
         [3, 4, 5],
         [4, 3, 5],
         [4, 5, 6],
         [5, 4, 6],
         [5, 6, 7],
         [6, 2, 8],
         [6, 5, 7]]

# print(decreasing_edges_path(graph, 0, 2))

# ([0, 2, 3, 4, 5], 10)
graph = [[0, 1, 2],
         [0, 2, 4],
         [1, 0, 2],
         [1, 2, 10],
         [1, 4, 12],
         [1, 5, 100],
         [2, 0, 4],
         [2, 1, 10],
         [2, 3, 3],
         [3, 2, 3],
         [3, 4, 2],
         [4, 3, 2],
         [4, 1, 12],
         [4, 5, 1],
         [5, 1, 100],
         [5, 4, 1]]

print(decreasing_edges_path(graph, 0, 5))
