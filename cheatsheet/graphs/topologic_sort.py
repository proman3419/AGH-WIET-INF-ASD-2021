# algorytm zaklada, ze sortowany graf jest DAGiem (Directed Acyclic Graph)


def topologic_sort_util(graph, s, visited, res, m):
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


def topologic_sort(graph):
  n = len(graph)
  visited = [False]*n
  res = [-1]*n
  m = n - 1 # ostatni indeks, do ktorego bedziemy wpisywali rozwiazanie

  for i in range(n):
    if not visited[i]:
      m = topologic_sort_util(graph, i, visited, res, m)

  return res


graph = [[1, 2],
         [2, 4],
         [],
         [],
         [3, 5, 6],
         [],
         []]

print(topologic_sort(graph))
