# time complexity
# best:  n*log(n)
# avg:   n*log(n)
# worst: n*log(n)

# space complexity
# worst: 1


def max_heapify(A, n, pi): # pi - parent index
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


##########################################################################
# test_sort
from random import randint, seed
from time import time
def test_sort():
  seed(1337)
  rr = (1, 10)
  n = 10**1
  sort_func = heap_sort
  print_res = True

  tests = []
  tests.append([])
  tests.append([0])
  tests.append([1, -1, 0])
  tests.append([2, -3, 4, -5])
  tests.append([randint(rr[0], rr[1]) for _ in range(n)])

  for t in tests:
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    sort_func(t)
    stop = time()
    if print_res: print('output:  ', t)

    res = 'INCORRECT'
    if t == expected_res:
      res = 'CORRECT'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

test_sort()
