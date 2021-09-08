from math import inf
from collections import deque


def bin_search(A, x):
  n = len(A)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if A[c] < x:
      l = c + 1
    elif A[c] > x:
      r = c - 1
    else:
      while c > 0 and A[c-1] == x:
        c -= 1
      break

  if A[c] != x:
    return None
  return c


def generate_graph(cities, lines):
  n = len(cities)
  graph = [[0 for _ in range(n)] for _ in range(n)]

  for u, v, w in lines:
    u = bin_search(cities, u)
    v = bin_search(cities, v)
    if u is not None and v is not None:
      graph[u][v] = w

  return graph


def copy_graph(graph, _graph, n):
  for i in range(n):
    for j in range(n):
      _graph[i][j] = graph[i][j]


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


def dfs_am(graph, s):
  n = len(graph)
  visited = [False]*n
  time = 0

  def dfs_visit(u):
    nonlocal graph, visited, time, n

    time += 1
    visited[u] = True

    for v in range(n):
      if graph[u][v] != 0 and not visited[v]:
        dfs_visit(v)

    time += 1

  dfs_visit(s)

  return visited


def sabotage(cities, lines):
  n = len(cities)
  cities.sort()
  graph = generate_graph(cities, lines)
  _graph = [[0 for _ in range(n)] for _ in range(n)]
  copy_graph(graph, _graph, n)

  A = bin_search(cities, 'A')
  B = bin_search(cities, 'B')
  min_cut_val = ford_fulkerson(_graph, A, B)

  # po wykonaniu forda_fulkersona graf jest siecia rezidualna.
  # wszystkie wierzcholki, ktore mozna osiagnac ze zrodla poprzez jakas sciezke w sieci rezidualnej
  # naleza do jednego zbioru, te ktore nie do drugiego.
  # krawedzie, ktore istnialy w grafie poczatkowym laczace te dwa zbiory naleza do min cuta

  visited = dfs_am(_graph, A)

  min_cut_edges = []
  for i in range(n):
    if visited[i]:  
      for j in range(n):
        if not visited[j] and graph[i][j] > 0:
          min_cut_edges.append([i, j, graph[i][j]])

  return (min_cut_val, min_cut_edges)


cities = ['A', 'B', 'C', 'D', 'E']

lines = [['A', 'D', 3],
         ['A', 'C', 4],
         ['D', 'E', 3],
         ['C', 'E', 2],
         ['C', 'B', 3],
         ['E', 'B', 2]]

# (5, [[2, 1, 3], [4, 1, 2]])
print(sabotage(cities, lines))
