# O(V^2)
def scc_am_util(graph):
  n = len(graph)
  visited = [False]*n
  time = 0
  process_times = [-1]*n

  def dfs_visit(u):
    nonlocal graph, visited, time, n
    nonlocal process_times

    time += 1
    visited[u] = True

    for v in range(n):
      if graph[u][v] == 1 and not visited[v]:
        dfs_visit(v)

    time += 1
    process_times[u] = time

  for u in range(n):
    if not visited[u]:
      dfs_visit(u)

  return process_times


def scc_am_util_reverse(graph, visited, sccs, u, scc_id):
  visited[u] = True
  sccs[u] = scc_id

  for v in range(len(graph)):
    if graph[v][u] == 1 and not visited[v]:
      scc_am_util_reverse(graph, visited, sccs, v, scc_id)


# O(V^2)
def scc_am(graph):
  n = len(graph)
  process_times = scc_am_util(graph)

  to_sort = [(i, process_times[i]) for i in range(n)]
  to_sort.sort(key=lambda x: x[1], reverse=True)

  visited = [False]*n
  sccs = [-1]*n
  scc_id = 0
  for e in to_sort:
    if not visited[e[0]]:
      scc_am_util_reverse(graph, visited, sccs, e[0], scc_id)
      scc_id += 1

  return sccs


# [0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]
graph = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

print(scc_am(graph))

# ==============================================================================

# O(V + E)
def scc_nl_util(graph):
  n = len(graph)
  visited = [False]*n
  time = 0
  process_times = [-1]*n

  def dfs_visit(u):
    nonlocal graph, visited, time, n
    nonlocal process_times

    time += 1
    visited[u] = True

    for v in graph[u]:
      if not visited[v]:
        dfs_visit(v)

    time += 1
    process_times[u] = time

  for u in range(n):
    if not visited[u]:
      dfs_visit(u)

  return process_times


def generate_reversed_graph_nl(graph):
  n = len(graph)
  _graph = [[] for _ in range(n)]

  for u in range(n):
    for v in graph[u]: 
      _graph[v].append(u)

  return _graph


def scc_nl_util_reverse(graph, visited, sccs, u, scc_id):
  visited[u] = True
  sccs[u] = scc_id

  for v in graph[u]:
    if not visited[v]:
      scc_nl_util_reverse(graph, visited, sccs, v, scc_id)


# O(V + E)
def scc_nl(graph):
  n = len(graph)
  process_times = scc_nl_util(graph)

  to_sort = [(i, process_times[i]) for i in range(n)]
  to_sort.sort(key=lambda x: x[1], reverse=True)

  r_graph = generate_reversed_graph_nl(graph)

  visited = [False]*n
  sccs = [-1]*n
  scc_id = 0
  for e in to_sort:
    if not visited[e[0]]:
      scc_nl_util_reverse(r_graph, visited, sccs, e[0], scc_id)
      scc_id += 1

  return sccs


graph_nl = [[1, 4],
            [2, 3],
            [0, 7],
            [4],
            [5],
            [3, 6],
            [3],
            [9],
            [7, 6],
            [10],
            [8]]

print(scc_nl(graph_nl))
