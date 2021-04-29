# obliczyc minimalna ilosc tankowan, zeby dojechac do t
def tank_a(L, S, P, n, t):
  # jezeli mamy wiecej paliwa niz potrzebujemy lub idealnie na dotarcie to nie musimy tankowac
  if L >= t:
    return (0, [0, t])

  pos = 0 # obecna pozycja
  next_s = 0 # nastepna stacja do odwiedzenia
  cnt = 0
  path = []

  # dopoki nie dojedziemy do ostatniej stacji lub nie osiagniemy celu
  while next_s != n and pos < t:
    curr_s = next_s
    # szukamy nastepnej, najdalszej stacji, do ktorej mozemy dojechac
    while curr_s < n-1 and S[curr_s+1] - pos <= L:
      curr_s += 1

    # jezeli mozemy do niej dojechac to do niej jedziemy
    if S[curr_s] - pos <= L:
      pos = S[curr_s]
      cnt += 1
      next_s = curr_s + 1
      path.append(S[curr_s])
    # jezeli nie to nie ma sensu rozpatrywac nastepnych stacji
    else:
      break

  # na tym etapie albo dojechalismy do ostatniej stacji i patrzymy, czy mozemy z niej dojechac do celu majac pelen bak
  # albo (pos >= t) <=> (t - pos <= 0 <= L)
  if t - pos <= L:
    path.append(t)
    return (cnt, path)
  else:
    return (-1, None)


# zakladam, ze stacje sa w posortowanej kolejnosci
S = [2, 7, 12, 15, 20] # odleglosci stacji od punktu 0
P = [4, 3, 10, 1, 4] # koszty paliw na poszczegolnych stacjach
n = len(S) # ilosc stacji
L = 100 # pojemnosc baku
t = 50 # pole, do ktorego chcemy dojechac

print(tank_a(L, S, P, n, t))
