class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


def display(head):
  curr = head
  while curr is not None:
    print(curr.val, end=' ')
    curr = curr.next
  print()


##########################################################################


def merge(head1, head2):
  prev1 = head1
  curr1 = head1.next
  curr2 = head2.next

  while curr1 is not None and curr2 is not None:
    if curr1.val < curr2.val:
      prev1, curr1 = curr1, curr1.next
    else:
      temp = curr2.next
      prev1.next = curr2
      curr2.next = curr1
      prev1 = curr2
      curr2 = temp

  if curr2 is not None:
    prev1.next = curr2

  return head1


head1 = Node()
add(head1, 1)
add(head1, 4)
add(head1, 6)
add(head1, 12)

head2 = Node()
add(head2, 3)
add(head2, 5)
add(head2, 7)
add(head2, 9)

display(merge(head1, head2))
