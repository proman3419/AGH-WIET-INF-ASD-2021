class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def sort_add(head, val):
  curr = head.next # pomin wartownika
  if curr is None:
    head.next = Node(val)
  else:
    prev = head
    while curr is not None and curr.val < val:
      prev, curr = curr, curr.next

    new = Node(val)
    prev.next = new
    new.next = curr


def bucket_sort(A):
  n = len(A)
  B = [0]*n

  for i in range(n):
    B[i] = Node()

  for i in range(n):
    sort_add(B[int(n*A[i])], A[i])

  i = 0
  for j in range(n):
    B[j] = B[j].next # pomin wartownika
    while B[j] is not None:
      A[i] = B[j].val
      B[j] = B[j].next
      i += 1
