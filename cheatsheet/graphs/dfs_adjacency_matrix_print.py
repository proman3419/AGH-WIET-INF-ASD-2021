def dfs_am(graph, s):
  n = len(graph)
  visited = [False]*n

  def dfs_visit(u):
    nonlocal graph, visited

    visited[u] = True
    for v in range(n):
      if graph[u][v] == 1 and not visited[v]:
        print(f'visit: {v}')
        dfs_visit(v)

  print(f'visit: {s}')
  dfs_visit(s)


graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

dfs_am(graph, 0)
