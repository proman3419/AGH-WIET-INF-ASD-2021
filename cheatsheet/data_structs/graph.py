class Vertex:
  def __init__(self, neighbors, _id):
    self.neighbors = neighbors
    self.id = _id
    self.parent = None
    self.visited = False
    self.distance = -1
    self.visit_time = -1
    self.process_time = -1
    
  def display(self):
    print(f'vertex {self.id} ================================================')
    print(f'neighbors: {self.neighbors}')
    print(f'parent: {self.parent}')
    print(f'visited: {self.visited}')
    print(f'distance: {self.distance}')
    print(f'visit_time: {self.visit_time}')
    print(f'process_time: {self.process_time}')
    print()
    

def display_graph(graph):
  for i in range(len(graph)):
    graph[i].display()
    

graph = [[1], [2], [0, 1]]
graph = [Vertex(graph[i], i) for i in range(len(graph))]

display_graph(graph)
