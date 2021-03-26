class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


def insert(head, val):
  curr = head
  if curr.next == None:
    curr.next = Node(val)
  else:
    temp = curr.next
    curr.next = Node(val)
    curr.next.next = temp


def display(head):
  curr = head
  while curr is not None:
    print(curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


def reverse(head):
  # pomin wartownika
  curr = head.next

  if curr is None:
    return head

  prev = None
  next = curr.next

  while next is not None:
    curr.next = prev
    prev, curr, next = curr, next, next.next

  curr.next = prev

  return Node(next=curr)


head = Node()
add(head, 1)
add(head, 2)
add(head, 3)
add(head, 4)
add(head, 5)
add(head, 6)

display(reverse(head))
