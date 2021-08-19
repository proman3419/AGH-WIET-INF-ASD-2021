from math import inf


# algorytm
# sortujemy klocki kazdego dziecka a nastepnie odbieramy taki, ktory
# najbardziej zminimalizuje roznice wysokosci miedzy nasza wieza a najwyzsza innego dziecka


def find_max_h_i(heights):
  max_h_i = 0
  for i in range(1, len(heights)):
    if heights[i] > heights[max_h_i]:
      max_h_i = i

  return max_h_i


def find_min_h_diff_i(k, w, heights, max_h_i):
  min_h_diff_i = 0
  min_h_diff = inf
  for i in range(len(heights)):
    last_i = w[i][1]
    curr_h_diff = heights[max_h_i] - heights[k] - w[i][0][last_i]
    if i == max_h_i:
      curr_h_diff -= w[i][0][last_i]

    if curr_h_diff < min_h_diff:
      min_h_diff_i = i
      min_h_diff = curr_h_diff

  return min_h_diff_i


def print_result(k, w, heights):
  for i in range(len(w)):
    print(f'i: {i}, sum: {heights[i]}, klocki:', end=' ')
    for j in range(w[i][1]+1):
      print(w[i][0][j], end=' ')
    print()


def steal_bricks(k, w):
  m = len(w)
  heights = [0]*m

  for i in range(m):
    heights[i] = sum(w[i])
    w[i].sort()
    w[i] = [w[i], len(w[i])-1]

  bricks_taken = 0

  while True:
    max_h_i = find_max_h_i(heights)

    if max_h_i == k:
      print_result(k, w, heights)
      return bricks_taken

    min_h_diff_i = find_min_h_diff_i(k, w, heights, max_h_i)

    last_i = w[min_h_diff_i][1]
    heights[min_h_diff_i] -= w[min_h_diff_i][0][last_i]
    w[min_h_diff_i][1] -= 1

    heights[k] += w[min_h_diff_i][0][last_i]
    w[k][0].append(w[min_h_diff_i][0][last_i])
    w[k][1] += 1

    bricks_taken += 1


# i: 0, sum: 13, klocki: 1 2 3 7 
# i: 1, sum: 23, klocki: 1 10 12 
# i: 2, sum: 13, klocki: 2 2 9 
# i: 3, sum: 16, klocki: 2 4 10 
# 2
k = 1
w = [[1, 7, 3, 2],
     [1],
     [2, 2, 9, 12],
     [2, 4, 10, 10]]

# i: 0, sum: 7, klocki: 2 5 
# i: 1, sum: 6, klocki: 6 
# i: 2, sum: 4, klocki: 4 
# 1
k = 0
w = [[2],
     [6],
     [5, 4]]

# i: 0, sum: 9, klocki: 1 8 
# i: 1, sum: 0, klocki: 
# i: 2, sum: 7, klocki: 3 4 
# 1
k = 0
w = [[1], [8], [4, 3]]

# i: 0, sum: 10, klocki: 1 9 
# i: 1, sum: 0, klocki: 
# i: 2, sum: 9, klocki: 4 5 
# 1
k = 0
w = [[1], [9], [4, 5]]

print(steal_bricks(k, w))
