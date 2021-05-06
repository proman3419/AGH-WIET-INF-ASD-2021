def dfs_nl(graph, s):
  visited = [False]*len(graph)
  time = 0

  def dfs_visit(u):
    nonlocal graph, visited, time

    time += 1 # czas odwiedzenia

    visited[u] = True
    for v in graph[u]:
      if not visited[v]:
        #print(f'odwiedz: {v}')
        dfs_visit(v)

    time += 1 # czas przetworzenia

  #print(f'odwiedz: {s}')
  dfs_visit(s)


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

dfs_nl(graph, 0)
