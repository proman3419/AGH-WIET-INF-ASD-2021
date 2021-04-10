# n + n + max_w + n*max_w = O(n*max_w + 2n + max_w)
def knapsack(P, W, max_w):
  # tworzymy tablice, w ktorej:
  # wiersze - do ktorego przedmiotu juz rozwazylismy
  # kolumny - jaka waga zostala wykorzystana
  # wartosc pola - profit
  n = len(W)
  F = [None]*n # O(n)
  for i in range(n): # O(n)
    F[i] = [0]*(max_w+1)

  # dla pierwszego rzedu problem jest trywialny
  # jezeli tylko waga nam na to pozwala to bierzemy przedmiot
  # P[0] > 0
  for w in range(W[0], max_w+1): # O(max_w+1-W[0]) <= O(max_w)
    F[0][w] = P[0]

  for i in range(1, n): # O(n)
    for w in range(1, max_w+1): # O(max_w)
      # jezeli nie wezmiemy przedmiotu to profit bedzie rowny profitowi
      # dla poprzedniego przedmiotu i tej samej wykorzystanej wadze
      F[i][w] = F[i-1][w]

      # jezeli obecna waga pozwala nam na wziecie obecnego przedmiotu
      if w >= W[i]:
        # to rozwazamy sytuacje gdy go bierzemy lub nie
        F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])

  return (F, F[n-1][max_w])


def get_solution(F, P, W, i, w):
  if i == 0:
    if w >= W[0]: return [0]
    return []

  if w >= W[i] and F[i][w] == F[i-1][w-W[i]] + P[i]:
    return get_solution(F, P, W, i-1, w-W[i]) + [i]
  return get_solution(F, P, W, i-1, w)


P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
max_w = 24

res = knapsack(P, W, max_w)
print(get_solution(res[0], P, W, len(W)-1, max_w))
