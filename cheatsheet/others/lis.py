# O(n^2)
def lis(A):
  n = len(A)
  # F[i] - dlugosc najdluzszego rosnacego podciagu konczacego sie na A[i]
  F = [1]*n
  P = [-1]*n

  for i in range(1, n):
    for j in range(i):
      if A[j] < A[i] and F[j] + 1 > F[i]:
        F[i] = F[j] + 1
        P[i] = j

  _max_i = n - 1
  for i in range(n-2, -1, -1):
    if F[i] > F[_max_i]:
      _max_i = i

  return (_max_i, F, P)


def get_solution(A, P, i):
  if i == -1:
    return []

  return get_solution(A, P, P[i]) + [i]


# binary search
# O(logn)
def find_i(A, l, r, val):
  while r - l > 1:
    m = l + (r-l)//2
    if A[m] >= val:
      r = m
    else:
      l = m

  return l


# O(nlogn)
def lis2(A):
  n = len(A)
  # przechowujemy tylko konce podciagow
  tails = [-1]*(n+1)
  tails[0] = A[0]
  # dlugosc tablicy koncow, ktora jest wykorzystywana
  m = 1

  for i in range(1, n):
    if A[i] < tails[0]:
      tails[0] = A[i]
    elif A[i] > tails[m-1]:
      tails[m] = A[i]
      m += 1
    else:
      tails[find_i(tails, -1, m-1, A[i])+1] = A[i] # O(logn)

  return m


# [3, 4, 5]
# 3
A = [1, 2, 3, -3, -2, 1]

res = lis(A)
sol = get_solution(A, res[2], res[0])
print(f'{sol}\n{len(sol)}')

# print(lis2(A))
