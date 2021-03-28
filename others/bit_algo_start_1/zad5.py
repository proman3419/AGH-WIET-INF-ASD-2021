# m = _max - _min + 1
# 3n + m -> O(n + m)
def counting_sort(A, _min, _max):
  m = _max - _min + 1
  n = len(A)
  O = [0]*m

  for i in range(n): # O(n)
    O[A[i]-_min] += 1

  for i in range(1, m): # O(m)
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1): # O(n)
    B[O[A[i]-_min]-1] = A[i]
    O[A[i]-_min] -= 1

  for i in range(n): # O(n)
    A[i] = B[i]

  return A


# O(n^2)
def insertion_sort(A):
  n = len(A)
  for i in range(1, n): # O(n)
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key: # <= O(j) <= O(n)
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

  return A


# O(n - k)
def shift_up(A, n, k):
  for i in range(n-k-1, -1, -1): # O(n - k)
    A[i+k] = A[i]


# n + n + k + 10^2 + 10 + n - k + k + 10 - k = 120 + 3n -> O(n)
def sort_with_10_changed(A, k):
  changed = [-1]*10
  n = len(A)

  j = 0
  for i in range(n): # O(n)
    if 0 <= A[i] <= k:
      continue
    changed[j] = A[i]
    A[i] = k # po posortowaniu beda najbardziej po prawej w tablicy
    j += 1

  counting_sort(A, 0, k) # n + k + 1 -> O(n + k)
  insertion_sort(changed) # O(10^2)

  k = 0
  while k < 10 and changed[k] < 0: # O(10)
    k += 1

  shift_up(A, n, k) # O(n - k)

  for i in range(k): # O(k)
    A[i] = changed[i]

  for i in range(k, 10): # O(10 - k)
    A[n-(10-i)] = changed[i]

  return A


A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, -100, 25, 14, -1, -20, 99, 67, 19, 23]
print(sort_with_10_changed(A, 9))
