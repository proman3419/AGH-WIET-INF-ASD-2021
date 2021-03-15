def gcd(a, b):
  while b != 0:
    a, b = b, a%b
  return a


def shift_array(A, k):
  k *= -1
  n = len(A)
  k %= n
  q = gcd(n, k)
  for i in range(q):
    temp = A[i]
    j = i

    while True:
      l = j + k

      if l >= n:
        l -= n

      if l == i:
        break

      A[j] = A[l]
      j = l

    A[j] = temp

  return A


A = [1, 2, 4, 3, 8, 6, 12]
print(shift_array(A, 4))
