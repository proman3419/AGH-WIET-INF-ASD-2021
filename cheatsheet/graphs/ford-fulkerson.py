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


# 23
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

# print(ford_fulkerson(graph, 0, 5))

# 5
graph = [[0, 8, 3, 0, 0, 0],
         [0, 0, 0, 9, 0, 0],
         [0, 0, 0, 7, 4, 0],
         [0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0]]

# print(ford_fulkerson(graph, 0, 5))

# 19
graph = [[0, 10, 10, 0, 0, 0],
         [0, 0, 2, 4, 8, 0],
         [0, 0, 0, 0, 9, 0],
         [0, 0, 0, 0, 0, 10],
         [0, 0, 0, 6, 0, 10],
         [0, 0, 0, 0, 0, 0]]

print(ford_fulkerson(graph, 0, 5))
