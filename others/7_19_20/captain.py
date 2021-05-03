def dfs(graph, s):
  visited = [False]*len(graph)

  def dfs_visit(u):
    nonlocal graph, visited

    visited[u] = True
    for v in graph[u]:
      if not visited[v]:
        dfs_visit(v)

  dfs_visit(s)


def captain(M, T):
  n = len(M[0])
  m = len(M)
  visited = [[False for _ in range(n)] for _ in range(m)]

  def captain_visit(y, x):
    nonlocal M, T, visited, n, m

    visited[y][x] = True
    if y-1 >= 0 and not visited[y-1][x] and M[y-1][x] >= T: captain_visit(y-1, x)
    if x-1 >= 0 and not visited[y][x-1] and M[y][x-1] >= T: captain_visit(y, x-1)
    if y+1 < m and not visited[y+1][x] and M[y+1][x] >= T: captain_visit(y+1, x)
    if x+1 < n and not visited[y][x+1] and M[y][x+1] >= T: captain_visit(y, x+1)

  captain_visit(0, 0)

  return visited[-1][-1]


# M = [[1, 0, 0, 1, 1, 0, 0, 1],
#      [1, 1, 1, 1, 0, 1, 0, 0],
#      [1, 0, 0, 1, 0, 0, 1, 0],
#      [1, 0, 0, 1, 1, 0, 0, 0],
#      [1, 1, 0, 0, 1, 1, 1, 1]]
# T = 1

M = [[4, 3, 2],
     [1, 2, 0],
     [3, 3, 3],
     [10, 2, 1]]
T = 3

print(captain(M, T))
