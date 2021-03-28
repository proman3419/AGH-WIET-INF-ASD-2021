from math import log, ceil


# O(logn)
def min_heapify(A, n, pi):
  min_i = pi
  l = 2*pi + 1
  r = 2*pi + 2

  if l < n and A[l] < A[min_i]:
    min_i = l
  if r < n and A[r] < A[min_i]:
    min_i = r

  if min_i != pi:
    A[pi], A[min_i] = A[min_i], A[pi]
    min_heapify(A, n, min_i)


# O(nlogn)
def build_min_heap(A, n):
  last_parent = n//2 - 1

  for i in range(last_parent, -1, -1): # O(n//2-1) <= O(n)
    min_heapify(A, n, i) # O(logn)

  return A


def display(A):
  n = len(A)
  steps = ceil(log(n, 2))

  i = 0
  for s in range(steps):
    for j in range(2**s):
      if i >= n:
        break
      print(A[i], end=' ')
      i += 1
    print()
  print()


A = [2, 6, 1, 0, 4, 9, 5]
display(build_min_heap(A, len(A)))
