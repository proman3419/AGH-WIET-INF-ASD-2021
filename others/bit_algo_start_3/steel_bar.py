def best_sell(profits):
  n = len(profits)
  # F[i] - max zysk do i
  F = [0]*n
  F[0] = profits[0]

  for i in range(1, n):
    F[i] = profits[i]
    for j in range(i):
      F[i] = max(F[i], F[i-j] + profits[j])

  print(F)
  return F[-1]


# profits[i] - zysk ze sprzedazy kawalka o dlugosci i
# profits[0] = 0, zeby problem mial sens
profits = [0, 13, 27, 35, 42, 51, 57]

print(best_sell(profits))
