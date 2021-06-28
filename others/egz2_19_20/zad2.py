from zad2testy import runtests
from math import ceil, inf


def distance(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)


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
def kruskal(graph, V, A):
  graph.sort(key=lambda x: x[2])
  vertices = [Node(i) for i in range(V)]
  result = []

  i = 0
  e_cnt = 0
  min_diff = 0
  max_diff = 0
  while e_cnt < V - 1:
    u, v, w, sgn = graph[i]
    i += 1
    x = find(vertices[u])
    y = find(vertices[v])

    if x != y:
      if sgn:
        if w > max_diff:
          max_diff = w
      elif -1*w < min_diff:
        min_diff = -1*w

      e_cnt += 1
      result.append([u, v, w])
      union(x, y)

  return max_diff - min_diff


def generate_edges_graph(A, V):
  edges = []

  for i in range(V):
    for j in range(V):
      if i != j:
        edges.append([i, j, ceil(distance(A[i], A[j]))])

  return edges


def generate_time_diffs_graph(edges, e_i):
  n = len(edges)
  td_graph = []

  for i in range(n):
    td_graph.append([edges[i][0], edges[e_i][1], abs(edges[i][2]-edges[e_i][2]),edges[i][2]-edges[e_i][2] >= 0])

  return td_graph


# O(E*log(E))
def highway(A):
  V = len(A)
  edges = generate_edges_graph(A, V)

  min_diff = inf
  for i in range(len(edges)):
    td_graph = generate_time_diffs_graph(edges, i)
    curr_diff = kruskal(td_graph, V, A)

    if curr_diff < min_diff:
      min_diff = curr_diff

  return min_diff
        

runtests( highway ) 
