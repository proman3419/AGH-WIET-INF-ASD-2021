# time complexity
# best:  n + k
# avg:   n + k
# worst: n^2

# space complexity
# worst: n

# the algorithm assumes that values to be sorted lay in the [0, 1) range and their distribution is uniform


class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def sort_add(head, val):
  curr = head.next # skip the warden
  if curr is None:
    head.next = Node(val)
  else:
    prev = head
    while curr is not None and curr.val < val:
      prev, curr = curr, curr.next

    new = Node(val)
    prev.next = new
    new.next = curr


def bucket_sort(A):
  n = len(A)
  B = [0]*n

  for i in range(n):
    B[i] = Node()

  for i in range(n):
    sort_add(B[int(n*A[i])], A[i]) # int() works as math.floor

  i = 0
  for j in range(n):
    B[j] = B[j].next # skip the warden
    while B[j] is not None:
      A[i] = B[j].val
      B[j] = B[j].next
      i += 1


##########################################################################
# test_sort
from random import random, seed
from time import time
def test_sort():
  seed(1337)
  n = 10**1
  sort_func = bucket_sort
  print_res = True

  tests = []
  tests.append([0.01, 0.1, 0.32, 0.167, 0.9, 0.42])
  tests.append([0.0])
  tests.append([random() for _ in range(n)])

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
