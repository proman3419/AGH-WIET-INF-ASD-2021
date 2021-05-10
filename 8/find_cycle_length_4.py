from collections import deque


def check_if_full(graph):
  n = len(graph)

  for i in range(n):
    for j in range(n):
      if i != j and graph[i][j] == 0:
        return False

  return True


# O(n^2)
def bfs(graph, s):
  n = len(graph)
  queue = deque()
  visited = [False]*n # O(n)
  distances = [-1]*n # O(n)
  paths = [-1]*n # O(n)

  distances[s] = 0
  visited[s] = True
  queue.append(s)

  while queue: # O(n)
    u = queue.popleft()

    if distances[u] == 2:
      break

    for v in range(n): # O(n)
      if graph[u][v] == 1:
        if not visited[v]:
          distances[v] = distances[u] + 1
          paths[v] = u
          visited[v] = True
          queue.append(v)
        else:
          if distances[v] == 2:
            return (paths, u, v)

  return (None, None, None)


# O(n^3)
def find_cycle_length_4(graph):
  n = len(graph)

  # jezeli graf jest pelny to usuwamy jedna krawedz, inaczej dla tego przypadku algorytm nie zadziala.
  # nie zadziala poniewaz dla kazdego punktu min odleglosc bedzie rowna 1.
  # na koniec cofamy ta zmiane
  is_full = check_if_full(graph) # O(n^2)
  if is_full:
    graph[0][n-1] = 0

  # dla kazdego wierzcholka odpalamy bfsa na max odleglosc 2.
  # jezeli znajdziemy jakis wierzcholek, ktory ma odleglosc 2 od poczatkowego
  # to oznacza to, ze obecny wierzcholek przez krawedz z tym wierzcholkiem tworzy cykl o dlugosci 4
  for i in range(n): # O(n)
    paths, s, e = bfs(graph, i) # O(n^2)
    if paths != None:
      break

  if paths == None:
    return None

  if is_full:
    graph[0][n-1] = 1

  return [s, paths[s], paths[e], e]


# [5, 3, 4, 6]
# graph = [[0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 0]]

# [2, 0, 1, 4]
# n = 5
# graph = [[0 if i == j else 1 for i in range(n)] for j in range(n)]

# None
# n = 3
# graph = [[0 if i == j else 1 for i in range(n)] for j in range(n)]

# [2, 0, 1, 3]
# graph = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]]

# None
# graph = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]]

# None
# graph = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0]]

# [5, 0, 2, 3]
# graph = [[0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0]]

# None
# graph = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print(find_cycle_length_4(graph))
