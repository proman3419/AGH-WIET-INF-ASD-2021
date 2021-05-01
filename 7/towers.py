# algorytm
# sortujemy klocki kazdego dziecka a nastepnie odbieramy temu, ktory ma
# najdluzszy, powtarzamy az mamy klocki o najdluzszej lacznej dlugosci


# dowod
# warunkiem koncowym algorytmu jest posiadanie najwyzszej wiezy, dlatego nie trzeba tego udowadniac.
# nalezy sie skupic na tym, czy faktycznie osiagniemy to kradnac najmniejsza ilosc klockow.
# w kazdym momencie, kiedy chcemy podebrac klocek najbardziej oplaca nam sie
# wziac najdluzszy (oznaczmy go litera l).
# gdybysmy wybrali jakikolwiek inny klocek (oznaczmy go litera s) oraz wiemy, ze s < l to
# tracimy l - s wysokosci, ktore moglibysmy dobrac w obecnym kroku.
# dobranie s zamiast l nie przynosi tez korzysci w nastepnych krokach


def find_max_sum(m, w):
  _max_i = 0
  for i in range(1, m):
    if w[i][1] > w[_max_i][1]:
      _max_i = i

  return _max_i


def find_max_height(m, k, w):
  _max_i = 0
  for i in range(m):
    if i != k:
      if w[i][2] >= 0:
        if w[i][0][-1] > w[_max_i][0][-1]:
          _max_i = i

  return _max_i


def print_result(m, k, w):
  for i in range(m):
    print(f'i: {i}, sum: {w[i][1]}, klocki:', end=' ')
    for j in range(w[i][2]+1):
      print(w[i][0][j], end=' ')
    print()


# O(m^2 + O(len(w[i])))
def steal_bricks(m, k, w):
  for i in range(m):
    w[i] = [sorted(w[i]), sum(w[i]), len(w[i])-1] # O(len(w[i]))

  while find_max_sum(m, w) != k: # O(m)
    _max_h_i = find_max_height(m, k, w) # O(m)

    w[k][0].append(w[_max_h_i][0][w[_max_h_i][2]]) # zamortyzowany O(1)
    w[k][1] += w[k][0][-1]
    w[k][2] += 1

    w[_max_h_i][1] -= w[k][0][-1]
    w[_max_h_i][2] -= 1

  return w


m = 4
k = 2
w = [[1, 7, 3, 2],
     [4, 9, 2],
     [3, 15, 6, 7, 1],
     [20]]

w = steal_bricks(m, k, w)
print_result(m, k, w)
