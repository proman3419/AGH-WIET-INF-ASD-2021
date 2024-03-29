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


head = array_to_list([])
