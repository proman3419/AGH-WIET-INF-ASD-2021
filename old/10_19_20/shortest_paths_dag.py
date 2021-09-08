from queue import PriorityQueue
from math import inf


def dijkstra(graph, s):
  n = len(graph)
  queue = PriorityQueue()
  processed = [False]*n
  distances = [inf]*n
  parents = [None]*n

  distances[s] = 0
  queue.put((distances[s], s))

  while not queue.empty():
    u = queue.get()[1]

    if not processed[u]:
      for v, weight in graph[u]:
        # relaxation
        curr_dist = distances[u] + weight
        if curr_dist < distances[v]:
          parents[v] = u
          distances[v] = curr_dist
          queue.put((distances[v], v))

      processed[u] = True

  return distances, parents


def print_path(distances, parents, v):
  def print_path_rec(v):
    nonlocal parents

    if v == None or parents[v] == None: return

    print_path_rec(parents[v])
    print(parents[v], end=' ')

  if distances[v] == inf:
    print('None')
  else:
    print_path_rec(v)
    print(v)


def find_shortest_paths_dag(graph, s):
  distances, parents = dijkstra(graph, s)

  for v in range(len(graph)):
    print(f'vertex {v}: distance = {distances[v]}, path =', end=' ')
    print_path(distances, parents, v)


graph = [[(1, 1), (2, 10)],
         [(2, 2), (4, 3)],
         [],
         [],
         [(3, 4), (5, 6), (6, 7)],
         [],
         []]

s = 4

find_shortest_paths_dag(graph, s)
