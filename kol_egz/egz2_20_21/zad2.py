# t: O(n) 
# s: O(n)

# w drzewie ilosc krawedzi jest ograniczona przez ilosc wierzcholkow (n), 
# najwiekszy czynnik tego algorytmu to ilosc krawedzi wiec zlozonosc czasowa bedzie O(n)


# dodajemy nowe pole w node - sum, bedzie ona przechowywac wage drzewa,
# ktorego korzeniem jest ten node.
# obliczamy wagi poddrzew rekurencyjnie odwolujac sie w glab drzewa.

# majac obliczone wagi nodow w drzewie rozpatrujemy jak beda wygladaly
# wagi obu drzew po usunieciu krawedzi (rozpatrujemy dla kazdej krawedzi).

# po rozdzieleniu glownego drzewa na dwa:

# zeby obliczyc wage drzewa z glownym korzeniem nalezy zastosowac wzor:
# root_sum - edge_w - subroot_sum,
# gdzie:
# - root_sum - waga drzewa zaczynajacego sie w glownym korzeniu
# - edge_w - waga usuwanej krawedzi
# - subroot_sum - waga drzewa, do ktorego prowadzi usuwana krawedz

# waga drugiego drzewa jest zawarta w jego polu sum.

# minimalizujemy abs roznicy z tych wag i zwracamy indeks, dla ktorego wystapil


from zad2testy import runtests
from math import inf


class Node:
  def __init__( self ):   # stwórz węzeł drzewa
    self.edges   = []     # lista węzłów do których są krawędzie
    self.weights = []     # lista wag krawędzi
    self.ids     = []     # lista identyfikatorów krawędzi
    self.sum     = 0      # suma wag drzewa o korzeniu w obecnym nodzie
      
  def addEdge( self, x, w, id ): # dodaj krawędź z tego węzła do węzła x
    self.edges.append( x )       # o wadze w i identyfikatorze id
    self.weights.append( w ) 
    self.ids.append( id )


def init_sums(tree):
  if tree is None:
    return 0

  n = len(tree.edges)
  _sum = 0
  for i in range(n):
    _sum += tree.weights[i]
    _sum += init_sums(tree.edges[i])

  tree.sum = _sum

  return _sum


def balance( T ):
  init_sums(T)

  best_diff = inf
  best_diff_id = -1

  def rec(tree):
    nonlocal best_diff, best_diff_id, T

    if tree is None:
      return

    n = len(tree.edges)

    for i in range(n):
      curr_diff = abs((T.sum - tree.weights[i] - tree.edges[i].sum) - tree.edges[i].sum)
      if curr_diff < best_diff:
        best_diff = curr_diff
        best_diff_id = tree.ids[i]

      rec(tree.edges[i])

  rec(T)

  return best_diff_id

  
runtests( balance )
