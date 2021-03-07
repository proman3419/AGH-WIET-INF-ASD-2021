# time complexity
# best:  n + k
# avg:   n + k
# worst: n + k

# space complexity
# worst: k, (n + k if implemented like counting_sort2)
# it can be lowered to k by creating the B array outside of the function
# ^ Cormen's implementation

# the algorithm assumes that values to be sorted lay in a specific [min, max] range
# if the range is big it may be a good idea to choose a different algorithm


# time complexity: n + m*n
# space complexity: m
def counting_sort1(A, _min, _max):
  if _min*_max < 0:
    m = abs(_min) + abs(_max) + 1
  else:
    m = _max - _min + 1
  n = len(A)
  O = [0]*m # occurances

  for i in range(n):
    O[A[i]-_min] += 1

  i = 0
  for j in range(m):
    while O[j] > 0:
      A[i] = _min + j
      O[j] -= 1
      i += 1

  return A


# time complexity: n + m-1 + n = 2*n + m - 1
# space complexity: n + m
def counting_sort2(A, _min, _max):
  if _min*_max < 0:
    m = abs(_min) + abs(_max) + 1
  else:
    m = _max - _min + 1
  n = len(A)
  O = [0]*m # occurances

  for i in range(n):
    O[A[i]-_min] += 1

  for i in range(1, m):
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1):
    B[O[A[i]-_min]-1] = A[i]
    O[A[i]-_min] -= 1

  return B


# test_sort
from random import randint, seed
from time import time
def test_sort():
  #seed(1337)
  rr = (-10000, 10000)
  n = 10**2
  sort_func = counting_sort1
  print_res = True

  tests = []
  #tests.append([])
  tests.append([0])
  tests.append([1, -1, 0])
  tests.append([2, -3, 4, -5])
  tests.append([1, 4, 3, 2, 5, 1, 2, 7, 6])
  tests.append([randint(rr[0], rr[1]) for _ in range(n)])

  for t in tests:
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = sort_func(t, min(t), max(t))
    stop = time()
    if print_res: print('output:  ', t)

    res = 'INCORRECT'
    if t == expected_res:
      res = 'CORRECT'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

test_sort()
