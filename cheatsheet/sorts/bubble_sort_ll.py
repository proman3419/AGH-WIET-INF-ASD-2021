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


def swap(p, q, r):
  temp = r.next
  p.next = r
  r.next = q
  q.next = temp


# O(n^2)
def bubble_sort_ll(head):
  # jezeli lista jest pusta lub jednoelementowa to jest posortowana
  if head is None or head.next is None:
    return head

  warden = Node()
  warden.next = head

  swp = True
  while swp: # <= O(n)
    p = warden
    q = warden.next
    r = q.next
    swp = False
    while r is not None: # O(n)
      if q.val > r.val:
        swap(p, q, r)
        q, r = r, q
        swp = True
      p, q, r = p.next, q.next, r.next

  return warden.next


head = array_to_list([10, 2, 3, -1, 4, -2, 0, 14])
display(bubble_sort_ll(head))
