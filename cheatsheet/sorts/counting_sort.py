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


A = [10, -2, 14, 7, 3, 8, 1]
print(counting_sort(A, min(A), max(A)))
