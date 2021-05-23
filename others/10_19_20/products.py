from queue import PriorityQueue
from math import inf


def get_path(distances, parents, v):
  def get_path_rec(v):
    nonlocal parents, path

    if v == None:
      return

    get_path_rec(parents[v])
    path.append(v)

  if distances[v] == inf:
    return None

  path = []
  get_path_rec(v)

  return path


def djikstra(graph, s, e):
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
        if distances[u] != 0:
          curr_dist = distances[u]*weight
        else:
          curr_dist = weight

        if curr_dist < distances[v]:
          parents[v] = u
          distances[v] = curr_dist
          queue.put((distances[v], v))

      processed[u] = True

  return (get_path(distances, parents, e), distances[e])


def find_path_min_product(graph, u, v):
  return djikstra(graph, u, v)


# ([0, 1, 2, 4, 3, 5], 12)
graph = [[(1, 2), (2, 4)],
         [(2, 1), (3, 7)],
         [(4, 3)],
         [(5, 1)],
         [(3, 2), (5, 5)],
         []]

print(find_path_min_product(graph, 0, 5))
