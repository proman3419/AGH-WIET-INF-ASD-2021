from collections import deque


# O(V^2)
def bfs_am(graph, s):
  n = len(graph)
  queue = deque()
  visited = [False]*n
  # parents = [None]*n
  # distances = [-1]*n

  # distances[s] = 0
  visited[s] = True
  queue.append(s)

  while queue:
    u = queue.popleft()

    for v in range(n):     
      if graph[u][v] == 1 and not visited[v]:
        # parents[v] = u
        # distances[v] = distances[u] + 1
        visited[v] = True
        queue.append(v)

  return visited


graph_am = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

print(bfs_am(graph_am, 0))

# ==============================================================================

# O(V + E)
def bfs_nl(graph, s):
  n = len(graph)
  queue = deque()
  visited = [False]*n
  # parents = [None]*n
  # distances = [-1]*n

  # distances[s] = 0
  visited[s] = True
  queue.append(s)

  while queue:
    u = queue.popleft()

    for v in graph[u]:
      if not visited[v]:
        # parents[v] = u
        # distances[v] = distances[u] + 1
        visited[v] = True
        queue.append(v)

  return visited


graph_nl = [[1, 2],
            [0, 3, 4],
            [0, 5, 6],
            [1],
            [1],
            [2, 7],
            [2, 8, 9],
            [5],
            [6],
            [6]]

print(bfs_nl(graph_nl, 0))
