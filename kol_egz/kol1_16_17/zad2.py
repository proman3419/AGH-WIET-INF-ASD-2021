def randomized_partition(A, l, r):
  x = A[r]
  i = l - 1
  for j in range(l, r):
    if A[j] < x:
      i += 1
      A[i], A[j] = A[j], A[i]

  i += 1
  A[i], A[r] = A[r], A[i]

  return i


def randomized_select(A, l, r, i):
  if l == r:
    return A[l]

  pi = randomized_partition(A, l, r)
  if i == pi:
    return A[pi]
  elif i < pi:
    return randomized_select(A, l, pi-1, i)
  else:
    return randomized_select(A, pi+1, r, i)


# O(3n)
def SumBetween(T, _from, to, n):
  if n == 0:
    return 0

  _from_val = randomized_select(T, 0, n-1, _from) # O(n) (oczekiwana zlozonosc)
  to_val = randomized_select(T, 0, n-1, to) # O(n) (oczekiwana zlozonosc)

  _sum = 0
  for i in range(n): # O(n)
    if _from_val <= T[i] <= to_val:
      _sum += T[i]

  return _sum


T = [1, 7, 2, 3, 6, 5]
print(SumBetween(T, 2, 4, len(T)))
