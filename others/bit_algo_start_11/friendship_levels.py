from collections import deque


# O(V + E)
def bfs_nl(graph, s):
  n = len(graph)
  queue = deque()
  visited = [False]*n
  distances = [-1]*n

  distances[s] = 0
  visited[s] = True
  queue.append(s)

  while queue:
    u = queue.popleft()

    for v in graph[u]:
      if not visited[v]:
        distances[v] = distances[u] + 1
        visited[v] = True
        queue.append(v)

  return max(distances)


def friendship_levels(graph):
  n = len(graph)
  max_level = 0

  for i in range(n):
    max_level = max(max_level, bfs_nl(graph, i))

  return max_level


# 2
graph = [[1, 2],
         [0, 2],
         [0, 1, 3],
         [2]]

print(friendship_levels(graph))
