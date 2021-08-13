# V - wartosci, W - wagi, H - wysokosci
def knapsack_3d(V, W, H, max_w, max_h):
  n = len(V)
  # F[i][w][h] - max profit rozwazajac do i-tego przedmiotu z wykorzystana waga w i wysokoscia h
  F = [[[0 for _ in range(max_h+1)] for _ in range(max_w+1)] for _ in range(n)]

  for w in range(W[0], max_w+1):
    for h in range(H[0], max_h+1):
      F[0][w][h] = V[0]

  for i in range(1, n):
    for w in range(1, max_w+1):
      for h in range(H[0], max_h+1):
        F[i][w][h] = F[i-1][w][h] # nie bierzemy

        if w >= W[i] and h >= H[i]:
          F[i][w][h] = max(F[i][w][h], F[i-1][w-W[i]][h-H[i]] + V[i]) # bierzemy (jezeli sie oplaca)

  return (F, F[n-1][max_w][max_h])


def get_solution(V, W, H, i, w, h):
  if i == 0:
    if w >= W[0] and h >= H[0]: return [0]
    return []

  if w >= W[i] and h >= H[i] and F[i][w][h] == F[i-1][w-W[i]][h-H[i]] + V[i]:
    return get_solution(V, W, H, i-1, w-W[i], h-H[i]) + [i]
  return get_solution(V, W, H, i-1, w, h)


# 100
# [2]
V = [5, 1, 100]
W = [5, 5, 6]
H = [5, 6, 10]
max_w = 10; max_h = 10

# 35
# [1, 2, 3, 6]
V = [10, 10, 14, 6, 12, 20, 5]
W = [15, 7, 8, 4, 1, 2, 5]
H = [15, 3, 6, 5, 15, 19, 2]
max_w = 24; max_h = 30

F, res = knapsack_3d(V, W, H, max_w, max_h)
print(res)
if res != 0:
  print(get_solution(V, W, H, len(V)-1, max_w, max_h))
