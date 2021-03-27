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


head = None # bez wartownika
head = array_to_list([1, 7, 2, -3, 10, 4, 15, 2])


##########################################################################
# min max ll
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


print(min_max_ll(head))
