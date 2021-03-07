# time complexity
# best:  n*log(n)
# avg:   n*log(n)
# worst: n*log(n)

# space complexity
# worst: n


from math import inf
def merge_sort(T, l, r):
  n = r - l
  if n <= 1:
    return

  if n == 2:
    if T[l] > T[l+1]:
      T[l], T[l+1] = T[l+1], T[l]
    return 

  m = (l+r)//2
  merge_sort(T, l, m)
  merge_sort(T, m, r)

  L = T[l:m] + [inf] # inf -> warden
  R = T[m:r] + [inf]

  i = j = 0
  for k in range(l, r):
    if L[i] < R[j]:
      T[k] = L[i]
      i += 1
    else:
      T[k] = R[j]
      j += 1        


# test_sort
from random import randint, seed
from time import time
def test_sort():
  seed(1337)
  rr = (1, 10)
  n = 10**2
  sort_func = merge_sort
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
    sort_func(t, 0, len(t))
    stop = time()
    if print_res: print('output:  ', t)

    res = 'INCORRECT'
    if t == expected_res:
      res = 'CORRECT'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

test_sort()
