from math import inf
from collections import deque


def bfs(graph, s, e, parents, locked):
  n = len(graph)
  queue = deque()
  visited = [False]*n

  for i in range(n):
    visited[i] = locked[i]

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

  return visited[e]


# O(V*E^2)
def ford_fulkerson(graph, src, sink):
  parents = [None]*len(graph)
  locked = [False]*len(graph)
  max_flow = 0

  while bfs(graph, src, sink, parents, locked):
    curr_flow = inf
  
    v = sink
    while v != src:
      v = parents[v]
      if v != src:
        locked[v] = True

    max_flow += 1

    v = sink
    while v != src:
      u = parents[v]
      graph[u][v] -= 1
      graph[v][u] += 1
      v = parents[v]

  return max_flow


def disconnected_paths(graph, s, t):
  # ford-fulkerson z zaznaczaniem odwiedzonych wierzcholkow.
  # mozna tez usuwac krawedzie z odwiedzanych wierzcholkow.

  # jednak nie dziala, kontprzyklad:  
  # ._____._____._____.
  # |\_._/ \___/_\_._/|
  # \_____.___/   \_._/

  # poprawnym rozwiazaniem jest rozdzielenie kazdego wierzcholka na dwa:
  # jeden wejsciowy i drugi wyjsciowy i poprzepinac krawedzie wej do wej, wyj do wyj
  # i polaczyc wierzch wej z wyj krawedzia o wadze 1.
  # nastepnie puszczamy forda fulkersona, ktory znajdzie szukane sciezki.
  # przez kazdy wierzcholek przejdzie sie tylko raz poniewaz krawedzie pomiedzy wej i wyj beda bottleneckowac

  return ford_fulkerson(graph, s, t)


# 1
graph = [[0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]] 

# print(disconnected_paths(graph, 0, 6))

# 2
graph = [[0, 1, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0]] 

# print(disconnected_paths(graph, 0, 5))

# 1
graph = [[0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0]]

print(disconnected_paths(graph, 0, 7))
