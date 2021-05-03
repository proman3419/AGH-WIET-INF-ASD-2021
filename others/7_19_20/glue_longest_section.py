from queue import Queue


# O(n)
def generate_vertex_to_val(sections, n):
  vertex_to_val = [sections[0][0]]
  i = 1
  j = 0
  while i + j < 2*n:
    if i < n and sections[i][0] < sections[j][1]:
      if sections[i][0] > vertex_to_val[-1]:
        vertex_to_val.append(sections[i][0])
      i += 1
    else:
      if sections[j][1] > vertex_to_val[-1]:
        vertex_to_val.append(sections[j][1])
      j += 1

  return vertex_to_val


# O(logn)
def find_vertex_id(A, x):
  n = len(A)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if A[c] < x:
      l = c + 1
    elif A[c] > x:
      r = c - 1
    else:
      while c > 0 and A[c-1] == x:
        c -= 1
      break

  if A[c] != x:
    return None
  return c


# O(m^2 + n)
def generate_adjacency_matrix(sections, n, vertex_to_val):
  m = len(vertex_to_val)
  graph = [[0 for _ in range(m)] for _ in range(m)]
  for i in range(n):
    graph[find_vertex_id(vertex_to_val, sections[i][0])][find_vertex_id(vertex_to_val, sections[i][1])] = 1

  return graph


def bfs_am(graph, visited, vertex_to_val, s):
  n = len(graph)
  queue = Queue()

  queue.put(s)
  visited[s] = 0

  while not queue.empty():
    u = queue.get()
    for v in range(n):     
      if graph[u][v] == 1 and visited[v] == 0:
        visited[v] += visited[u] + (vertex_to_val[v] - vertex_to_val[u])
        queue.put(v)


# m = len(set(sections))
# O(m^2 + n)
def glue_sections(sections):
  n = len(sections)
  if n == 0:
    return None

  # sortujemy odcinki po wartosciach poczatkowych
  sections.sort(key=lambda x: x[0]) # O(nlogn)

  # tworzymy tablice, ktora pozwala nam tlumaczyc id wierzcholkow na wartosci poczatkowe odcinkow
  vertex_to_val = generate_vertex_to_val(sections, n) # O(n)

  # generujemy macierz sasiedztwa
  graph = generate_adjacency_matrix(sections, n, vertex_to_val) # O(m^2 + n)

  m = len(vertex_to_val)
  # 0 - nieodwiedzony, > 0 - max dlugosc 
  visited = [0]*m

  # cala petla O(V + E) (((chyba)))
  for i in range(m):
    if visited[i] == 0:
      bfs_am(graph, visited, vertex_to_val, i)

  return max(visited) # O(m)


# 16
# sections = [(0, 3), (2, 6), (3, 5), 
#             (5, 11), (6, 9), (9, 14), 
#             (11, 15), (14, 18), (17, 20)]

# 18
sections = [(1, 3), (2, 7), (3, 13), (7, 20)]

print(glue_sections(sections))
