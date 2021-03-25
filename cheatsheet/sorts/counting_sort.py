def counting_sort(A, _min, _max):
  m = _max - _min + 1
  n = len(A)
  O = [0]*m

  for i in range(n):
    O[A[i]-_min] += 1

  for i in range(1, m):
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1):
    B[O[A[i]-_min]-1] = A[i]
    O[A[i]-_min] -= 1

  for i in range(n):
    A[i] = B[i]

  return A


A = counting_sort(A, _min, _max)
