def is_bipartite(graph, s):
  # None - nieodwiedzony, {0, 1} - kolor
  visited = [None]*len(graph)
  bipartite_flag = True

  def dfs_visit(u, color):
    nonlocal graph, visited, bipartite_flag

    visited[u] = color
    for v in graph[u]:
      # przerwanie rekurencji
      if not bipartite_flag:
        return

      # jezeli zostal juz odwiedzony
      if visited[v] is not None:
        # i ma ten sam kolor co jego rodzic to znaczy, ze
        # 2 kolory sa niewystarczjace do pokolorowania jego wierzcholkow
        # czyli nie jest dwudzielny
        if visited[v] == color:
          bipartite_flag = False
          return
      # jezeli nie zostal odwiedzony to odwiedzamy go i bedziemy go kolorowac
      # innym kolorem niz obecnym
      else:
        dfs_visit(v, (color+1)%2)

  dfs_visit(s, 0)

  return bipartite_flag


# True
# graph = [[3, 5],
#          [2, 6],
#          [1],
#          [0, 4],
#          [3],
#          [0, 6],
#          [1, 5]]

# False
graph = [[3, 5],
         [2, 6],
         [1],
         [0, 4, 5],
         [3],
         [0, 3, 6],
         [1, 5]]

# True
# graph = [[], [], []]

print(is_bipartite(graph, 0))
