def dfs(graph, u):
  n = len(graph)
  visited = [0]*n

  def dfs_visit(u):
    visited[u] = 1
    for v in range(n):
      if graph[u][v] == 1 and visited[v] == 0:
        dfs_visit(v)

  dfs_visit(u)

  return visited


def transitive_closure(G):
  n = len(G)
  H = [[0 for _ in range(n)] for _ in range(n)]

  for u in range(n):
    visited = dfs(G, u)
    for v in range(n):
      if u != v:
        H[u][v] = visited[v]

  return H


# [0, 1, 1, 0, 1]
# [0, 0, 1, 0, 1]
# [0, 0, 0, 0, 1]
# [0, 0, 1, 0, 1]
# [0, 0, 0, 0, 0]
G = [[0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0]]

for r in transitive_closure(G):
  print(r)
