from copy import deepcopy


def dfs(graph, degrees):
  n = len(graph)
  # visited[u][v] - czy krawedz u -> v zostala odwiedzona
  # graf jest nieskierowany wiec visited[u][v] = visited[v][u]
  visited = [[0 for _ in range(n)] for _ in range(n)] # O(n^2)
  cycle = []

  def dfs_visit(u):
    nonlocal graph, n, degrees, visited, cycle

    for v in range(n): # O(n)
      # jezeli krawedz istnieje i nie zostala odwiedzona
      if graph[u][v] == 1 and visited[u][v] == 0:
        # zaznaczamy, ze odwiedzilismy ja
        visited[u][v] = visited[v][u] = 1
        # dla obu wierzcholkow stopien zmniejszy sie o 1 bo nie bedziemy juz rozpatrywali krawedzi u <-> v
        degrees[u] -= 1
        degrees[v] -= 1
        # odwiedzamy nastepny wierzcholek
        dfs_visit(v)

    # jezeli skonczylismy przetwarzac obecny wierzcholek to dodajemy go do cyklu
    if degrees[u] == 0:
      cycle.append(u) # zamortyzowane O(1)

  # na tym etapie pewnym jest, ze graf posiada cykl Eulera (przypadek przeciwny odrzucilismy w glownej funkcji).
  # wystarczy wywolac dfsa z jednego wierzcholka, poniewaz nie ma znaczenia
  # w ktorym miejscu cyklu zaczniemy i tak odwiedzimy wszystkie krawedzie.
  # max ilosc dla grafu pelnego i wynosi:
  # (n po 2) = n!/(2!*(n - 2)!) = (n*(n-1))/2 ≃ n^2
  # dfs_visit(0) zakonczy sie kiedy odwiedzone zostana wszystkie krawedzie oraz
  # zeby wykonac rekurencyjnie dfs_visit() musimy odwiedzic jedna krawedz
  dfs_visit(0)

  return cycle


def euler( G ):
  n = len(G)
  degrees = [0]*n # O(n)

  # wyznaczamy stopnie wierzcholkow
  for i in range(n): # O(n)
    for j in range(n): # O(n)
      degrees[i] += G[i][j]

    # jezeli ktorys z wierzcholkow nie posiada parzystego stopnia to graf nie posiada cyklu Eulera      
    if degrees[i]%2 == 1:
      return None

  cycle = dfs(G, degrees)

  return cycle
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")
