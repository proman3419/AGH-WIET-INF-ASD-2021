def get_solution(P):
  def rec(i):
    nonlocal P

    if P[i] == -1:
      return [i]

    return rec(P[i]) + [i-P[i]]

  return rec(len(P)-1)


def best_sell(profits):
  n = len(profits)
  # F[i] - max zysk do i
  F = [0]*n
  P = [-1]*n
  F[0] = profits[0]

  for i in range(1, n):
    F[i] = profits[i]
    for j in range(i):
      new_p = F[i-j] + profits[j]

      if new_p > F[i]:
        F[i] = new_p
        P[i] = i - j

  print(get_solution(P))

  return F[n-1]


# profits[i] - zysk ze sprzedazy kawalka o dlugosci i
# profits[0] = 0, zeby problem mial sens
profits = [0, 5, 15, 23, 33, 39, 45, 51, 60, 71]

# [5, 4]
# 72
print(best_sell(profits))
