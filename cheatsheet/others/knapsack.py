from math import inf


# O(n*max_w)
def knapsack(P, W, max_w):
  n = len(W)
  if n == 0:
    return (None, 0)

  # F[i][w] - max profit rozwazajac do i-tego przedmiotu z wykorzystana waga w
  F = [[0 for _ in range(max_w+1)] for _ in range(n)] # O(n*max_w)

  for w in range(W[0], max_w+1): # O(max_w)
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


# 51
# [0, 6, 9, 13, 15]
W = [4, 5, 12, 9, 10, 13, 5, 8, 7, 3, 6, 13, 23, 5, 34, 23, 12]
P = [10, 2, 4, 5, 3, 4, 8, 4, 2, 10, 4, 10, 12, 4, 16, 19, 4]
max_w = 40

F, res = knapsack(P, W, max_w)
print(res)
if res != 0:
  print(get_solution(F, P, W, len(W)-1, max_w))
