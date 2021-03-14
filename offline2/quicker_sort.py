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
  l_pi = l.next # lewy pivot
  r_pi = l_pi   # prawy pivot
  i = l_pi      # prev
  j = l_pi.next # curr

  if j == r:
    return

  while j != r:
    if j.value < l_pi.value:   # j < l_pi
      i.next = j.next
      j.next = l.next
      l.next = j
      j = i.next
    elif j.value > l_pi.value: # j > l_pi
      i, j = i.next, j.next
    else:                      # j == l_pi
      # jeżeli rozważany element jest równy lewemu pivotowi to wystarczy przesunąć prawy pivot, i, j
      # bez tego przypadku j.next wskazywałby na samego siebie dzięki linijce oznaczonej <-
      if l_pi.next == j:
        r_pi = j
        i, j = j, j.next
        continue
      i.next = j.next
      j.next = l_pi.next # <-
      l_pi.next = j
      j = i.next

  if l.next != l_pi:
    partition(l, l_pi)
  if r_pi.next != r:
    partition(r_pi, r)


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
