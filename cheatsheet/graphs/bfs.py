from queue import Queue


def bfs(graph, s):
  n = len(graph)
  queue = Queue()
  visited = [False]*len(graph)

  # print(f'odwiedz: {s}\n')
  queue.put(s)
  visited[s] = True

  while not queue.empty():
    u = queue.get()
    # print(f'rodzic: {u}')
    # for v in range(n):     
    #   if graph[u][v] == 1 and not visited[v]:
    for v in graph[u]:
      if not visited[v]:
        # print(f'odwiedz: {v}')
        visited[v] = True
        queue.put(v)
    # print()


graph = [[1, 2],
         [0, 3, 4],
         [0, 5, 6],
         [1],
         [1],
         [2, 7],
         [2, 8, 9],
         [5],
         [6],
         [6]]

# graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#          [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#          [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
#          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
         
bfs(graph, 2)
