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


# O(V + E)
def dfs_am(graph, s, t):
  n = len(graph)
  visited = [False]*n
  achieved_t = False

  def dfs_visit(u):
    nonlocal graph, visited, t, achieved_t

    visited[u] = True
    for v in range(n):
      # wczesne przerwanie rekurencji
      if achieved_t:
        return

      if graph[u][v] == 1 and not visited[v]:
        # jezeli dotarlismy do t to konczymy
        if v == t:
          achieved_t = True
          return
        else:
          dfs_visit(v)

  dfs_visit(s)

  return achieved_t


# m = len(set(sections))
# O(m^2 + n)
def glue_sections(sections, a, b):
  n = len(sections)
  if n == 0:
    return None

  # sortujemy odcinki po wartosciach poczatkowych
  sections.sort(key=lambda x: x[0]) # O(nlogn)

  # tworzymy tablice, ktora pozwala nam tlumaczyc id wierzcholkow na wartosci poczatkowe odcinkow
  vertex_to_val = generate_vertex_to_val(sections, n) # O(n)

  # generujemy macierz sasiedztwa
  graph = generate_adjacency_matrix(sections, n, vertex_to_val) # O(m^2 + n)

  a_id = find_vertex_id(vertex_to_val, a) # O(logn)
  b_id = find_vertex_id(vertex_to_val, b) # O(logn)
  return dfs_am(graph, a_id, b_id) # O(V + E)


sections = [(0, 3), (2, 6), (3, 5), 
            (5, 11), (6, 9), (9, 14), 
            (11, 15), (14, 18), (17, 20)]
a = 6
b = 18

print(glue_sections(sections, a, b))
