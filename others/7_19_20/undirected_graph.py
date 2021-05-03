def nl_to_am(nl):
  n = len(nl)
  am = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(len(nl[i])):
      am[i][nl[i][j]] = 1

  return am


# O(n^2)
def is_undirected(graph):
  am = nl_to_am(graph)
  n = len(graph)

  for i in range(n):
    for j in range(n):
      if am[i][j] != am[j][i]:
        return False

  return True


# True
graph = [[1, 3],
         [0, 2],
         [1, 3],
         [0, 2]]

# False
# graph = [[1],
#          [2],
#          [3],
#          [0]]

print(is_undirected(graph))
