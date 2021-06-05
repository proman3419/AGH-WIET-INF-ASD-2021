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


def extend_graph(graph, srcs, sinks):
  n = len(graph)

  graph.append([0]*n)
  graph.append([0]*n)

  n = len(graph)

  srcs.sort()
  sinks.sort()
  i = j = 0

  for k in range(n):
    graph[k].append(0)
    graph[k].append(0)

    if i < len(srcs) and k == srcs[i]:
      graph[-2][k] = inf # SZ
      i += 1

    if j < len(sinks) and k == sinks[j]:
      graph[k][-1] = inf # SU
      j += 1

  return graph


def find_max_flow_multiple_srcs_sinks(graph, srcs, sinks):
  # tworzymy super zrodlo (SZ) i super ujscie (SU), 
  # SZ - przedostatni wierzcholek, SU - ostatni.
  # ustawiamy wagi krawedzi miedzy SZ i zrodlami oraz SU i ujsciami na inf, zeby
  # nie zanieczyszczac wyniku

  graph = extend_graph(graph, srcs, sinks)

  return ford_fulkerson(graph, len(graph)-2, len(graph)-1)


# 9
graph = [[0, 0, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 0, 4, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 5, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

srcs = [0, 1, 2]
sinks = [7, 8]

print(find_max_flow_multiple_srcs_sinks(graph, srcs, sinks))
