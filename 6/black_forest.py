def black_forest(c):
  n = len(c)
  if n == 1: return c[0]

  # F[i] - max zysk do i-tego drzewa wlacznie
  F = [0]*n

  F[0] = c[0]
  F[1] = max(c[0], c[1])

  for i in range(2, n):
    F[i] = max(F[i-1], F[i-2] + c[i])

  return F[-1]


# 1100
# c = [100, 1000, 1, 100]

# 21
c = [7, 2, 1, 11, 4, 3]

print(black_forest(c))
