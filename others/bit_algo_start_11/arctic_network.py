from math import ceil


def distance(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)


def generate_graph(coords, is_transmitter):
  n = len(coords)
  k = 0
  graph = []

  for i in range(n):
    for j in range(i+1, n):
      # scalamy transmitery w 1
      if is_transmitter[i] and is_transmitter[j]:
        dist = 0
      else:
        dist = distance(coords[i], coords[j])

      graph.append([i, j, dist])
      graph.append([j, i, dist])

  return graph


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

  max_dist = 0
  for u, v, w in result:
    max_dist = max(max_dist, w)

  print(result)

  return max_dist


def arctic_network(coords, transmitters):
  is_transmitter = [False]*len(coords)
  for t in transmitters:
    is_transmitter[t] = True

  graph = generate_graph(coords, is_transmitter)

  return ceil(kruskal(graph, len(coords)))


# 5
coords = [(0, 1), (1, 3), (4, 2), (6, 6), (0, 5), (7, 5)]
transmitters = []
print(arctic_network(coords, transmitters))

# 4
coords = [(0, 1), (1, 3), (4, 2), (6, 6), (0, 5), (7, 5)]
transmitters = [5, 3, 2]
print(arctic_network(coords, transmitters))
