# O(n^2)
def lis(A, n):
  # sprawdzam tablice od tylu, zeby pierwsze elementy podciagow rosnacych
  # mialy maksymalne F[i], przy printowaniu podciagow szukam maksymalnych F[i] i od nich zaczynam wypisywanie
  # gdybym nie przechodzil po tablicy od ostatniego indeksu to maksymalne F[i]
  # mialyby elementy koncowe podciagow w efekcie czego printowalbym je od tylu

  # dlatego, ze przechodze przez tablice od ostatniego indeksu musze szukac
  # podciagow malejacych (ktore przy printowaniu w normalnej kolejnosci beda rosnacymi)

  # F[i] - dlugosc najdluzszego malejacego podciagu konczacego sie na A[i]
  # kazdy element tworzy sam w sobie podciag o dlugosci 1
  F = [1]*n # O(n)

  # P[i] - tablica indeksow, pod ktorymi znajduja sie mozliwe poprzednie elementy podciagu
  P = [[] for _ in range(n)] # O(n)

  for i in range(n-1, -1, -1): # O(n)
    for j in range(i+1, n): # O(n)
      # jezeli:
      # - j-ty element moze stworzyc z najdluzszym podciagiem malejacym konczacym sie na A[i] podciag malejacy
      # - nowy podciag bedzie dluzszy lub rowny obecnemu najdluzszemu podciagowi konczacemu sie na A[i]
      if A[j] > A[i] and F[j] + 1 >= F[i]:
        # dopisujemy indeks elementu do podciagu
        P[i].append(j) # zamortyzowane O(1)

        # jezeli nowy podciag jest dluzszy niz byl to zapisujemy nowa dlugosc
        if F[j] + 1 != F[i]:
          F[i] = F[j] + 1

  # szukamy maksymalnej dlugosci podciagu
  _max = F[0]
  for i in range(1, n): # O(n)
    if F[i] > _max:
      _max = F[i]

  return (F, P, _max)


# ciezko okreslic O
def print_solution(A, P, _max, res, cnt, i, j):
  # gdy doszlismy do konca podciagu to go printujemy, zwiekszamy licznik i go zwracamy
  if j == _max:
    for k in range(j):
      print(res[k], end=' ')
    print()

    return cnt + 1

  # dla wszystkich mozliwych kontynuacji podciagu
  for k in range(len(P[i])):
    res[j] = A[P[i][k]]
    # kontynuujemy szukanie jego kolejnych elementow
    cnt = print_solution(A, P, _max, res, cnt, P[i][k], j+1)

  return cnt


# conajmniej O(n^2)
def printAllLIS(A):
  n = len(A)
  # jesli tablica jest pusta to konczymy
  if n == 0: return 0

  # tworzymy tablice F i P (opisane w lis)
  F, P, _max  = lis(A, n) # O(n^2)
  # tablica, ktora bedzie przechowywala wynik
  res = [0]*n # O(n)
  # licznik podciagow
  cnt = 0 

  print('podciagi:')
  for i in range(n): # O(n)
    # jezeli na obecnym indeksie konczy sie podciag malejacy
    if F[i] == _max:
      res[0] = A[i]
      # to printujemy go w odwrotnej kolejnosci otrzymujac podciag rosnacy
      cnt += print_solution(A, P, _max, res, 0, i, 1) # ciezko okreslic O
  print()

  return cnt


A = [2, 1, 4, 3]

print(f'tablica: {A}\n')
print(f'ilosc: {printAllLIS(A)}')
