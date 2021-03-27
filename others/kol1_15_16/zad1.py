def partition(A, l, r):
  x = A[r][2]
  i = l - 1
  for j in range(l, r):
    if A[j][2] < x:
      i += 1
      A[i], A[j] = A[j], A[i]

  i += 1
  A[i], A[r] = A[r], A[i]

  return i


def quick_sort(A, l, r):
  while l < r:
    pi = partition(A, l, r)
    
    if pi - l < r - pi:
      quick_sort(A, l, pi-1)
      l = pi + 1
    else:
      quick_sort(A, pi+1, r)
      r = pi - 1

  return A


def generate_sums(A, n):
  sums = [None]*n # O(n)
  for i in range(n): # O(n)
    _sum = 0
    for j in range(i*n, (i+1)*n): # O(n)
      _sum += A[j]
    sums[i] = (i*n, (i+1)*n, _sum)

  return sums


# O(n + n^2 + nlogn + n^2) = O(n + nlogn + 2n^2)
def SumSort(A, B, n):
  sums = generate_sums(A, n) # O(n + n^2)
  sums = quick_sort(sums, 0, n-1) # O(nlogn)

  i = 0
  for j in range(n): # O(n)
    for k in range(sums[j][0], sums[j][1]): # O(n)
      B[i] = A[k]
      i += 1

  return B


from random import randint
n = 5
A = [randint(0, 10) for _ in range(n*n)]
B = [0 for _ in range(n*n)]

print(A)
print(SumSort(A, B, n))
