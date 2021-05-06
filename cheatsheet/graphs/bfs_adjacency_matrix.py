from queue import Queue


def bfs_am(graph, s):
  n = len(graph)
  queue = Queue()
  visited = [False]*n

  #print(f'odwiedz: {s}\n')
  queue.put(s)
  visited[s] = True

  while not queue.empty():
    u = queue.get()
    #print(f'rodzic: {u}')
    for v in range(n):     
      if graph[u][v] == 1 and not visited[v]:
        #print(f'odwiedz: {v}')
        visited[v] = True
        queue.put(v)
    #print()


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
