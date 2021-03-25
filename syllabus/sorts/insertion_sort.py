# time complexity
# best:  n
# avg:   n^2
# worst: n^2

# space complexity
# worst: 1


def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

  return A


##########################################################################
# test_sort
from random import randint, seed
from time import time
def test_sort():
  seed(1337)
  rr = (1, 10)
  n = 10**2
  sort_func = insertion_sort
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
