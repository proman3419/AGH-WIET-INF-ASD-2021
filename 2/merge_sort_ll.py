class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def add(head, val):
  curr = head
  while curr.next is not None:
    curr = curr.next

  curr.next = Node(val)


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


def merge(head1, head2):
  prev1 = head1
  curr1 = head1.next
  curr2 = head2.next

  while curr1 is not None and curr2 is not None:
    if curr1.val < curr2.val:
      prev1, curr1 = curr1, curr1.next
    else:
      temp = curr2.next  # not to lose the ref
      prev1.next = curr2 # insert curr2
      curr2.next = curr1
      prev1 = curr2      # prepare prev1 and curr2 for the next iteration
      curr2 = temp

  if curr2 is not None:
    prev1.next = curr2   # append the remaining part

  return head1


def find_series(head):
  series = []
  curr = head.next
  while curr is not None:
    s = curr
    while curr.next is not None and curr.next.val > curr.val:
      curr = curr.next

    series += [s]
    s_tail = curr
    curr = curr.next
    s_tail.next = None

  return series


def sort_natural_series(head):
  series = find_series(head)
  # ???


head1 = array_to_list([1, 3, 5, 7, 10, 20, 34])
head2 = array_to_list([2, 7, 11, 14, 17, 23, 29])
display(merge(head1, head2))

head3 = array_to_list([1, 3, 6, 2, 4, 8, 5, 9, 2, 11])
#sort_natural_series(head3)
for s in find_series(head3):
  display(s)
display(head3)
