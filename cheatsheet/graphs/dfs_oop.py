class Vertex:
  def __init__(self, neighbors):
    self.neighbors = neighbors
    self.parent = None
    self.visited = False
    #self.distance = -1
    self.visit_time = -1
    self.process_time = -1
    

  def display(self):
    print(f'neighbors: {self.neighbors}')
    print(f'parent: {self.parent}')
    print(f'visited: {self.visited}')
    #print(f'distance: {self.distance}')
    print(f'visit_time: {self.visit_time}')
    print(f'process_time: {self.process_time}')


def display_graph(graph):
  for i in range(len(graph)):
    print(f'vertex {i} ======================================================')
    graph[i].display()
    print()


def dfs_oop(graph):
  time = 0

  def dfs_visit(u):
    nonlocal graph, time

    time += 1
    # czas odwiedzenia
    graph[u].visit_time = time
    graph[u].visited = True

    # for v in range(n):
    #   if graph[u].neighbors[v] == 1 and not graph[v].visited:
    for v in graph[u].neighbors:
      if not graph[v].visited:
        graph[v].parent = u
        dfs_visit(v)

    time += 1
    # czas przetworzenia
    graph[u].process_time = time

  for u in range(len(graph)):
    if not graph[u].visited:
      dfs_visit(u)


graph = [[1, 2],
         [0, 3],
         [0, 3, 4],
         [1, 2, 5],
         [2, 6],
         [3, 7],
         [4],
         [5, 8, 9],
         [7],
         [7]]

# graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#          [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#          [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#          [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#          [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
#          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

graph = [Vertex(graph[i]) for i in range(len(graph))]

dfs_oop(graph)
display_graph(graph)
