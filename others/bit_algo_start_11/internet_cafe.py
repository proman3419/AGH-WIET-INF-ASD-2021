from math import inf
from collections import deque


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
        queue.append(v)

  return visited[e]


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


def create_graph(Z, K, A, C):
  n = K + A + 2 # 2 na SZ i SU
  graph = [[0 for _ in range(n)] for _ in range(n)]
  # indeksowanie w grafie:
  # - SZ -> -2
  # - SU -> -1
  # - Aplikacje -> 0..A
  # - Komputery -> A..A+K

  for i in range(A):
    graph[-2][i] = graph[i][-2] = Z[i]
    for j in C[i]:
      graph[i][A+j] = graph[A+j][i] = 1

  for i in range(A, A+K):
    graph[-1][i] = graph[i][-1] = 1

  return graph


def internet_cafe(Z, K, A, C):
  graph = create_graph(Z, K, A, C)

  return ford_fulkerson(graph, -2, -1) == sum(Z)


Z = [2, 1, 1] # Z[i] zapotrzebowanie na ita aplikacje
K = 4 # ilosc komputerow
A = 3 # ilosc aplikacji
C = [[0], [2, 1], [3]] # lista kompatybilnosci aplikacji z komputerami

# False
print(internet_cafe(Z, K, A, C))
