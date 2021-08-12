from copy import deepcopy
from collections import deque


# O(n^2)
def dfs(graph):
  n = len(graph)
  # visited[u][v] - czy krawedz u -> v zostala odwiedzona
  # graf jest nieskierowany wiec visited[u][v] = visited[v][u]
  visited = [[0 for _ in range(n)] for _ in range(n)] # O(n^2)

  # last_considered[i] - ostatni wierzcholek rozpatrzony bedac w wierzcholu i.
  # dzieki przechowywaniu tej informacji dla kazdego z n wierzcholkow
  # wykonamy sumarycznie n operacji w petli dfs_visit, poniewaz bedziemy zapamietywali stan petli wewnetrznej
  last_considered = [-1]*n

  # lista z rozwiazaniem
  cycle = []

  # na tym etapie pewnym jest, ze graf posiada cykl Eulera (przypadek przeciwny odrzucilismy w glownej funkcji).
  # dla grafow niespojnych musimy znalezc wierzcholek, z ktorego zaczniemy
  for u in range(n):
    edges_cnt = 0
    for v in range(n):
      edges_cnt += graph[u][v]
      
    if edges_cnt != 0:
      stack = [u]
      break

  # petla dfs_visit zakonczy sie kiedy odwiedzone zostana wszystkie krawedzie.
  # dla kazdego wierzcholka (n) sprawdzimy wszystkie mozliwe krawedzie (n).
  # dzieki spamietywaniu rozpatrzonych wierzcholkow, o ktorym juz wspominalem 
  # nie sprawdzimy wiecej niz raz kazda krawedz.
  # podsumowujac: zlozonosc czasowa petli dfs_visit to O(n^2)

  # dfs_visit iteracyjnie
  while len(stack) > 0:
    u = stack[-1]
    v = last_considered[u] + 1

    while v < n:
      # nadpisujemy wartosc ostatniego rozpatrzonego wierzcholka z u
      last_considered[u] += 1

      # jezeli krawedz istnieje i nie zostala odwiedzona
      if graph[u][v] == 1 and visited[u][v] == 0:
        # zaznaczamy, ze ja odwiedzilismy
        visited[u][v] = visited[v][u] = 1

        # odwiedzamy nastepny wierzcholek, realizujemy to przez:
        # - dodanie go na stos
        stack.append(v)
        # - nadpisanie wierzcholka, z ktorego teraz rozpatrujemy
        u = v
        # - nadpisanie wierzcholka, z ktorym sprawdzamy krawedz
        v = last_considered[u] + 1
      # jezeli krawedz nie istnieje lub nie zostala odwiedzona to przechodzimy
      # do nastepnego wierzcholka, z ktorym bedziemy sprawdzali krawedz
      else:
        v += 1

    # jezeli skonczylismy przetwarzac obecny wierzcholek to dodajemy go do cyklu
    cycle.append(u) # zamortyzowane O(1)
    # i usuwamy ze stosu
    stack.pop()

  return cycle


# O(n^2)
def check_if_even_degrees(graph):
  n = len(graph)

  for i in range(n): # O(n)
    degree = 0
    for j in range(n): # O(n)
      degree += graph[i][j]

    if degree%2 == 1:
      return False

  return True


# O(n^2)
def bfs(graph, s):
  n = len(graph)
  queue = deque()
  visited = [False]*n

  visited[s] = True
  queue.append(s)

  while queue:
    u = queue.popleft()
    for v in range(n):     
      if graph[u][v] == 1 and not visited[v]:
        visited[v] = True
        queue.append(v)

  return visited


# O(n^2)
def check_if_has_euler(graph):
  # pusty graf
  if len(graph) == 0:
    # print('empty')
    return False

  # jezeli graf nie ma wszystkich wierzcholkow parzystego stopnia
  if not check_if_even_degrees(graph): # O(n^2)
    # print('not all degrees are even')
    return False
  # to nie posiada cyklu Eulera

  return True


# O(n^2)
def euler( G ):
  cycle = None

  if check_if_has_euler(G): # O(n^2)
    cycle = dfs(G) # O(n^2)
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
