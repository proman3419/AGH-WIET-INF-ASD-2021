from queue import PriorityQueue
from math import inf


# O(V^2*log(V))
def prim_am(graph, s=0):
  n = len(graph)
  queue = PriorityQueue()
  in_mst = [False]*n

  in_mst[s] = True # startujemy w s wiec odznaczamy
  T = [] # MST

  for v in range(n):
    if graph[s][v] != 0:
      queue.put((graph[s][v], v, s))

  while not queue.empty():
    w, u, p = queue.get()

    if not in_mst[u]:
      T.append([p, u, w])
      in_mst[u] = True

      if len(T) == n - 1:
        return T

      for v in range(n):
        if graph[u][v] != 0:
          if not in_mst[v]: # jezeli jest juz w MST to krawedzie wychodzace
          # sa w kolecje lub zostaly juz przetworzone
            queue.put((graph[u][v], v, u))

  # graf niespojny
  return None


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
def prim_nl(graph, s=0):
  n = len(graph)
  queue = PriorityQueue()
  in_mst = [False]*n

  in_mst[s] = True # startujemy w s wiec odznaczamy
  T = [] # MST

  for v, w in graph[s]:
    queue.put((w, v, s))

  while not queue.empty():
    w, u, p = queue.get()

    if not in_mst[u]:
      T.append([p, u, w])
      in_mst[u] = True

      if len(T) == n - 1:
        return T

      for v, w in graph[u]:
        if not in_mst[v]: # jezeli jest juz w MST to krawedzie wychodzace
        # sa w kolecje lub zostaly juz przetworzone
          queue.put((w, v, u))

  # graf niespojny
  return None


# [[0, 2, 2], [0, 5, 3], [2, 4, 5], [4, 3, 4], [3, 1, 1]]
graph_nl = [[[1, 7], [2, 2], [3, 8], [5, 3]],
            [[0, 7], [3, 1]],
            [[0, 2], [4, 5]],
            [[0, 8], [1, 1], [4, 4], [5, 12]],
            [[2, 5], [3, 4], [5, 6]],
            [[0, 3], [3, 12], [4, 6]]]

# [[0, 6, 1], [6, 3, 1], [3, 2, 2], [2, 1, 3], [3, 4, 3], [6, 5, 5]]
graph_nl = [[[1, 4], [6, 1]],
            [[0, 4], [2, 3]],
            [[1, 3], [3, 2], [6, 10]],
            [[2, 2], [4, 3], [5, 6], [6, 1]],
            [[3, 3]],
            [[3, 6], [6, 5]],
            [[0, 1], [2, 10], [3, 1], [5, 5]]]

print(prim_nl(graph_nl))
