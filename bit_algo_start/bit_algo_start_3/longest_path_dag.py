def topologic_sort_util(graph, s, visited, res, m, n):
  def dfs_visit(u):
    nonlocal graph, visited, res, m, n

    visited[u] = True
    for v in range(n):
      if graph[u][v]:
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


def get_longest_path_len_dag(graph):
  n = len(graph) 

  # F[i] - dlugosc najdluzszej sciezki konczacej sie w i
  F = [0]*n

  sorted_order = topologic_sort(graph)

  for v in sorted_order:
    for u in range(n):
      if graph[u][v] == 1:
        F[v] = max(F[v], F[u] + 1)

  return max(F)


# [0, 2, 1, 2, 5, 4, 3]
graph = [[0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]]

print(get_longest_path_len_dag(graph))
