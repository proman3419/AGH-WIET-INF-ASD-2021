from queue import Queue


def bfs_am(graph, s):
  n = len(graph)
  queue = Queue()
  visited = [False]*n

  queue.put(s)
  visited[s] = True

  while not queue.empty():
    u = queue.get()
    for v in range(n):     
      if graph[u][v] == 1 and not visited[v]:
        visited[v] = True
        queue.put(v)


graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

bfs_am(graph, 2)
