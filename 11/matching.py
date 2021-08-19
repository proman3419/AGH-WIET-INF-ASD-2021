from math import inf
from collections import deque


# wariant max licznosc:
# drzewo jest grafem dwudzielnym, wystarczy zastosowac forda-fulkersona
# na drzewie, w ktorym wszystkie wagi ustawimy na 1 i dodamy superzrodlo oraz superujscie

# wariant max suma wag:
# nie zadziala poniewaz musimy nadpisac wagi krawedzi


def color_bipartite_am(graph, s):
  n = len(graph)
  # None - nieodwiedzony, {0, 1} - kolor
  visited = [None]*len(graph)
  bipartite_flag = True

  def dfs_visit(u, color):
    nonlocal graph, visited, bipartite_flag, n

    visited[u] = color
    for v in range(n):
      if not bipartite_flag:
        return

      if graph[u][v] == 1:
        if visited[v] is not None:
          if visited[v] == color:
            bipartite_flag = False
            return
        else:
          dfs_visit(v, (color+1)%2)

  for u in range(len(graph)):
    if visited[u] is None:
      dfs_visit(u, 0)

  if bipartite_flag:
    return visited

  return None


def extend_graph_ff(graph, srcs, sinks):
  n = len(graph)

  graph.append([0]*n) # SZ
  graph.append([0]*n) # SU

  n = len(graph)

  srcs.sort()
  sinks.sort()
  i = j = 0

  for k in range(n):
    graph[k].append(0)
    graph[k].append(0)

    if i < len(srcs) and k == srcs[i]:
      graph[-2][k] = 1 # SZ
      i += 1

    if j < len(sinks) and k == sinks[j]:
      graph[k][-1] = 1 # SU
      j += 1

  return graph


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


# O(V*E^2)
def find_matching_val(graph):
  n = len(graph)

  for u in range(n):
    for v in range(n):
      if graph[u][v] != 0:
        graph[u][v] = 1

  visited = color_bipartite_am(graph, 0)

  if visited is None:
    print('not a tree')
    return

  srcs = []
  sinks = []
  for i in range(n):
    if visited[i] == 0:
      srcs.append(i)
    else:
      sinks.append(i)

  graph = extend_graph_ff(graph, srcs, sinks)

  return ford_fulkerson(graph, len(graph)-2, len(graph)-1)


# 1
graph = [[0, 1, 1],
         [1, 0, 0],
         [1, 0, 0]]

# 2
graph = [[0, 1, 1, 0],
         [1, 0, 0, 1],
         [1, 0, 0, 0],
         [0, 1, 0, 0]]

# 6
graph = [[0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

# 5
graph = [[0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(find_matching_val(graph))
