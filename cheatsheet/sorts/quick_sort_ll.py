class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


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
    if j.val < l_pi.val:    # j < l_pi
      i.next = j.next
      j.next = l.next
      l.next = j
      j = i.next
    elif j.val > l_pi.val:  # j > l_pi
      i, j = i.next, j.next
    else:                   # j == l_pi
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


# zakladamy optymalny podzial za pomoca partition (co najmniej 1 elem w kazdym przedziale)
# rekurencja lacznie wykonaja sie O(logn) razy
# na kazdym etapie sortujemy lacznie n elementow, zatem:
# n + 1 + nlogn + n = 2n + nlogn + 1 -> O(nlogn)
def quick_sort_ll(L):
  # jezeli lista jest pusta lub jednoelementowa to jest posortowana
  if L is None or L.next is None:
    return L

  tail, _len = list_tail_len(L) # O(n)

  L, tail = add_wardens(L, tail) # O(1)
  partition(L, tail) # O(nlogn)
  L = remove_wardens(L, tail) # O(n)

  return L


L = None # bez wartownika
L = array_to_list([7, 12, -2, 8, 9, -7, 15])
display(quick_sort_ll(L))
