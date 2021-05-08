class Vertex:
  def __init__(self, neighbors, _id):
    self.neighbors = neighbors
    self.id = _id
    self.parent = None
    self.visited = False
    #self.distance = -1
    self.visit_time = -1
    self.process_time = -1
    self.scc = -1
    
  def display(self):
    print(f'vertex {self.id} ================================================')
    print(f'neighbors: {self.neighbors}')
    print(f'parent: {self.parent}')
    print(f'visited: {self.visited}')
    #print(f'distance: {self.distance}')
    print(f'visit_time: {self.visit_time}')
    print(f'process_time: {self.process_time}')
    print(f'scc: {self.scc}')
    print()
    

def display_graph(graph):
  for i in range(len(graph)):
    graph[i].display()


def scc_util(graph):
  n = len(graph)
  time = 0

  def dfs_visit(u):
    nonlocal graph, time, n

    time += 1
    # czas odwiedzenia
    graph[u].visit_time = time
    graph[u].visited = True

    for v in range(n):
      if graph[u].neighbors[v] == 1 and not graph[v].visited:
        graph[v].parent = u
        dfs_visit(v)

    time += 1
    # czas przetworzenia
    graph[u].process_time = time

  for u in range(len(graph)):
    if not graph[u].visited:
      dfs_visit(u)


def scc_util_reverse(graph, u, scc_id):
  graph[u].visited = True
  graph[u].scc = scc_id

  for v in range(len(graph)):
    if graph[v].neighbors[u] == 1 and not graph[v].visited:
      scc_util_reverse(graph, v, scc_id)


def scc(graph):
  # wykonujemy dfs
  scc_util(graph)

  # sortujemy malejaco po czasie przetworzenia
  # tworzymy kopie wierzcholkow zawierajaca (id, process_time)
  # sortujac po oryginale reprezentacja macierzowa stracilaby na znaczeniu
  to_sort = [(v.id, v.process_time) for v in graph]
  to_sort.sort(key=lambda x: x[1], reverse=True)

  # resetujemy flagi odwiedzenia
  for i in range(len(graph)):
    graph[i].visited = False

  scc_id = 0
  # ponowne wykonanie dfs po grafie z odwroconymi krawedziami
  for e in to_sort:
    if not graph[e[0]].visited:
      scc_util_reverse(graph, e[0], scc_id)
      scc_id += 1


# graph = [[1, 4],
#          [2, 3],
#          [0, 7],
#          [4],
#          [5],
#          [3, 6],
#          [3],
#          [9],
#          [7, 6],
#          [10],
#          [8]]

graph = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

graph = [Vertex(graph[i], i) for i in range(len(graph))]

scc(graph)
display_graph(graph)
