from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    



def qsort( L ):
  print("Tu proszę napisać swoją funckję")
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


# random test sort
from random import randint, seed
from time import time
def test_sort():
  rr = (-10**3, 10**3)
  n = 10**3
  m = 100
  sort_func = qsort
  print_res = True

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
