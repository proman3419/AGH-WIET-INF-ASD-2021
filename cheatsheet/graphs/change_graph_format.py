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


graph = [[1, 2],
         [0, 3],
         [0, 3, 4],
         [1, 2, 5],
         [2, 6],
         [3, 7],
         [4],
         [5, 8, 9],
         [7],
         [7]]

print(nl_to_am(graph))
#print(am_to_nl(graph))
#print(am_to_nl(nl_to_am(graph)))
