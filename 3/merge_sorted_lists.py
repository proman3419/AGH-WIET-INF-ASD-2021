class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def add(head, val):
  if head is None:
    head = Node(val)
  else:
    curr = head
    while curr.next is not None:
      curr = curr.next

    curr.next = Node(val)

  return head


def array_to_list(A):
  n = len(A)
  if n == 0:
    return None

  head = Node(A[0])
  curr = head
  for i in range(1, n):
    curr.next = Node(A[i])
    curr = curr.next

  return head


def display(head):
  if head is None:
    print('Empty')
    return

  curr = head
  while curr is not None:
    print(curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


def merge(head1, head2):
  l_w = Node() # add left warden
  l_w.next = head1

  prev1 = l_w
  curr1 = head1
  curr2 = head2
  while curr1 is not None and curr2 is not None:
    if curr1.val < curr2.val:
      prev1, curr1 = curr1, curr1.next
    else:
      temp = curr2.next  # not to lose the ref
      prev1.next = curr2 # insert curr2
      curr2.next = curr1
      prev1 = curr2      # prepare prev1 and curr2 for the next iteration
      curr2 = temp

  if curr2 is not None:
    prev1.next = curr2   # append the remaining part

  return l_w.next


def merge_sorted_lists(lists):
  n = len(lists)
  m = 1
  while m < n:
    i = 0
      merge(lists[i], lists[i+m])
    m += 1

  return lists[0]


head1 = array_to_list([5, 9])
head2 = array_to_list([2, 11])
#display(merge(head1, head2))

head3 = array_to_list([7, 2, 2, 9, 4, 6, 7, 8, 9, 9, 9, 9, 9])
#head3 = sort_natural_series(head3)
#display(head3)


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
  rr = (-10**3, 10**3)
  n = 10**5
  m = 10
  sort_func = sort_natural_series
  print_res = False

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
