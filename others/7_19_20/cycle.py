from queue import Queue


def bfs(graph, s):
  n = len(graph)
  queue = Queue()
  visited = [False]*n
  parent = [None]*n

  queue.put(s)
  visited[s] = True

  while not queue.empty():
    u = queue.get()
    for v in graph[u]:
      if visited[v]:
        if v != parent[u]:
          return True
      else:
        parent[v] = u
        visited[v] = True
        queue.put(v)

  return False


# False
# graph = [[1],
#          [0, 2],
#          [1]]

# True
graph = [[1, 2],
         [0, 2],
         [1, 0]]

print(bfs(graph, 0))
