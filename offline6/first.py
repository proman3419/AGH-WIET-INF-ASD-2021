from math import *

C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]


def dist(p1, p2):
  return ((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**(1/2)


def bitonicTSP( C ):
  # sortujemy tablice miast po wspolrzednej x
  C = sorted(C, key=lambda x: x[1])
  n = len(C)

  # F[i][j] - minimalny koszt sciezek 0 -> i, 0 -> j takich, ze lacznie te sciezki odwiedza kazde miasto ze zbioru {1, ..., j} dokladnie raz
  # i - ostatnie miasto sciezki pierwszej (krotszej)
  # j - ostatnie miasto sciezki drugiej (dluzszej)
  
  F = [[inf for _ in range(n)] for _ in range(n)] # O(n^2)

  # jest to droga pomiedzy dwoma miastami pomiedzy ktorymi nie wystepuje
  # zadne inne miasto, dlatego mozemy wyrazic odleglosc jako zwykla euklidesowa
  F[0][1] = dist(C[0], C[1])

  def tspf(i, j):
    nonlocal F, C

    if F[i][j] != inf:
      return F[i][j]

    # dla i == j - 1
    # k - pierwsze miasto idac od j do 0 takie, ze znajduje sie na dluzszej sciezce
    # k < j - 1
    # F[j-1][j] = min(F[k][j-1] + dist(k, j))
    if i == j - 1:
      best = inf
      for k in range(j-1):
        best = min(best, tspf(k, j-1)) + dist(C[k], C[j])
      F[j-1][j] = best
    # dla i < j - 1
    # F[i][j] = F[i][j-1] + dist(j-1, j)
    else:
      F[i][j] = tspf(i, j-1) + dist(C[j-1], C[j])

    return F[i][j]

  min_res = inf
  for i in range(n-1):
    # rozwiazanie
    # min(F[i][n-1] + dist(i, n-1))
    res = tspf(i, n-1) + dist(C[i], C[n-1])
    if res < min_res:
      min_res = res

  return min_res


bitonicTSP( C )
