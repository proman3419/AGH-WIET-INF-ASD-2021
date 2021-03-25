# time complexity
# best:  n*log(n)
# avg:   n*log(n)
# worst: n^2

# space complexity
# worst: log(n)


def partition(A, l, r):
  x = A[r] # pivot
  i = l - 1
  for j in range(l, r):
    if A[j] < x:
      i += 1
      A[i], A[j] = A[j], A[i]

  i += 1
  A[i], A[r] = A[r], A[i]

  return i


def quick_sort(A, l, r):
  if l < r:
    pi = partition(A, l, r) # partition index
    quick_sort(A, l, pi-1)
    quick_sort(A, pi+1, r)


# removed tail recursion
def quick_sort2(A, l, r):
  while l < r:
    pi = partition(A, l, r) # partition index
    quick_sort(A, l, pi-1)
    l = pi + 1


# improved quick_sort2
# space complexity O(log(n))
# recursive call is made only on the smaller part, the greater is handled
# iteratively
# in the worst scenario in each call both parts are the same length
# so we have log(n) recursive calls
def quick_sort3(A, l, r):
  while l < r:
    pi = partition(A, l, r) # partition index
    
    if pi - l < r - pi:
      quick_sort3(A, l, pi-1)
      l = pi + 1
    else:
      quick_sort3(A, pi+1, r)
      r = pi - 1


##########################################################################
# test_sort
from random import randint, seed
from time import time
def test_sort():
  seed(1337)
  rr = (1, 10)
  n = 10**3
  sort_func = quick_sort3
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
    sort_func(t, 0, len(t)-1)
    stop = time()
    if print_res: print('output:  ', t)

    res = 'INCORRECT'
    if t == expected_res:
      res = 'CORRECT'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

test_sort()
