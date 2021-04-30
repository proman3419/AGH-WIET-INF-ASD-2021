# algorytm
# sortujemy wartosci a nastepnie przechodzimy po nich i jezeli nie mamy przedzialu,
# w ktorym zawieralby sie element to tworzymy nowy i dodajemy do niego elementy tak dlugo
# az nie beda wieksze o > 1 od poczatkowego


# dowod
# zal R - rozwiazanie opisywanego algorytmu, R* - rozwiazanie optymalne
# zal X posortowane
# zal X[i+1] >= X[i]
# dla kazdego elementu X[i], X[i+1] mamy 2 przypadki:

# jezeli X[i+1] - X[i] > 1:
# X[i+1] zaczyna nowy przedzial, w R* tez musi zostac utworzony
# nowy przedzial poniewaz nie jestesmy w stanie umiescic dwoch elementow rozniacych sie o > 1 w jednym.
# wynika z tego, ze dla tego przypadku R i R* zachowuja sie tak samo

# jezeli X[i+1] - X[i] <= 1:
# X[i+1] zawiera sie w przedziale, do ktorego nalezy X[i].
# nie zwiekszamy wiec ilosci przedialow w tym przypadku

# skoro dodajemy przedzialy w R wtw dodajemy w R* i dla pozostalych przypadkow
# nie zmieniamy liczby przedzialow dla R to rozwiazanie R jest co najmniej optymalnym


def cover_with_ranges(X):
  X.sort()
  n = len(X)
  cnt = curr = 0
  ranges = []

  while curr < n:
    start = end = curr
    while curr < n and X[curr] - X[start] <= 1:
      end = curr
      curr += 1

    ranges.append((X[start], X[start]+1))
    cnt += 1

  return (cnt, ranges)


X = [0.25, 1.6, 0.5]
print(cover_with_ranges(X))
