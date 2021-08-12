from math import inf


def dfs_low(graph):
  n = len(graph)
  visited = [False]*n
  time = 0
  parents = [None]*n
  visit_times = [-1]*n
  lows = [inf]*n

  # d(v) = visit_times[v]
  # low(v) = min(
  # d(v), # 1
  # min({d(u), u: krawedz do wierz juz odwiedzonego, roznego od rodzica obecnego wierz}), # 2
  # min({low(w), w: w jest dzieckiem v w drzewie dfs}) # 3
  # )
  def dfs_visit(u):
    nonlocal graph, visited, time, n
    nonlocal parents, visit_times, lows

    time += 1
    visit_times[u] = time
    visited[u] = True

    # 1
    lows[u] = min(lows[u], visit_times[u])

    # for v in graph[u]:
    for v in range(n):
      if graph[u][v] == 1:
        if not visited[v]:
          parents[v] = u
          dfs_visit(v)
          # 3
          lows[u] = min(lows[u], lows[v])
        # 2
        elif v != parents[u]:
          lows[u] = min(lows[u], lows[v])

    time += 1

  for u in range(n):
    if not visited[u]:
      dfs_visit(u)

  return visit_times, lows, parents


def find_bridges(graph):
  n = len(graph)
  visit_times, lows, parents = dfs_low(graph)

  bridges = []
  for v in range(n):
    if lows[v] == visit_times[v] and parents[v] is not None:
      bridges.append([v, parents[v]])

  return bridges


# [[3, 2], [7, 4]]
# graph = [[0, 1, 0, 0, 1, 0, 0, 0],
#          [1, 0, 1, 0, 0, 0, 0, 0],
#          [0, 1, 0, 1, 1, 0, 0, 0],
#          [0, 0, 1, 0, 0, 1, 1, 0],
#          [1, 0, 1, 0, 0, 0, 0, 1],
#          [0, 0, 0, 1, 0, 0, 1, 0],
#          [0, 0, 0, 1, 0, 1, 0, 0],
#          [0, 0, 0, 0, 1, 0, 0, 0]]

# [[6, 7], [8, 2], [10, 5]]
graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]

# [[6, 7], [8, 2], [10, 5]]
# graph = [[1, 2], [0, 2], [0, 1, 8], [4, 5], [3, 6], [3, 6, 10], [4, 5, 7], [6, 8, 9], [2, 7, 9], [7, 8], [5, 11, 12], [10, 12], [10, 11]]

# [[3, 2], [7, 4]]
# graph = [[1, 7], [0, 2], [2, 3, 4], [2, 5, 6], [0, 2, 7], [3, 6], [5, 3], [4]]

print(find_bridges(graph))
