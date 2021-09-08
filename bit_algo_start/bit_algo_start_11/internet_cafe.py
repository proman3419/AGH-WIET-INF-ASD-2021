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
def ford_fulkerson(graph, src, sink, A, K):
  parents = [None]*len(graph)
  max_flow = 0
  pc_app_disposal = [None]*K

  while bfs(graph, src, sink, parents):
    curr_flow = inf
    
    v = sink
    while v != src:
      curr_flow = min(curr_flow, graph[parents[v]][v])
      if A <= v < A+K:
        pc_app_disposal[v-A] = parents[v]
      v = parents[v]

    max_flow += curr_flow

    v = sink
    while v != src:
      u = parents[v]
      graph[u][v] -= curr_flow
      graph[v][u] += curr_flow
      v = parents[v]

  return pc_app_disposal

def create_graph(Z, K, A, C):
  n = K + A + 2 # 2 na SZ i SU
  graph = [[0 for _ in range(n)] for _ in range(n)]
  # indeksowanie w grafie:
  # - SZ -> -2
  # - SU -> -1
  # - Aplikacje -> 0..A
  # - Komputery -> A..A+K

  for i in range(A):
    graph[-2][i] = Z[i]
    for j in C[i]:
      graph[i][A+j] = 1

  for i in range(A, A+K):
    graph[i][-1] = 1

  return graph


def verify(pc_app_disposal, Z, K):
  for i in range(K):
    if pc_app_disposal[i] is not None:
      Z[pc_app_disposal[i]] -= 1

  for e in Z:
    if e > 0:
      return False

  return True


def internet_cafe(Z, K, A, C):
  graph = create_graph(Z, K, A, C)
  pc_app_disposal = ford_fulkerson(graph, -2, -1, A, K)

  if verify(pc_app_disposal, Z, K):
    return pc_app_disposal
  else:
    return None


# [0, 0, 1, 2]
Z = [2, 1, 1] # Z[i] - zapotrzebowanie na ita aplikacje
C = [[0, 1], [2], [3]] # C[i][j] - ita aplikacja moze byc zainstalowana na jtym komputerze
A = len(C) # ilosc aplikacji
K = 4 # ilosc komputerow
# print(internet_cafe(Z, K, A, C))

# None
Z = [0, 1, 2, 1, 0, 0]
C = [[0, 1], [3], [0, 1, 2, 3], [3], [3], [0]]
A = len(C)
K = 4
# print(internet_cafe(Z, K, A, C))

# [1, 2, 2, 3]
Z = [0, 1, 2, 1, 0, 0]
C = [[0, 1], [0, 3], [0, 1, 2, 3], [3], [1, 3], [0]]
A = len(C)
K = 4
# print(internet_cafe(Z, K, A, C))

# [1, 2, 2, 3, 5, 5]
Z = [0, 1, 2, 1, 0, 2]
C = [[0, 1], [0, 3], [0, 1, 2, 3], [3], [1, 3], [0, 4, 5]]
A = len(C)
K = 6
print(internet_cafe(Z, K, A, C))

# None
Z = [0, 1, 2, 1, 0, 2]
C = [[0, 1], [3], [0, 1, 2, 3], [3], [3], [0, 4, 5]]
A = len(C)
K = 6
# print(internet_cafe(Z, K, A, C))

# None
Z = [0, 1, 2, 1, 0, 1]
C = [[0, 1], [3], [0, 1, 2, 3], [3], [3], [0]]
A = len(C)
K = 4
# print(internet_cafe(Z, K, A, C))
