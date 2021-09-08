from zad3testy import runtests


class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def merge(head1, head2):
  l_w = Node() # lewy wartownik
  l_w.next = head1

  prev1 = l_w
  curr1 = head1
  curr2 = head2
  while curr1 is not None and curr2 is not None:
    if curr1.val < curr2.val:
      prev1, curr1 = curr1, curr1.next
    else:
      temp = curr2.next  # zeby nie stracic referencji
      prev1.next = curr2 # wstaw curr2
      curr2.next = curr1
      prev1 = curr2      # przygotuj prev1 i curr2 na nastepna iteracje
      curr2 = temp

  if curr2 is not None:
    prev1.next = curr2   # przylacz reszte

  return l_w.next


def tasks(T):
  n = len(T)

  while n > 1:
    m = 0
    for i in range(0, n-1, 2):
      T[m] = merge(T[i], T[i+1])
      m += 1

    if n%2 == 1:
      T[m] = T[n-1]
      m += 1
    n = m

  return T[0]


runtests( tasks )
