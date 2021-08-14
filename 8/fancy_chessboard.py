from queue import PriorityQueue
from collections import deque
from math import inf


s = (0, 0)
directions = [(-1, -1), (0, -1), (1, -1),
              (-1,  0),          (1,  0),
              (-1,  1), (0,  1), (1,  1)]


def get_path(distances, parents, v):
  if distances[v[0]][v[1]] == inf:
    return None

  if parents[v[0]][v[1]] is None:
    return []

  path = []

  while v is not None:
    path.append(v)
    v = parents[v[0]][v[1]]

  return path[::-1]


# O(V + (V^2)*log(V))
def kings_path(graph):
  n = len(graph)
  queue = PriorityQueue()
  processed = [[False for _ in range(n)] for _ in range(n)]
  distances = [[inf for _ in range(n)] for _ in range(n)]
  parents = [[None for _ in range(n)] for _ in range(n)]

  distances[s[0]][s[1]] = graph[s[0]][s[1]]
  queue.put((distances[s[0]][s[0]], s))

  while not queue.empty():
    u = queue.get()[1]

    if not processed[u[0]][u[1]]:
      for d in directions:
        v = (u[0]+d[0], u[1]+d[1])

        if 0 <= v[0] < n and 0 <= v[1] < n:
          curr_dist = distances[u[0]][u[1]] + graph[v[0]][v[1]]

          if curr_dist < distances[v[0]][v[1]]:
            distances[v[0]][v[1]] = curr_dist
            parents[v[0]][v[1]] = (u[0], u[1])

            queue.put((distances[v[0]][v[1]], (v[0], v[1])))

      processed[u[0]][u[1]] = True

  print(get_path(distances, parents, (n-1, n-1)))

  return distances[-1][-1]


# W = max_w - min_w, w naszym przypadku jest to 5 - 1 = 5 wiec traktujemy jako stala i pomijamy
# O(W*V^2)
def kings_path_2(graph):
  n = len(graph)
  queue = deque()
  visited = [[False for _ in range(n)] for _ in range(n)]
  distances = [[inf for _ in range(n)] for _ in range(n)]
  parents = [[None for _ in range(n)] for _ in range(n)]

  distances[s[0]][s[1]] = graph[s[0]][s[1]]
  visited[s[0]][s[1]] = True
  queue.append((1, s))

  while queue:
    w, u = queue.popleft()

    if w > 1:
      queue.append((w-1, u)) 
      continue

    for d in directions:
      v = (u[0]+d[0], u[1]+d[1])

      if 0 <= v[0] < n and 0 <= v[1] < n and not visited[v[0]][v[1]]:
        distances[v[0]][v[1]] = distances[u[0]][u[1]] + graph[v[0]][v[1]]
        parents[v[0]][v[1]] = (u[0], u[1])
        visited[v[0]][v[1]] = True

        queue.append((graph[v[0]][v[1]], v))

  print(get_path(distances, parents, (n-1, n-1)))

  return distances[-1][-1]


# przyjmuje konwencje, w ktorej (0, 0) i (-1, -1) maja wartosc 0 bo i tak krol musi przez nie przejsc.
# kod dziala gdy nie jest zachowana

# [(0, 0), (0, 1), (1, 2), (2, 1), (3, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
# 7
A = [[0, 1, 1, 5, 5],
     [5, 5, 1, 5, 5],
     [1, 1, 1, 5, 5],
     [1, 5, 5, 5, 5],
     [1, 1, 1, 1, 0]]

# [(0, 0), (0, 1), (0, 2), (1, 3), (2, 2), (3, 1), (4, 2), (4, 3), (4, 4)]
# 7
A = [[0, 1, 1, 1, 1],
     [5, 5, 5, 1, 5],
     [5, 5, 1, 5, 5],
     [5, 1, 5, 5, 5],
     [1, 1, 1, 1, 0]]

# [(0, 0), (0, 1), (1, 2), (2, 2)]
# 4
A = [[0, 3, 2],
     [1, 5, 1],
     [2, 5, 0]]

print(kings_path(A))
print(kings_path_2(A))
