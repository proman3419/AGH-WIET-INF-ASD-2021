from random import shuffle


def counting_sort(A, exp, n):
  n = len(A)
  O = [0]*n

  for i in range(n):
    _i = int((A[i]/exp)%n)
    O[_i] += 1

  for i in range(1, n):
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1):
    _i = int((A[i]/exp)%n)
    B[O[_i]-1] = A[i]
    O[_i] -= 1

  for i in range(n):
    A[i] = B[i]


def radix_sort(A, _max, n):
  exp = 1 # exp = n^i, i to obecna cyfra
  while _max//exp > 0:
    counting_sort(A, exp, n)
    exp *= n


n = 10
A = [i for i in range(n**2)]
shuffle(A)
print(A)
radix_sort(A, n**2-1, n)
print(A)
