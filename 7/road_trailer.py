# algorytm
# sortujemy tablice wag nierosnaco.
# przechodzimy nastepnie po niej i, jezeli mozemy, bierzemy przedmioty na przyczepe


# dowod
# wybierzmy najwieksza wage, ktora mozemy wziac i oznaczmy ja jako t.
# zeby uzyskac mase > t za pomoca mniejszych elementow musielibysmy zlozyc z nich najpierw t.

# dobrze to widac, jezeli zinterpretujemy wagi w postaci binarnej, przyklad:
# t = 1000
# u = 10001 = 10000 + 00001 = 1000 + 1000 + 00001

# moglibysmy rozbijac u na wieksze sumy, ale byloby to rownoznaczne z przedstawianiem
# tej samej wagi za pomoca wiekszej ilosci wag.
# z warunkow zadania powinnismy faworyzowac takie, ktore sklada sie z najmniejszej ilosci wag.


def road_trailer(K, w):
  n = len(w)
  w.sort(reverse=True)
  total_weight = 0
  items = []

  for i in range(n):
    if w[i] <= K:
      K -= w[i]
      total_weight += w[i]
      items.append(w[i])

  return (total_weight, items)


K = 27
w = [2, 2, 4, 8, 1, 8, 16]

print(road_trailer(K, w))
