from math import log, ceil


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

  return A


def add_to_max_heap(A, val):
  A.append(val)
  n = len(A)
  i = n - 1
  pi = (i-1)//2

  while pi >= 0:
    max_heapify(A, n, pi)
    pi = (pi-1)//2


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


A = build_max_heap(A, n)
