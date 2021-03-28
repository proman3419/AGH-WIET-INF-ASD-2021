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


# O(n + n^2 + n) = O(2n + n^2) <= O(n^2) - najgorszy przypadek
# O(3n) <= O(n) - rozklad jednostajny
def bucket_sort_ll(head, _min, _max):
  # jezeli lista jest pusta lub jednoelementowa to jest posortowana
  if head is None or head.next is None:
    return head

  n = get_ll_len(head)
  B = [0]*n

  for i in range(n): # O(n)
    B[i] = Node()

  # O(n^2) - najgorszy przypadek
  # O(n) - rozklad jednostajny
  curr = head
  for i in range(n): # O(n)
    _next = curr.next
    curr.next = None
    sort_add(B[find_bucket(curr.val, n, _min, _max)], curr) # O(len(b)) <= O(n), b - obecny bucket
    curr = _next

  head = curr = B[0]
  for i in range(1, n): # O(n)
    if curr is None:
      continue

    while curr.next is not None:
      curr = curr.next

    B[i] = B[i].next # pomin wartownika
    curr.next = B[i]

  return head.next


head = None # bez wartownika
A = [7, 2, -2, 4, -4, 10, 14]
head = array_to_list(A)
display(bucket_sort_ll(head, min(A), max(A)))
