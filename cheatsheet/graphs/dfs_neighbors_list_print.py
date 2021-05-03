def dfs_nl(graph, s):
  visited = [False]*len(graph)

  def dfs_visit(u):
    nonlocal graph, visited

    visited[u] = True
    for v in graph[u]:
      if not visited[v]:
        print(f'visit: {v}')
        dfs_visit(v)

  print(f'visit: {s}')
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
