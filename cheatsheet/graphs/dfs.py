def dfs(graph):
  n = len(graph)
  visited = [False]*n
  time = 0

  def dfs_visit(u):
    nonlocal graph, visited, time, n

    time += 1
    # czas odwiedzenia

    visited[u] = True
    # for v in range(n):
    #   if graph[u][v] == 1 and not visited[v]:
    for v in graph[u]:
      if not visited[v]:
        # print(f'visit {v}')
        dfs_visit(v)

    time += 1
    # czas przetworzenia

  for u in range(n):
    if not visited[u]:
      # print(f'visit {u}')
      dfs_visit(u)


graph = [[1, 2],
         [0, 3],
         [0, 3, 4],
         [1, 2, 5],
         [2, 6],
         [3, 7],
         [4],
         [5, 8, 9],
         [7],
         [7]]

# graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#          [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#          [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#          [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#          [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
#          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

dfs(graph)
