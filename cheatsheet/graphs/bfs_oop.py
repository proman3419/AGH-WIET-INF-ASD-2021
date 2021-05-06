from queue import Queue


class Vertex:
  def __init__(self, neighbors):
    self.neighbors = neighbors
    self.parent = None
    self.visited = False
    self.distance = -1
    #self.visit_time = -1
    #self.process_time = -1
    

  def display(self):
    print(f'neighbors: {self.neighbors}')
    print(f'parent: {self.parent}')
    print(f'visited: {self.visited}')
    print(f'distance: {self.distance}')
    #print(f'visit_time: {self.visit_time}')
    #print(f'process_time: {self.process_time}')
    

def display_graph(graph):
  for i in range(len(graph)):
    print(f'vertex {i} ======================================================')
    graph[i].display()
    print()


def bfs_oop(graph, s):
  n = len(graph)
  queue = Queue()

  graph[s].distance = 0
  graph[s].visited = True
  queue.put(s)

  while not queue.empty():
    u = queue.get()

    # for v in range(n):
    #   if graph[u].neighbors[v] == 1 and not graph[v].visited:
    for v in graph[u].neighbors:
      if not graph[v].visited:
        graph[v].visited = True
        graph[v].distance = graph[u].distance + 1
        graph[v].parent = u
        queue.put(v)


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

graph = [Vertex(graph[i]) for i in range(len(graph))]

bfs_oop(graph, 0)
display_graph(graph)
