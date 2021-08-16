# algorytm zaklada, ze sortowany graf jest DAGiem (Directed Acyclic Graph)


# O(V^2)
def topologic_sort_am_util(graph, s, visited, res, m):
  n = len(graph)
  def dfs_visit(u):
    nonlocal graph, visited, res, m, n

    visited[u] = True
    for v in range(n):
      if graph[u][v] != 0:
        if not visited[v]:
          dfs_visit(v)

    res[m] = u
    m -= 1

  dfs_visit(s)

  return m


# O(V^2)
def topologic_sort_am(graph):
  n = len(graph)
  visited = [False]*n
  res = [-1]*n
  m = n - 1 # ostatni indeks, do ktorego bedziemy wpisywali rozwiazanie

  for i in range(n):
    if not visited[i]:
      m = topologic_sort_am_util(graph, i, visited, res, m)

  return res


# [0, 1, 4, 6, 5, 3, 2]
graph_am = [[0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

print(topologic_sort_am(graph_am))


# ==============================================================================

def topologic_sort_nl_util(graph, s, visited, res, m):
  def dfs_visit(u):
    nonlocal graph, visited, res, m

    visited[u] = True
    for v in graph[u]:
      if not visited[v]:
        dfs_visit(v)

    res[m] = u
    m -= 1

  dfs_visit(s)

  return m


# O(V + E)
def topologic_sort_nl(graph):
  n = len(graph)
  visited = [False]*n
  res = [-1]*n
  m = n - 1 # ostatni indeks, do ktorego bedziemy wpisywali rozwiazanie

  for i in range(n):
    if not visited[i]:
      m = topologic_sort_nl_util(graph, i, visited, res, m)

  return res


# [0, 1, 4, 6, 5, 3, 2]
graph_nl = [[1, 2],
            [2, 4],
            [],
            [],
            [3, 5, 6],
            [],
            []]

print(topologic_sort_nl(graph_nl))
