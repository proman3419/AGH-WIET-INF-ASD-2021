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

graph = [[1, 2], [0, 2], [0, 1, 8], [4, 5], [3, 6], [3, 6, 10], [4, 5, 7], [6, 8, 9], [2, 7, 9], [7, 8], [5, 11, 12], [10, 12], [10, 11]]

print(nl_to_am(graph))
#print(am_to_nl(graph))
#print(am_to_nl(nl_to_am(graph)))
