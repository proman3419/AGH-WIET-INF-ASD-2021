# algorytm
# priorytezujemy zadania o najwyzszym zysku, umieszczamy je jak najpozniej mozemy,
# zeby zajmowac jak najmniej miejsca dla zadan, ktore bedziemy musieli wykonac wczesniej


# dowod
# zal T posortowana po zysku malejaco
# zal, ze istnieje taka permutacja dwoch dowolnych zadan i, j w rozwiazaniu, ze
# zwiekszy ona zysk
# zal i < j

# zamiana dwoch elementow nie wplywa na zysk pozostalych.
# mozemy wiec rozpatrzec tylko jak zachowywac sie bedzie zysk dla zadan i oraz j, mamy 4 mozliwe przypadki:

# jezeli d[i] < j oraz j <= d[j]:
# tracimy g[i], g[j] pozostaje bez zmian poniewaz
# z zal przypadku j < d[j] oraz z zal dowodu i < j => i < j < d[j] czyli po zamianie nadal j < d[j]
# w tej sytuacji nowe rozwiazanie jest gorsze od proponowanego

# jezeli d[i] < j oraz j > d[j]:
# tracimy g[i], potencjalnie zyskujemy g[j], ale w takiej sytuacji g[i] > g[j]
# w tej sytuacji nowe rozwiazanie jest gorsze od proponowanego

# jezeli d[i] >= j oraz j <= d[j]:
# nie tracimy g[i] ani g[j]
# w tej sytuacji nowe rozwiazanie jest takie samo jak proponowane

# jezeli d[i] >= j oraz j > d[j]:
# nie tracimy g[i], nie zyskujemy ani nie tracimy g[j]
# w tej sytuacji nowe rozwiazanie jest takie samo jak proponowane

# podsumowujac proponowane rozwiazanie jest co najmniej rowne optymalnemu 


def tasks_with_deadlines(T):
  n = len(d)
  T.sort(key=lambda x: x[1], reverse=True) # sortujemy po zysku

  print(f'T po posortowaniu: {T}')

  profit = 0
  order = [-1]*n
  for i in range(n):
    j = T[i][0]
    while j > 0 and order[j] != -1:
      j -= 1

    if order[j] == -1:
      order[j] = T[i]
      profit += T[i][1]

  return (profit, order)


d = [5, 4, 4, 3, 1, 2] # terminy wykonania
g = [8, 7, 5, 4, 4, 2] # nagrody wykonania
T = list(zip(d, g))

# -1 w rozwiazaniu oznacza, ze mozemy umiescic tam zadanie o jakimkolwiek id, poza tymi o ustalonej kolejnosci
print(tasks_with_deadlines(T))
