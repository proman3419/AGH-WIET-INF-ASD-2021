# b - ilosc mozliwych wartosci
# O(n + b + n + n) = O(3n + b)
def counting_sort(A, n, exp):
  O = [0]*10

  for i in range(n): # O(n)
    _i = int((A[i]/exp)%10)
    O[_i] += 1

  for i in range(1, 10): # O(b)
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1): # O(n)
    _i = int((A[i]/exp)%10)
    B[O[_i]-1] = A[i]
    O[_i] -= 1

  for i in range(n): # O(n)
    A[i] = B[i]


# k = log(_max)
# k(3n + b) -> O(kn + kb)
def radix_sort(A, _max):
  n = len(A)
  exp = 1 # exp = baza^i, i to obecna cyfra od tylu
  while _max//exp > 0: # O(k)
    counting_sort(A, n, exp) # O(3n + b)
    exp *= 10

  return A


A = [99, 100, 27, 14, 82, 70, 45, 14]
print(radix_sort(A, max(A)))
