class Node:
  def __init__(self, val):
    self.val = val
    self.rank = 0
    self.parent = self


def find(x):
  if x != x.parent:
    x.parent = find(x.parent)

  return x.parent


def union(x, y):
  x = find(x)
  y = find(y)

  if x == y:
    return

  if x.rank > y.rank:
    y.parent = x
  else:
    x.parent = y
    if x.rank == y.rank:
      y.rank += 1


# O(E*log(E))
def kruskal(graph, V):
  graph.sort(key=lambda x: x[2])
  vertices = [Node(i) for i in range(V)]
  result = []

  i = 0
  e_cnt = 0
  while e_cnt < V - 1:
    u, v, w = graph[i]
    i += 1
    x = find(vertices[u])
    y = find(vertices[v])

    if x != y:
      e_cnt += 1
      result.append([u, v, w])
      union(x, y)

  min_cost = 0
  for e in result:
    min_cost += e[2]

  return result


# graf nieskierowany
# [[u, v, w], ...] krawedz {u, v} o wadze w
graph = [[0, 1, 7], [0, 3, 8], [0, 5, 3], [0, 2, 2], [1, 3, 1], [2, 4, 5],
         [3, 4, 4], [3, 5, 12], [4, 5, 6], # ->
         [1, 0, 7], [3, 0, 8], [5, 0, 3], [2, 0, 2], [3, 1, 1], [4, 2, 5], 
         [4, 3, 4], [5, 3, 12], [5, 4, 6]] # <-

V = 6

print(kruskal(graph, V))
