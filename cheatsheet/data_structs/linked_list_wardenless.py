class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


# O(n)
def add(head, val):
  if head is None:
    head = Node(val)
  else:
    curr = head
    while curr.next is not None:
      curr = curr.next

    curr.next = Node(val)

  return head


# O(1)
def insert(head, val):
  if head is None:
    head = Node(val)
  else:
    curr = head
    if curr.next == None:
      curr.next = Node(val)
    else:
      temp = curr.next
      curr.next = Node(val)
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


def list_to_array(head):
  A = []
  curr = head

  if curr is None:
    return A

  while curr is not None:
    A.append(curr.val)
    curr = curr.next

  return A


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
