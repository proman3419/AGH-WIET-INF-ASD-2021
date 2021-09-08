from math import inf
from collections import deque


def dfs_am(graph, s):
  n = len(graph)
  visited = [False]*n
  time = 0

  def dfs_visit(u):
    nonlocal graph, visited, time, n

    time += 1
    visited[u] = True

    for v in range(n):
      if graph[u][v] == 1 and not visited[v]:
        dfs_visit(v)

    time += 1

  dfs_visit(s)

  return visited


def bfs(graph, s, e, parents):
  n = len(graph)
  queue = deque()
  visited = [False]*n

  visited[s] = True
  queue.append(s)

  while queue:
    u = queue.popleft()
    for v in range(n):     
      if graph[u][v] > 0 and not visited[v]:
        visited[v] = True
        parents[v] = u

        if v == e:
          return True

        queue.append(v)

  return False


# O(V*E^2)
def ford_fulkerson(graph, src, sink):
  parents = [None]*len(graph)
  max_flow = 0

  while bfs(graph, src, sink, parents):
    curr_flow = inf
    
    v = sink
    while v != src:
      curr_flow = min(curr_flow, graph[parents[v]][v])
      v = parents[v]

    max_flow += curr_flow

    v = sink
    while v != src:
      u = parents[v]
      graph[u][v] -= curr_flow
      graph[v][u] += curr_flow
      v = parents[v]

  return max_flow


def copy_graph(graph, _graph, n):
  for i in range(n):
    for j in range(n):
      _graph[i][j] = graph[i][j]


# If the algorithm doesn't work check the previous version
# O(V^2*E^2)
def find_edge_connectivity(graph):
  n = len(graph)

  for v in dfs_am(graph, 0):
    if v != True:
      return 0

  _graph = [[0 for _ in range(n)] for _ in range(n)]

  k = inf
  s = 0
  for e in range(n):
    if e != s:
      copy_graph(graph, _graph, n)
      k = min(k, ford_fulkerson(_graph, s, e))

  return k


# 1
graph = [[0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 1, 0]]

# 0
graph = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]]

# 2
graph = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]]

print(find_edge_connectivity(graph))
