from queue import PriorityQueue
from math import inf


# O(V^2*log(V))
def prim_am(graph):
  n = len(graph)
  queue = PriorityQueue()
  processed = [False]*n
  in_mst = [False]*n
  parents = [None]*n

  u = 0 # poczatkowy wierzcholek
  T = [] # MST
  in_mst[u] = True

  for v in range(n):
    if graph[u][v] != 0:
      queue.put((graph[u][v], v))
      parents[v] = u

  while not queue.empty():
    w, u = queue.get()

    if not in_mst[u]:
      T.append([parents[u], u, w])
      in_mst[u] = True

    if not processed[u]:
      for v in range(n):
        if graph[u][v] != 0:
          if parents[v] is None or graph[u][v] < graph[parents[v]][v]: 
            queue.put((graph[u][v], v))
            parents[v] = u

      processed[u] = True

  if len(T) != n - 1:
    # graf niespojny
    return None
  return T


# [[0, 2, 2], [0, 5, 3], [2, 4, 5], [4, 3, 4], [3, 1, 1]]
graph_am = [[0, 7, 2, 8, 0, 3],
            [7, 0, 0, 1, 0, 0],
            [2, 0, 0, 0, 5, 0],
            [8, 1, 0, 0, 4, 12],
            [0, 0, 5, 4, 0, 6],
            [3, 0, 0, 12, 6, 0]]

# [[0, 6, 1], [6, 3, 1], [3, 2, 2], [2, 1, 3], [3, 4, 3], [6, 5, 5]]
graph_am = [[0, 4, 0, 0, 0, 0, 1],
            [4, 0, 3, 0, 0, 0, 0],
            [0, 3, 0, 2, 0, 0, 10],
            [0, 0, 2, 0, 3, 6, 1],
            [0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 5],
            [1, 0, 10, 1, 0, 5, 0]]

print(prim_am(graph_am))

# ==============================================================================

# O(E*log(V))
# def prim_nl(graph):
#   n = len(graph)
#   queue = PriorityQueue()
#   processed = [False]*n
#   in_mst = [False]*n
#   parents = [None]*n

#   u = 0 # poczatkowy wierzcholek
#   T = [] # MST
#   in_mst[u] = True

#   for v, w in graph[u]:
#     queue.put((w, v))
#     parents[v] = u

#   while not queue.empty():
#     w, u = queue.get()

#     if not in_mst[u]:
#       T.append([parents[u], u, w])
#       in_mst[u] = True

#     if not processed[u]:
#       for v, w in graph[u]:
#         if parents[v] is None or w < graph[parents[v]][v]: 
#           queue.put((graph[u][v], v))
#           parents[v] = u

#       processed[u] = True

#   if len(T) != n - 1:
#     # graf niespojny
#     return None
#   return T
