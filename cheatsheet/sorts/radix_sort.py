def counting_sort(A, n, exp):
  O = [0]*10

  for i in range(n):
    _i = int((A[i]/exp)%10)
    O[_i] += 1

  for i in range(1, 10):
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1):
    _i = int((A[i]/exp)%10)
    B[O[_i]-1] = A[i]
    O[_i] -= 1

  for i in range(n):
    A[i] = B[i]


def radix_sort(A, _max):
  n = len(A)
  exp = 1 # exp = 10^i, i to obecna cyfra
  while _max//exp > 0:
    counting_sort(A, n, exp)
    exp *= 10

  return A


A = [99, 100, 27, 14, 82, 70, 45, 14]
print(radix_sort(A, max(A)))
