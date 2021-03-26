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
  l_warden.next = L

  tail.next = Node()
  tail = tail.next

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
      # jezeli rozwazany element jest rowny lewemu pivotowi to wystarczy przesunac prawy pivot, i, j
      # bez tego przypadku j.next wskazywalby na samego siebie dzieki linijce oznaczonej <-
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


def quick_sort(L):
  # jezeli lista jest pusta lub jednoelementowa to jest posortowana
  if L is None or L.next is None:
    return L

  tail, _len = list_tail_len(L)

  L, tail = add_wardens(L, tail)
  partition(L, tail)
  L = remove_wardens(L, tail)

  return L


quick_sort(L)
