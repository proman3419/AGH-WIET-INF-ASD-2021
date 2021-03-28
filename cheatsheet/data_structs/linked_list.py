class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


# O(n)
def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


# O(1)
def insert(head, val):
  curr = head
  if curr.next == None:
    curr.next = Node(val)
  else:
    temp = curr.next
    curr.next = Node(val)
    curr.next.next = temp


def array_to_list(A):
  head = Node()
  curr = head
  for e in A:
    curr.next = Node(e)
    curr = curr.next

  return head


def list_to_array(head):
  A = []
  curr = head.next

  while curr is not None:
    A.append(curr.val)
    curr = curr.next

  return A


def display(head):
  curr = head
  while curr is not None:
    print(curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


head = array_to_list([])
