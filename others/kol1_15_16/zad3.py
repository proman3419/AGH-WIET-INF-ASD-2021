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


def insert_into_ll(l, new, r, prev_new=None):
  if prev_new is not None:
    prev_new.next = new.next

  l.next = new
  new.next = r


def cut_from_ll(l, to_cut, r):
  l.next = r

  return to_cut


# O(2n)
def fixSortedList(L):
  warden = Node() # dodajemy wartownika
  warden.next = L

  prev = warden
  curr = L
  _next = L.next

  # jezeli lista ma tylko dwa elementy
  if _next.next is None:
    if curr.val > _next.val:
      insert_into_ll(head, cut_from_ll(curr, _next, None), curr, None)
    return L

  while _next is not None and curr.val < _next.val: # O(n)
    prev, curr, _next = curr, _next, _next.next

  # jezeli ten losowy element nie zaburza posortowania
  if _next is None:
    return L

  # jezeli zaburza
  # brzydki kod :(
  bad_prev = curr
  bad = _next
  flag = False
  if prev.val is None:
    if _next.val < _next.next.val:
      bad_prev = prev
      bad = curr
      flag = True

  prev = warden
  curr = L
  _next = L.next
  while _next is not None and curr.val <= bad.val: # O(n)
    prev, curr, _next = curr, _next, _next.next

  if flag:
    insert_into_ll(curr, bad, _next, bad_prev)
  else:
    insert_into_ll(prev, bad, curr, bad_prev)

  return warden.next


head = array_to_list([1, 2, 3, 4, -1, 5, 6])
warden = Node()
warden.next = head

display(fixSortedList(head))
