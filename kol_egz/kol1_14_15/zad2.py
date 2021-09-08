class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def insert(head, node):
  if head is None:
    head = node
  else:
    curr = head
    if curr.next == None:
      curr.next = node
    else:
      temp = curr.next
      curr.next = node
      curr.next.next = temp

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


class TwoLists:
  def __init__(self):
    self.even = Node()
    self.odd = Node()


# O(n)
def split(head):
  two_lists = TwoLists()
  if head is None:
    return two_lists

  curr = head
  while curr is not None: # O(n)
    _next = curr.next
    curr.next = None
    if curr.val%2 == 0:
      insert(two_lists.even, curr) # O(1)
    else:
      insert(two_lists.odd, curr) # O(1)
    curr = _next

  two_lists.even = two_lists.even.next
  two_lists.odd = two_lists.odd.next

  return two_lists


head = array_to_list([1, 7, 2, 4, 7, 8, 15, 0])
two_lists = split(head)
print('even:', end=' ')
display(two_lists.even)
print('odd:', end=' ')
display(two_lists.odd)
