from zad1testy import runtests
from collections import deque
from math import inf


# korzen bedzie tak samo odlegly od najdalszych lisci w drzewie.
# puszczamy pierwszy bfs z losowego wierzcholka, zeby znalezc pierwszy taki lisc,
# a nastepnie puszczamy drugiego z tego liscia, zeby znalezc drugi lisc.
# potem porownujemy dystansy od jednego i drugiego i znajdujemy korzen


# O(V + E)
def bfs_nl(graph, s):
  n = len(graph)
  queue = deque()
  visited = [False]*n
  # parents = [None]*n
  distances = [inf]*n

  distances[s] = 0
  visited[s] = True
  queue.append(s)

  max_dist_v = -1
  max_dist = -1

  while queue:
    u = queue.popleft()

    for v in graph[u]:
      if not visited[v]:
        # parents[v] = u
        distances[v] = distances[u] + 1

        if distances[v] > max_dist:
          max_dist_v = v
          max_dist = distances[v]

        visited[v] = True
        queue.append(v)

  return (max_dist_v, distances)


# O(V + E)
def best_root( L ):
  n = len(L)

  x, x_dists = bfs_nl(L, 0)
  a, a_dists = bfs_nl(L, x)
  b, b_dists = bfs_nl(L, a)

  for v in range(n):
    if a_dists[v] == b_dists[v]:
      return v

  return -1


runtests( best_root ) 
