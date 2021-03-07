# time complexity
# best:  n*k
# avg:   n*k
# worst: n*k

# space complexity
# worst: n + k


def counting_sort(A, exp):
  n = len(A)
  O = [0]*10 # occurances

  for i in range(n):
    _i = int((A[i]/exp)%10)
    O[_i] += 1

  for i in range(1, 10):
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1):
    _i = int((A[i]/exp)%10)
    B[O[_i]-1] = A[i]
    O[_i] -= 1

  for i in range(n):
    A[i] = B[i]


def radix_sort(A, _max):
  exp = 1 # exp is 10^i where i is the current digit number
  while _max/exp > 0:
    counting_sort(A, exp) # digits {1, 2 ... 9}, 0 is added in the counting_sort function
    exp *= 10


# test_sort
from random import randint, seed
from time import time
def test_sort():
  #seed(1337)
  rr = (0, 10**3)
  n = 10**2
  sort_func = radix_sort
  print_res = True

  tests = []
  #tests.append([])
  tests.append([0])
  tests.append([1, 4, 3, 2, 5, 1, 2, 7, 6])
  tests.append([randint(rr[0], rr[1]) for _ in range(n)])

  for t in tests:
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    sort_func(t, max(t))
    stop = time()
    if print_res: print('output:  ', t)

    res = 'INCORRECT'
    if t == expected_res:
      res = 'CORRECT'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

test_sort()
