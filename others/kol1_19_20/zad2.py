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
def section(T, p, q):
  n = len(T)
  p_val = randomized_select(T, 0, n-1, p) # O(n) (oczekiwana zlozonosc)
  q_val = randomized_select(T, 0, n-1, q) # O(n) (oczekiwana zlozonosc)

  res = [0]*(q-p+1)
  j = 0
  for i in range(n): # O(n)
    if p_val <= T[i] <= q_val:
      res[j] = T[i]
      j += 1

  return res


test = [1, 7, 3, 24, 11, 8, 2, 15]
print(section(test, 2, 6))
