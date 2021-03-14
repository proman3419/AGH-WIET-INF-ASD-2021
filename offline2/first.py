class Node:
  def __init__(self):
    self.next = None
    self.value = None
  

def list_tail_len(L):
  if L is None:
    return 0

  _len = 0
  while L.next is not None:
    L = L.next
    _len += 1  

  return (L, _len+1)


def add_wardens(L, tail):
  l_warden = Node()
  #l_warden.value = 'L'
  l_warden.next = L

  tail.next = Node()
  tail = tail.next
  #tail.value = 'R'

  return l_warden, tail


def remove_wardens(L, tail):
  L = L.next
  curr = L

  while curr.next != tail:
    curr = curr.next
  curr.next = None

  return L


def partition(l, r):
  pi = l.next
  i = pi
  j = pi.next

  if j == r:
    return

  while j != r:
    if j.value < pi.value:
      i.next = j.next
      j.next = l.next
      l.next = j
      j = i.next
    else:
      i, j = i.next, j.next

  if l.next != pi:
    partition(l, pi)
  if pi.next != r:
    partition(pi, r)


def qsort( L ):
  tail, _len = list_tail_len(L)
  if _len < 2:
    return L

  L, tail = add_wardens(L, tail)
  partition(L, tail)
  L = remove_wardens(L, tail)

  return L


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")


def list2tab(A):
  if A is None:
    return []

  res = []
  while A is not None:
    res.append(A.value)
    A = A.next

  return res  


##########################################################################
# random test sort
from random import randint, seed
from time import time
def test_sort():
  rr = (-10**2, 10**2)
  n = 10**5
  m = 3
  sort_func = qsort
  print_res = False

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = list2tab(sort_func(tab2list(t)))
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
