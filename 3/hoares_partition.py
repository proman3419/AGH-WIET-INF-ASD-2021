def hoares_partition(A, l, r):
  x = A[r] # pivot
  i = l - 1
  j = r + 1

  while True:
    i += 1
    while A[i] < x:
      i += 1

    j -= 1
    while A[i] > x:
      j -= 1

    if i >= j:
      return j

    A[i], A[j] = A[j], A[i]


def quick_sort(A, l, r):
  if l < r:
    pi = hoares_partition(A, l, r) # partition index
    quick_sort(A, l, pi)
    quick_sort(A, pi+1, r)


##########################################################################
# random test sort
from random import randint, seed
from time import time
def test_sort():
  rr = (1, 10)
  n = 10**1
  m = 10
  sort_func = quick_sort
  print_res = True

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
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

    if res == 'INCORRECT':
      break

test_sort()
