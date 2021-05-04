def print_solution(F, c, profit):
  n = len(c)
  res = []

  i = n - 1
  while i > 0 and F[i] == F[i-1]:
    i -= 1
  res.append(c[i])

  while i >= 0:
    j = i
    # szukamy kandydata
    while j >= 0 and F[j] + c[i] != F[i]:
      j -= 1

    if j < 0:
      break

    # pomijamy tych o tej samej wartosci w F co kandydat,
    # szukany bedzie pierwszym z ta wartoscia
    while j > 0 and F[j] == F[j-1]:
      j -= 1

    res.append(c[j])
    i = j

  for i in range(len(res)-1, -1, -1):
    print(res[i], end=' ')
  print(f'\n{profit}')


def black_forest(c):
  n = len(c)
  if n == 1: return c[0]

  # F[i] - max zysk do i-tego drzewa wlacznie
  F = [0]*n

  F[0] = c[0]
  F[1] = max(c[0], c[1])

  for i in range(2, n):
    F[i] = max(F[i-1], F[i-2] + c[i])

  return (F[-1], F)


# 1100
# c = [100, 1000, 1, 100]

# 21
# c = [7, 2, 1, 11, 4, 3, 1]

# 161
c = [56, 2, 14, 3, 1, 91]

profit, F = black_forest(c)
print_solution(F, c, profit)
