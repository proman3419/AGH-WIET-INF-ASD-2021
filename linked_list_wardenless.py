class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def add(head, val):
  if head is None:
    head = Node(val)
  else:
    curr = head
    while curr.next is not None:
      curr = curr.next

    curr.next = Node(val)

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


head = None