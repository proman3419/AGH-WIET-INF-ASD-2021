from zad3testy import runtests


def topologic_sort_util(graph, s, visited, res, m, n):
  def dfs_visit(u):
    nonlocal graph, visited, res, m

    visited[u] = True
    for v in range(n):
      if graph[u][v] == 1:
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
      m = topologic_sort_util(graph, i, visited, res, m, n)

  return res


# O(V + E)
def tasks(T):
  return topologic_sort(T)


runtests( tasks )
