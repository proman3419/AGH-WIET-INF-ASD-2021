from queue import PriorityQueue
from math import inf


def get_path(distances, parents, v, n):
  if distances[v] == inf:
    return None

  if parents[v] is None:
    return []

  path = []

  prev_v = v
  while v is not None:
    prev_v = v
    path.append(v%n)
    v = parents[v]

  return (prev_v, path[::-1])


# O(V + E*log(V))
def dijkstra_nl(graph, x, y):
  n = len(graph)
  m = 2*n # 0..n - A, n..2n - B
  queue = PriorityQueue()
  processed = [False]*m
  distances = [inf]*m
  parents = [None]*m

  distances[x] = 0
  queue.put((distances[x], x))
  distances[n+x] = 0
  queue.put((distances[n+x], n+x))

  while not queue.empty():
    u = queue.get()[1]

    if not processed[u]:
      for v, weight in graph[u%n]:
        if u < n: # is_alice = True
          curr_dist = distances[u] + weight

          if curr_dist < distances[n+v]:
            parents[n+v] = u
            distances[n+v] = curr_dist
            queue.put((distances[n+v], n+v))
        else: # is_alice = False
          curr_dist = distances[u]

          if curr_dist < distances[v]:
            parents[v] = u
            distances[v] = curr_dist
            queue.put((distances[v], v))

      processed[u] = True

  return get_path(distances, parents, y, n)


  # O(V + E*log(V))
def two_drivers(G, x, y):
  prev_v, path = dijkstra_nl(G, x, y)
  s_person = 'A' if prev_v < len(G) else 'B'

  return (s_person, path)


# ('A', [0, 1, 2])
G = [[[1, 10], [2, 40]],
     [[0, 10], [2, 20]],
     [[0, 40], [1, 20]]]
x = 0; y = 2

# ('B', [3, 4, 5, 0])
G = [[[1, 13], [2, 32], [5, 5]],
     [[0, 13], [2, 40], [5, 2]],
     [[0, 32], [1, 40], [3, 11], [4, 20]],
     [[2, 11], [4, 18]],
     [[2, 20], [3, 18], [5, 8]],
     [[0, 5], [1, 2], [4, 8]]]
x = 3; y = 0

# ('B', [2, 1])
x = 2; y = 1

# ('B', [4, 5, 1, 0])
x = 4; y = 0

print(two_drivers(G, x, y))
