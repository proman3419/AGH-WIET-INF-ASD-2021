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
def kruskal(graph, V, A, e_i, main_edge_w):
  vertices = [Node(i) for i in range(V)]
  result = []

  i = 0
  e_cnt = 0
  min_t_diff = 0
  max_t_diff = 0
  while e_cnt < V - 1:
    u, v, w = graph[i]
    i += 1
    x = find(vertices[u])
    y = find(vertices[v])

    t_diff = main_edge_w - w

    if x != y:
      if t_diff >= 0:
        if t_diff > max_t_diff:
          max_t_diff = t_diff
      elif t_diff < min_t_diff:
        min_t_diff = t_diff

      e_cnt += 1
      result.append([u, v, t_diff])
      union(x, y)

  return max_t_diff - min_t_diff


def generate_edges_graph(A, V):
  edges = []

  for i in range(V):
    for j in range(V):
      if i != j:
        edges.append([i, j, ceil(distance(A[i], A[j]))])

  return edges


# O(V^2*E*log(E))
def highway(A):
  V = len(A)
  edges = generate_edges_graph(A, V)
  _edges = [e for e in edges]

  min_t_diff = inf
  for i in range(len(edges)):
    _edges.sort(key=lambda e: abs(edges[i][2]-e[2]))
    t_diff = kruskal(_edges, V, A, i, edges[i][2])

    if t_diff < min_t_diff:
      min_t_diff = t_diff

  return min_t_diff
        

runtests( highway ) 
