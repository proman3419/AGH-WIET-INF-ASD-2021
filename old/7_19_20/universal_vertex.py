def universal_vertex(graph):
  n = len(graph)
  candidate = -1

  for i in range(n):
    # jezeli zadna krawedz nie wychodzi z wierzcholka
    # to jest on naszym kandydatem
    if sum(graph[i]) == 0:
      # nie moze byc wiecej niz 1 kandydat bo wtedy nie spelnimy
      # warunku polaczen ze wszystkimi innymi wierzcholkami
      if candidate != -1:
        return None
      candidate = i

  # musi byc n - 1 krawedzi, inaczej nie ma miedzy kazdym i tym
  _sum = 0
  for i in range(n):
    _sum += graph[i][candidate]
  
  if _sum == n - 1: return candidate
  return None


# 0
# graph = [[0, 0, 0, 0],
#          [1, 0, 0, 0],
#          [1, 0, 0, 0],
#          [1, 0, 1, 0]]

# None
# graph = [[0, 0, 0, 0, 0],
#          [1, 0, 0, 0, 1],
#          [1, 0, 0, 0, 1],
#          [1, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0]]

# 4
graph = [[0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0]]


print(universal_vertex(graph))
