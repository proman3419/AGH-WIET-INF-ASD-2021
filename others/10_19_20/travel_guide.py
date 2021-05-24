from queue import PriorityQueue
from math import inf


def get_path(parents, v, capacity):
  def get_path_rec(v):
    nonlocal parents, path

    if v == None:
      return

    get_path_rec(parents[v])
    path.append(v)

  if capacity[v] == 0:
    return None

  path = []
  get_path_rec(v)

  return path


def dijkstra(graph, s, e, starts, max_v):
  n = len(graph)
  queue = PriorityQueue()
  processed = [False]*n
  capacities = [-1]*(max_v+1)
  parents = [None]*(max_v+1)

  queue.put((-capacities[s], s))

  while not queue.empty():
    u = queue.get()[1]

    if not processed[u]:
      for i in range(starts[u], starts[u+1]):
        v = graph[i][1]

        if capacities[u] == -1:
          curr_capacity = graph[i][2]
        else:
          curr_capacity = min(capacities[u], graph[i][2])

        if curr_capacity > capacities[v]:
          if u != v:
            parents[v] = u
          capacities[v] = curr_capacity
          queue.put((-capacities[v], graph[i][1]))

      processed[u] = True

  return (get_path(parents, e, capacities), capacities[e])


def find_max_vertex(graph):
  _max = max(graph[0][0], graph[0][1])
  for i in range(len(graph)):
    _max = max(_max, graph[i][0], graph[i][1])

  return _max


def generate_starts(graph, max_v):
  n = len(graph)

  # max_v + 1 bo inkluzywnie, +1 bo nie chcemy ifowac jak bedziemy rozpatrywali ostatni wierzcholek
  starts = [n]*(max_v+2) 
  starts[0] = 0
  i = x = 0
  
  while i < n:
    while i < n and graph[i][0] == x:
      i += 1

    if i == n:
      break

    x += 1
    starts[x] = i

    while i < n and graph[i][0] < x:
      i += 1

  return starts


def travel_guide(graph, A, B):
  # -x[2] bo chcemy rozpatrywac pojemnosci od najwiekszej
  graph.sort(key=lambda x: (x[0], -x[2]))

  max_v = find_max_vertex(graph)

  starts = generate_starts(graph, max_v)

  return dijkstra(graph, A, B, starts, max_v)


graph = [(0, 1, 2), (0, 2, 4), (1, 2, 10), (1, 3, 7), (2, 4, 3), (3, 5, 1), (4, 3, 2), (4, 5, 5)]

A = 0
B = 5

print(travel_guide(graph, A, B))
