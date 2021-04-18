from math import *


#C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]

C = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]

def dist(p1, p2):
  return ((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**(1/2)


def bitonicTSP( C ):
  # sortujemy tablice miast po wspolrzednej x
  C = sorted(C, key=lambda x: x[1])
  n = len(C)

  # F[i][j] - minimalny koszt sciezek 0 -> i, 0 -> j takich, ze lacznie te sciezki odwiedza kazde miasto ze zbioru {1, ..., j} dokladnie raz
  # i - ostatnie miasto sciezki pierwszej
  # j - ostatnie miasto sciezki drugiej
  F = [[(inf, None) for _ in range(n)] for _ in range(n)] # O(n^2)

  # jest to droga pomiedzy dwoma miastami pomiedzy ktorymi nie wystepuje
  # zadne inne miasto, dlatego mozemy wyrazic odleglosc jako zwykla euklidesowa
  F[0][1] = (dist(C[0], C[1]), None)

  # implementacja z wykladu z dodatkami koniecznymi do odzyskania sciezki rozwiazania
  def tspf(i, j):
    nonlocal F, C

    # jezeli obliczylismy juz wartosc to ja zwracamy
    if F[i][j][0] != inf:
      return F[i][j][0]

    # dla i == j - 1
    # k - pierwsze miasto idac od j do 0 takie, ze znajduje sie na dluzszej sciezce
    # k < j - 1
    # F[j-1][j] = min(F[k][j-1] + dist(k, j))
    if i == j - 1:
      best = (inf, None)
      for k in range(j-1):
        curr = tspf(k, j-1) + dist(C[k], C[j])
        if curr < best[0]:
          # zapisujemy min dystans oraz indeks miasta, ktory jest przelomowym.
          # miasta pomiedzy dwoma miastami przelomowymi,
          # (albo od poczatku do miasta przelomowego/od ostatniego miasta przelomowego do konca),
          # naleza do tej samej sciezki
          best = (curr, k)
      F[j-1][j] = best
    # dla i < j - 1
    # F[i][j] = F[i][j-1] + dist(j-1, j)
    else:
      # dla i < j - 1 nie zapisujemy indeksu miasta przelomowego
      # poniewaz bedziemy go szukac przy rozpatrywaniu i == j - 1
      F[i][j] = (tspf(i, j-1) + dist(C[j-1], C[j]), None)

    return F[i][j][0]

  def get_solution(_long, short, i, j):
    nonlocal F

    # jezeli wyszlibysmy poza zakres tablicy
    if i < 0 or j < 0:
      return

    # dodajemy miasta do obecnej sciezki dluzszej tak dlugo az nie
    # dotrzemy do przelomowego miasta
    while j > i:
      _long.append(j)
      j -= 1

    # jezeli jedna z podsciezek juz sie skonczyla
    if i*j == 0:
      return

    # j == i => dotarlismy do przelomowego miasta,
    # od nastepnego miasta zaczynaja sie elementy nalezace do drugiej podsciezki,
    # dlatego w nastepnym wywolaniu zamieniamy podsciezke krotsza z dluzsza
    # zmienia nam sie tez zakres, w ktorym sie poruszamy,
    # F[i][i+1][1] przechowuje wczesniejsze miasto przelomowe, i jest tym, do ktorego dazylismy w obecnym wywolaniu.
    get_solution(short, _long, F[i][i+1][1], i)


  def print_solution(_long, short):
    nonlocal C

    # zaczynamy w miescie 0
    print(C[0][0], end=', ')
    # najpierw idziemy od miasta 0 do n-1.
    # zapisywalismy miasta w podsciezkach idac od tylu,
    # dlatego odczytujemy miasta idac od konca podsciezki.
    # (idac od tylu po elementach zapisanych w odwrotnej kolejnosci niwelujemy zapisywanie od tylu)
    for i in range(len(short)-1, -1, -1):
      print(C[short[i]][0], end=', ')

    # teraz idziemy od miasta n-1 do miasta 0.
    # nie przeszkadza nam odwrocona kolejnosc podsciezki poniewaz cofamy sie
    for i in range(len(_long)):
      print(C[_long[i]][0], end=', ')
    # konczymy w miescie 0
    print(C[0][0])

  min_res = inf
  min_i = -1
  # rozwiazanie (dlugosc sciezki)
  # min(F[i][n-1] + dist(i, n-1))
  for i in range(n-1):
    res = tspf(i, n-1) + dist(C[i], C[n-1])

    if res < min_res:
      min_res = res
      min_i = i

  # rozwiazanie (sciezka)
  # bedzie sie skladalo z dwoch podsciezek, jednej krotszej i drugiej dluzszej
  # rozne dlugosci wynikaja z faktu, ze jedna konczy sie w miescie i, druga w miescie j oraz i < j
  # z czego wynika, ze ta konczaca sie w j jest dluzsza
  _long = []
  short = []

  # zapisuje do _long i short podsciezki
  get_solution(_long, short, min_i, n-1)

  # wyswietla rozwiazanie (sciezke)
  if len(_long) > len(short):
    print_solution(_long, short)
  else:
    print_solution(short, _long)    

  print(min_res)


bitonicTSP( C )
