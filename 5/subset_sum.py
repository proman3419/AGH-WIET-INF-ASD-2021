def subset_sum(A, target):
  n = len(A)
  if target == 0: return True # nie bierzemy zadnego elementu
  if n == 0: return False # brak elem i target != 0 => niemozliwe do spelnienia

  # dp[i][j] - czy rozpatrujac do i-tego elementu znaleziono sume j
  # i - i-ty element
  # j - suma
  dp = [[False for _ in range(target+1)] for _ in range(n)]

  dp[0][A[0]] = True

  for i in range(1, n):
    for j in range(1, target+1):
      # jezeli obecny element ma wartosc > od obecnej sumy
      # to niemozliwe jest jej osiagniecie (wartosci sa naturalne)
      if A[i] > j:
        dp[i][j] = dp[i-1][j]
      # w przeciwnym razie sprawdzamy czy obecna suma zostala juz osiagnieta
      # albo czy istnieje taka suma do ktorej po dodaniu obecnego elementu
      # otrzymamy obecna sume
      else:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i]]

  return (dp, dp[n-1][target])


def get_solution(dp, A, i, j):
  if i == 0:
    if dp[i][j]: return [i]
    return []

  if dp[i-1][j]:
    return get_solution(dp, A, i-1, j)
  return get_solution(dp, A, i-1, j-A[i]) + [i]


A = [13, 3, 4, 12, 10, 8]
target = 34

res = subset_sum(A, target)
if res[1]:
  print(get_solution(res[0], A, len(A)-1, target))
else:
  print(res[1])
