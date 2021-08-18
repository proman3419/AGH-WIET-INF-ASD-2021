def color_bipartite_am(graph, s):
  n = len(graph)
  # None - nieodwiedzony, {0, 1} - kolor
  visited = [None]*len(graph)
  bipartite_flag = True

  def dfs_visit(u, color):
    nonlocal graph, visited, bipartite_flag, n

    visited[u] = color
    for v in range(n):
      if not bipartite_flag:
        return

      if graph[u][v] != 0:
        if visited[v] is not None:
          if visited[v] == color:
            bipartite_flag = False
            return
        else:
          dfs_visit(v, (color+1)%2)

  for u in range(len(graph)):
    if visited[u] is None:
      dfs_visit(u, 0)

  if bipartite_flag:
    return visited

  return None


# [0, 1, 0, 1, 0, 1, 0]
graph_am = [[0, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0]]

# None
# graph_am = [[0, 0, 0, 1, 0, 1, 0],
#             [0, 0, 1, 0, 0, 0, 1],
#             [0, 1, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 1, 1, 0],
#             [0, 0, 0, 1, 0, 0, 0],
#             [1, 0, 0, 1, 0, 0, 1],
#             [0, 1, 0, 0, 0, 1, 0]]

# [0, 0, 0]
# graph_am = [[0, 0, 0], 
#             [0, 0, 0], 
#             [0, 0, 0]]

# None
# graph_am = [[0, 1, 0, 1, 0, 1],
#             [1, 0, 0, 0, 0, 1],
#             [0, 0, 0, 0, 1, 0],
#             [1, 0, 0, 0, 1, 0],
#             [0, 0, 1, 1, 0, 0],
#             [1, 1, 0, 0, 0, 0]]

# [0, 0, 1]
# graph_am = [[0, 0, 0],
#             [0, 0, 1],
#             [0, 1, 0]]

# None
# graph_am = [[0, 0, 0, 0],
#             [0, 0, 1, 1],
#             [0, 1, 0, 1],
#             [0, 1, 1, 0]]

print(color_bipartite_am(graph_am, 0))

# ==============================================================================

def color_bipartite_nl(graph, s):
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

  for u in range(len(graph)):
    if visited[u] is None:
      dfs_visit(u, 0)

  if bipartite_flag:
    return visited

  return None


# [0, 1, 0, 1, 0, 1, 0]
graph_nl = [[3, 5],
            [2, 6],
            [1],
            [0, 4],
            [3],
            [0, 6],
            [1, 5]]

# None
# graph_nl = [[3, 5],
#             [2, 6],
#             [1],
#             [0, 4, 5],
#             [3],
#             [0, 3, 6],
#             [1, 5]]

# [0, 0, 0]
# graph_nl = [[], [], []]

# None
# graph_nl = [[1, 3, 5], [0, 5], [4], [4, 0], [3, 2], [1, 0]]

# [0, 0, 1]
# graph_nl = [[],
#             [2],
#             [1]]

# None
# graph_nl = [[],
#             [2, 3],
#             [1, 3],
#             [1, 2]]

print(color_bipartite_nl(graph_nl, 0))
