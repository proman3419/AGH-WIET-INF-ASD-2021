# O(V^2)
def dfs_am(graph):
  n = len(graph)
  visited = [False]*n
  time = 0
  # parents = [None]*n
  # visit_times = [-1]*n
  # process_times = [-1]*n

  def dfs_visit(u):
    nonlocal graph, visited, time, n
    # nonlocal parents, visit_times, process_times

    time += 1
    # visit_times[u] = time
    visited[u] = True

    for v in range(n):
      if graph[u][v] == 1 and not visited[v]:
        # parents[v] = u
        dfs_visit(v)

    time += 1
    # process_times[u] = time

  for u in range(n):
    if not visited[u]:
      dfs_visit(u)

  return visited


graph_am = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

print(dfs_am(graph_am))

# ==============================================================================

# O(V + E)
def dfs_nl(graph):
  n = len(graph)
  visited = [False]*n
  time = 0
  # parents = [None]*n
  # visit_times = [-1]*n
  # process_times = [-1]*n

  def dfs_visit(u):
    nonlocal graph, visited, time, n
    # nonlocal parents, visit_times, process_times

    time += 1
    # czas odwiedzenia
    # visit_times[u] = time
    visited[u] = True

    for v in graph[u]:
      if not visited[v]:
        # parents[v] = u
        dfs_visit(v)

    time += 1
    # czas przetworzenia
    # process_times[u] = time

  for u in range(n):
    if not visited[u]:
      dfs_visit(u)

  return visited


graph_nl = [[1, 2],
            [0, 3],
            [0, 3, 4],
            [1, 2, 5],
            [2, 6],
            [3, 7],
            [4],
            [5, 8, 9],
            [7],
            [7]]

print(dfs_nl(graph_nl))
