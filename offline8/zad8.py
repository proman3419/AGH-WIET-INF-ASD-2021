from copy import deepcopy


# O(n^2)
def dfs(graph, degrees):
  n = len(graph)
  # visited[u][v] - czy krawedz u -> v zostala odwiedzona
  # graf jest nieskierowany wiec visited[u][v] = visited[v][u]
  visited = [[0 for _ in range(n)] for _ in range(n)] # O(n^2)

  # last_considered[i] - ostatni wierzcholek rozpatrzony bedac w wierzcholu i.
  # dzieki przechowywaniu tej informacji dla kazdego z n wierzcholkow
  # wykonamy sumarycznie n operacji w dfs_visit(), poniewaz
  # bedziemy zapamietywali stan petli
  last_considered = [-1]*n

  cycle = []

  def dfs_visit(u):
    nonlocal graph, n, degrees, visited, last_considered, cycle

    for v in range(last_considered[u]+1, n):
      # nadpisujemy wartosc ostatniego rozpatrzonego juz w tym miejscu,
      # poniewaz jezeli ponizszy warunek zostanie spelniony to bedziemy
      # mieli nieaktualna wartosc w nastepnym wywolaniu dfs_visit()
      last_considered[u] += 1

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

  # dfs_visit(0) zakonczy sie kiedy odwiedzone zostana wszystkie krawedzie.
  # dla kazdego wierzcholka (n) sprawdzimy wszystkie mozliwe krawedzie (n - 1).
  # dzieki spamietywaniu rozpatrzonych wierzcholkow, o ktorym juz wspominalem 
  # nie sprawdzimy wiecej niz raz kazda krawedz.
  # podsumowujac: zlozonosc czasowa ponizszej operacji to O(n^2)
  dfs_visit(0)

  return cycle


# O(n^2)
def euler( G ):
  n = len(G)

  # nie spelnia definicji cyklu (min stopien < 2)
  if n == 0:
    return None

  degrees = [0]*n # O(n)

  # wyznaczamy stopnie wierzcholkow
  for i in range(n): # O(n)
    for j in range(n): # O(n)
      degrees[i] += G[i][j]

    # jezeli ktorys z wierzcholkow nie posiada parzystego stopnia  lub
    # graf nie jest spojny
    # to graf nie posiada cyklu Eulera
    if degrees[i]%2 == 1 or degrees[i] == 0:
      return None

  cycle = dfs(G, degrees) # O(n^2)

  # print(cycle)

  return cycle
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

# [0, 2, 5, 3, 1, 5, 4, 2, 1, 0]
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]

# testy =======================================================================
# [0, 5, 4, 1, 5, 2, 0, 4, 3, 1, 0]
# G = [[0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0]]

# [0, 4, 5, 6, 2, 5, 1, 6, 7, 3, 2, 1, 0]
# G = [[0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]]

# [0, 4, 5, 3, 4, 2, 0, 3, 1, 0]
# G = [[0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]

# None
# G = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]

# None
# G = []
# end testy ===================================================================

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
