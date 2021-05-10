def find_candidate(graph):
  n = len(graph)

  i = j = 0
  while i < n:
    while j < n:
      if graph[i][j] == 1:
        i = j
      else:
        j += 1
        if j == n:
          return i
    i += 1

  return n - 1
  

def universal_vertex_n(graph):
  n = len(graph)
  candidate = find_candidate(graph)

  for i in range(n):
    if i == candidate or (graph[candidate][i] == 0 and graph[i][candidate] == 1):
      continue
    return None

  return candidate


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
# graph = [[0, 0, 0, 0, 1],
#          [1, 0, 0, 0, 1],
#          [1, 0, 0, 0, 1],
#          [1, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0]]

print(universal_vertex_n(graph))
