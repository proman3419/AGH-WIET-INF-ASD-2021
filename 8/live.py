def remove(G):
    n = len(G)
    visited = [False]*n
    process = [0]*n #czas przetworzenia
    time = 0

    def dfs_visit(u):
        nonlocal G, visited,time
        time += 1
        visited[u] = True
        for i in range(n):
            if not visited[i]:
                dfs_visit(i)
        time += 1
        process[u] = time

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    for i in range(n): #krotka z indeksem i czasem przetworzenia
        process[i] = (process[i],i)

    process = sorted(process, key = lambda x: x[0]) #sortuej po czasie przetowrzenia

    for i in range(n):
        process[i] = process[i][1]

    #for i in range(n): #usuwam krawedzie z wierzchołków od najmniejszego czasu przetworznia
    #   for j in range(n):
    #      G[i][j] = 0

    return process

G = [[0,1,1,0],[1,1,0,0],[1,1,0,1],[0,0,1,0]]
G = [[0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]
G = [[0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]]
print(remove(G))





def is_bipartite(graph, s):
  # None - nieodwiedzony, {0, 1} - kolor
  visited = [None]*len(graph)
  bipartite_flag = True

  def dfs_visit(u, color):
    nonlocal graph, visited, bipartite_flag

    visited[u] = color
    for v in graph[u]:
      # przerwanie rekurencji
      if not bipartite_flag:
        return

      # jezeli zostal juz odwiedzony
      if visited[v] is not None:
        # i ma ten sam kolor co jego rodzic to znaczy, ze
        # 2 kolory sa niewystarczjace do pokolorowania jego wierzcholkow
        # czyli nie jest dwudzielny
        if visited[v] == color:
          bipartite_flag = False
          return
      # jezeli nie zostal odwiedzony to odwiedzamy go i bedziemy go kolorowac
      # innym kolorem niz obecnym
      else:
        dfs_visit(v, (color+1)%2)

  dfs_visit(s, 0)

  return bipartite_flag


# True
# graph = [[3, 5],
#          [2, 6],
#          [1],
#          [0, 4],
#          [3],
#          [0, 6],
#          [1, 5]]

# False
# graph = [[3, 5],
#          [2, 6],
#          [1],
#          [0, 4, 5],
#          [3],
#          [0, 3, 6],
#          [1, 5]]

# True
# graph = [[], [], []]

# False
graph = [[1, 3, 5], [0, 5], [4], [4, 0], [3, 2], [1, 0]]

print(is_bipartite(graph, 0))


def BFS(G, s):
    # G = (V, E)

    V = G[0]
    E = G[1]
    n = V


    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]


    for i in range(n):
        for j in range(n):
            for p in range(n):
                visited[p] = False
                parent[p] = None
                    
            if E[i][j] == 1:
                for k in range(n):
                    if k != i and E[j][k] == 1 and not visited[k]:
                        visited[k] = True
                        parent[k] = j
                    elif k != i and E[j][k] == 1 and visited[k]:
                        kr = (i, j, k, parent[k])
                        return kr

    return None


def cycle_4(G):
    n = len(G)

    M = [[0 for i in range(n)]  for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(j+1,n):
                if i==j or i == k: continue
                elif G[i][j] == 1 and G[i][k] == 1:
                    if M[j][k] == 0 and M[k][j] == 0:
                        M[j][k] = 1
                        M[k][j] = 1
                    else:
                        return True

    return False

print(cycle_4(G))




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
