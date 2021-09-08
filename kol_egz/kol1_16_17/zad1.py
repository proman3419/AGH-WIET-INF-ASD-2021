class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def array_to_list(A):
  head = Node()
  curr = head
  for e in A:
    curr.next = Node(e)
    curr = curr.next

  return head


def display(head):
  curr = head
  while curr is not None:
    print(curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


def get_ll_len(head):
  _len = 0
  while head is not None:
    _len += 1
    head = head.next

  return _len


def sort_add(head, new):
  curr = head.next # pomin wartownika
  if curr is None:
    head.next = new
  else:
    prev = head
    while curr is not None and curr.val < new.val:
      prev, curr = curr, curr.next

    prev.next = new
    new.next = curr


def find_bucket(val, n, _min, _max):
  i = int((val-_min)/(_max-_min)*n)
  if i == n: i -= 1
  
  return i


def bucket_sort_ll(head, _min, _max):
  n = get_ll_len(head)
  B = [0]*n

  for i in range(n):
    B[i] = Node()

  curr = head
  for i in range(n):
    _next = curr.next
    curr.next = None
    sort_add(B[find_bucket(curr.val, n, _min, _max)], curr)
    curr = _next

  head = curr = B[0]
  for i in range(1, n):
    if curr is None:
      continue

    while curr.next is not None:
      curr = curr.next

    B[i] = B[i].next # pomin wartownika
    curr.next = B[i]

  return head.next


def min_max_ll(head):
  if head is None:
    return (None, None)

  _min = _max = head.val
  head = head.next
  while head is not None:
    if head.val < _min:
      _min = head.val
    if head.val > _max:
      _max = head.val
    head = head.next

  return (_min, _max)


# O(2n)
def Sort(list):
  list = list.next # usuwamy wartownika

  # jezeli lista jest pusta lub jednoelementowa to jest posortowana
  if list is None or list.next is None:
    return list

  _min, _max = min_max_ll(list) # O(n)
  list = bucket_sort_ll(list, _min, _max) # O(n)

  return list


head = array_to_list([7, 1, 8, 2, -4, -13])
display(Sort(head))
