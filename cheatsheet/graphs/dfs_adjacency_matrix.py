def dfs_am(graph, s):
  n = len(graph)
  visited = [False]*n
  time = 0

  def dfs_visit(u):
    nonlocal graph, visited, time, n

    time += 1
    # czas odwiedzenia

    visited[u] = True
    for v in range(n):
      if graph[u][v] == 1 and not visited[v]:
        #print(f'odwiedz: {v}')
        dfs_visit(v)

    time += 1
    # czas przetworzenia

  #print(f'odwiedz: {s}')
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
