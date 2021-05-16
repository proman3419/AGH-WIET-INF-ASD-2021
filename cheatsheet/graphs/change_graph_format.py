def nl_to_am(nl):
  n = len(nl)
  am = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(len(nl[i])):
      am[i][nl[i][j]] = 1

  return am


def am_to_nl(am):
  n = len(am)
  nl = [[] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if am[i][j] == 1:
        nl[i].append(j)

  return nl


# [[(neighbor, weight), ...], ...]
def nl_to_am_w(nl):
  n = len(nl)
  am = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(len(nl[i])):
      am[i][nl[i][j][0]] = nl[i][j][1]

  return am


# 0 - brak krawedzi, >= 1 - waga krawedzi
def am_to_nl_w(am):
  n = len(am)
  nl = [[] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if am[i][j] > 0:
        nl[i].append((j, am[i][j]))

  return nl


graph = [[1, 4],
         [2, 3],
         [0, 7],
         [4],
         [5],
         [3, 6],
         [3],
         [9],
         [7, 6],
         [10],
         [8]]

# graph = []

# print(nl_to_am(graph))
# print(am_to_nl(graph))
# print(am_to_nl(nl_to_am(graph)))

graph_w = [[(1, 2), (2, 4)],
           [(2, 1), (3, 7)],
           [(4, 3)],
           [(5, 1)],
           [(3, 2), (5, 5)],
           []]

# graph_w = []

print(nl_to_am_w(graph_w))
# print(am_to_nl_w(graph_w))
# print(am_to_nl_w(nl_to_am_w(graph_w)))
