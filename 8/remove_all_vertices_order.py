class Vertex:
  def __init__(self, neighbors, _id):
    self.neighbors = neighbors
    self.id = _id
    self.parent = None
    self.visited = False
    #self.distance = -1
    self.visit_time = -1
    self.process_time = -1
    
  def display(self):
    print(f'vertex {self.id} ================================================')
    print(f'neighbors: {self.neighbors}')
    print(f'parent: {self.parent}')
    print(f'visited: {self.visited}')
    #print(f'distance: {self.distance}')
    print(f'visit_time: {self.visit_time}')
    print(f'process_time: {self.process_time}')
    print()


def display_graph(graph):
  for i in range(len(graph)):
    graph[i].display()


def remove_all_vertices_order_util(graph):
  time = 0

  def dfs_visit(u):
    nonlocal graph, time

    time += 1
    # czas odwiedzenia
    graph[u].visit_time = time
    graph[u].visited = True

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


def remove_all_vertices_order(graph):
  remove_all_vertices_order_util(graph)
  
  graph.sort(key=lambda x: x.process_time)
  
  print('order:', end=' ')
  for v in graph:
    print(f'{v.id}', end=' ')


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

graph = [Vertex(graph[i], i) for i in range(len(graph))]

remove_all_vertices_order(graph)
