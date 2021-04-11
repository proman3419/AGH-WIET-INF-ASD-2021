def subset_sum(A, target):
  n = len(A)
  if target == 0: return True # nie bierzemy zadnego elementu
  if n == 0: return False # brak elem i target != 0 => niemozliwe do spelnienia

  # F[i][j] - czy rozpatrujac do i-tego elementu znaleziono sume j
  # i - i-ty element
  # j - suma
  F = [[False for _ in range(target+1)] for _ in range(n)]

  F[0][A[0]] = True

  for i in range(1, n):
    for j in range(1, target+1):
      # jezeli obecny element ma wartosc > od obecnej sumy
      # to niemozliwe jest jej osiagniecie (wartosci sa naturalne)
      if A[i] > j:
        F[i][j] = F[i-1][j]
      # w przeciwnym razie sprawdzamy czy obecna suma zostala juz osiagnieta
      # albo czy istnieje taka suma do ktorej po dodaniu obecnego elementu
      # otrzymamy obecna sume
      else:
        F[i][j] = F[i-1][j] or F[i-1][j-A[i]]

  return (F, F[n-1][target])


def get_solution(F, A, i, j):
  if i == 0:
    if F[i][j]: return [i]
    return []

  if F[i-1][j]:
    return get_solution(F, A, i-1, j)
  return get_solution(F, A, i-1, j-A[i]) + [i]


A = [13, 3, 4, 12, 10, 8]
target = 34

res = subset_sum(A, target)
if res[1]:
  print(get_solution(res[0], A, len(A)-1, target))
else:
  print(res[1])
