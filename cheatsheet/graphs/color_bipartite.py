def color_bipartite(graph, s):
  # None - nieodwiedzony, {0, 1} - kolor
  visited = [None]*len(graph)
  bipartite_flag = True

  def dfs_visit(u, color):
    nonlocal graph, visited, bipartite_flag

    visited[u] = color
    for v in graph[u]:
      if not bipartite_flag:
        return

      if visited[v] is not None:
        if visited[v] == color:
          bipartite_flag = False
          return
      else:
        dfs_visit(v, (color+1)%2)

  for v in range(len(graph)):
    if visited[v] is None:
      dfs_visit(v, 0)

  if bipartite_flag:
    return visited

  return None


# [0, 1, 0, 1, 0, 1, 0]
graph = [[3, 5],
         [2, 6],
         [1],
         [0, 4],
         [3],
         [0, 6],
         [1, 5]]

# None
# graph = [[3, 5],
#          [2, 6],
#          [1],
#          [0, 4, 5],
#          [3],
#          [0, 3, 6],
#          [1, 5]]

# [0, 0, 0]
# graph = [[], [], []]

# None
# graph = [[1, 3, 5], [0, 5], [4], [4, 0], [3, 2], [1, 0]]

# [0, 0, 1]
# graph = [[],
#          [2],
#          [1]]

# None
# graph = [[],
#          [2, 3],
#          [1, 3],
#          [1, 2]]

print(color_bipartite(graph, 0))
