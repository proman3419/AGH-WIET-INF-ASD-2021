def max_heapify(A, n, pi):
  max_i = pi
  l = 2*pi + 1
  r = 2*pi + 2

  if l < n and A[l] > A[max_i]:
    max_i = l
  if r < n and A[r] > A[max_i]:
    max_i = r

  if max_i != pi:
    A[pi], A[max_i] = A[max_i], A[pi]
    max_heapify(A, n, max_i)


def build_max_heap(A, n):
  last_parent = n//2 - 1

  for i in range(last_parent, -1, -1):
    max_heapify(A, n, i)


def heap_sort(A):
  n = len(A)
  build_max_heap(A, n)
  
  for i in range(n-1, 0, -1):
    A[0], A[i] = A[i], A[0]
    n -= 1
    max_heapify(A, n, 0)

  return A


print(heap_sort([11, -7, 8, 0, 9, 2, 1]))
