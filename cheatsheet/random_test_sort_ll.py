##########################################################################
# random test sort linked list
def list_to_array(A):
  if A is None:
    return []

  res = []
  while A is not None:
    res.append(A.val)
    A = A.next

  return res


from random import randint, seed
from time import time
def test_sort():
  rr = (1, 10)
  n = 10**2
  m = 100
  sort_func = change_it
  print_res = True

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = list_to_array(sort_func(array_to_list(t)))
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
