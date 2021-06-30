from math import *


C =  [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]


def dist(p1, p2):
  return ((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**(1/2)


# zdecydowalem sie na zagniezdzone funkcje i zmienne nonlocal
# dla zwiekszenia czytelnosci (nie trzeba przekazywac w kazdym wywolaniu
# funkcji rekurencyjnych tablic)
# O(n^2)
def bitonicTSP( C ):
  n = len(C)
  # brak miast => dystans = 0, brak miast do wyswietlenia
  if n == 0:
    print('0')
    return

  # 1 miasto => dystans = 0, zaczynamy i konczymy w tym samym
  if n == 1:
    print(f'{C[0][0]}\n0')
    return

  # sortujemy tablice miast po wspolrzednej x
  C = sorted(C, key=lambda x: x[1])

  # generujemy tablice dystansow
  D = [[0 for _ in range(n)] for _ in range(n)] # O(n^2)
  # porzebujemy tylko prawego, gornego trojkata poniewaz dla wszystkich rozpatrywanych przez nas sytuacji i < j
  for i in range(n): # O(n)
    for j in range(i+1, n): # O(n)
      D[i][j] = dist(C[i], C[j])

  # F[i][j] - minimalny koszt sciezek 0 -> i, 0 -> j takich, ze lacznie te sciezki odwiedza kazde miasto ze zbioru {1, ..., j} dokladnie raz, i < j
  # i - ostatnie miasto sciezki pierwszej
  # j - ostatnie miasto sciezki drugiej
  F = [[inf for _ in range(n)] for _ in range(n)] # O(n^2)

  # jest to droga pomiedzy dwoma miastami pomiedzy ktorymi nie wystepuje
  # zadne inne miasto, dlatego mozemy wyrazic odleglosc jako zwykla euklidesowa
  F[0][1] = D[0][1]

  # tablica miast przelomowych (czyli takich, na ktorych zmienia sie przynaleznosc miast do sciezki z jednej na druga).
  # miasta pomiedzy dwoma miastami przelomowymi,
  # (albo od poczatku do miasta przelomowego/od ostatniego miasta przelomowego do konca),
  # naleza do tej samej sciezki.
  # P[i] - indeks najblizszego miasta przelomowego dla sciezki konczacej sie w i, musi znajdowac sie przed miastem i.
  # wystarczy zapamietywac dla i == j - 1 poniewaz wczesniej rozpatrzymy taki przypadek
  # niz bedziemy musieli z tej informacji skorzystac.
  # spamietywanie dla kazdego i, j jest nieefektywne
  P = [-1]*n # O(n)

  # funkcje ===================================================================
  # implementacja z wykladu z dodatkami koniecznymi do odzyskania sciezki rozwiazania
  # O(n)
  def tspf(i, j):
    nonlocal F, C, D, P

    # jezeli obliczylismy juz wartosc to ja zwracamy
    if F[i][j] != inf:
      return F[i][j]

    # dla i == j - 1
    # k - pierwsze miasto idac od j do 0 takie, ze znajduje sie na dluzszej sciezce
    # k < j - 1
    # F[j-1][j] = min(F[k][j-1] + dist(k, j))
    if i == j - 1:
      best = inf
      for k in range(j-1):
        curr = tspf(k, j-1) + D[k][j]
        if curr < best:
          # zapisujemy min dystans oraz indeks miasta, ktory jest przelomowym
          best = curr
          P[i] = k
      F[j-1][j] = best
    # dla i < j - 1
    # F[i][j] = F[i][j-1] + dist(j-1, j)
    else:
      # dla i < j - 1 nie zapisujemy indeksu miasta przelomowego
      # poniewaz bedziemy go szukac przy rozpatrywaniu i == j - 1
      F[i][j] = tspf(i, j-1) + D[j-1][j]

    return F[i][j]

  # O(n)
  def get_solution(l_len, s_len, i, j, l_add):
    nonlocal F, P, path

    # jezeli wyszlibysmy poza zakres tablicy
    if i < 0 or j < 0:
      return (l_len, s_len)

    # dodajemy miasta do obecnej podsciezki tak dlugo az nie
    # dotrzemy do przelomowego miasta
    while j > i:
      if l_add:
        path[l_len] = j
        l_len += 1
      else:
        path[-s_len-1] = j
        s_len += 1
      j -= 1

    # jezeli jedna z podsciezek juz sie skonczyla
    if i*j == 0:
      return (l_len, s_len)

    # j == i => dotarlismy do przelomowego miasta,
    # od nastepnego miasta zaczynaja sie elementy nalezace do drugiej podsciezki, dlatego zmieniamy flage l_add.
    # zmienia sie tez zakres, w ktorym sie poruszamy,
    # P[i] przechowuje wczesniejsze miasto przelomowe, i jest tym, do ktorego dazylismy w obecnym wywolaniu
    return get_solution(l_len, s_len, P[i], i, not l_add)

  # O(n)
  def print_solution(l_len, s_len):
    nonlocal C, path

    # zaczynamy w miescie 0
    print(C[0][0], end=', ')
    # najpierw idziemy od miasta 0 do n-1.
    # zapisywalismy miasta w podsciezkach idac od tylu,
    # dlatego odczytujemy miasta idac od konca podsciezki.
    # (idac od tylu po elementach zapisanych w odwrotnej kolejnosci niwelujemy zapisywanie od tylu)
    for i in range(l_len-1, -1, -1):
      print(C[path[i]][0], end=', ')

    # teraz idziemy od miasta n-1 do miasta 0.
    # nie przeszkadza nam odwrocona kolejnosc podsciezki poniewaz cofamy sie
    for i in range(s_len):
      print(C[path[-i-1]][0], end=', ')
    # konczymy w miescie 0
    print(C[0][0])
  # end funkcje ===============================================================

  min_res = inf
  min_i = -1
  # rozwiazanie (dlugosc sciezki)
  # min(F[i][n-1] + dist(i, n-1))
  for i in range(n-1): # O(n)
    res = tspf(i, n-1) + D[i][n-1] # O(n)

    if res < min_res:
      min_res = res
      min_i = i

  # rozwiazanie (sciezka)
  # bedzie sie skladalo z dwoch podsciezek, jednej krotszej i drugiej dluzszej.
  # rozne dlugosci wynikaja z faktu, ze jedna konczy sie w miescie i, druga w miescie j oraz i < j
  # z czego wynika, ze ta konczaca sie w j jest dluzsza.
  # dluzsza podsciezke bedziemy zapisywali od poczatku tablicy, krotsza od konca
  path = [-1]*n # O(n)
  l_len = 0 # dlugosc dluzszej
  s_len = 0 # dlugosc krotszej
  l_add = True # flaga mowiaca do ktorej podsciezki dodajemy

  # zapisuje do path podsciezki
  l_len, s_len = get_solution(l_len, s_len, min_i, n-1, l_add) # O(n)

  # wyswietla rozwiazanie (sciezke)
  print_solution(l_len, s_len) # O(n)

  # wyswietla rozwiazanie (dlugosc sciezki)
  print(min_res)


bitonicTSP( C )
