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


def find_bucket(A, n, _min, _max, i):
  _i = int((A[i]-_min)/(_max-_min)*n)
  if _i == n: _i -= 1
  
  return _i


def bucket_sort(A, _min, _max):
  n = len(A)
  B = [0]*n

  for i in range(n):
    B[i] = Node()

  for i in range(n):
    sort_add(B[find_bucket(A, n, _min, _max, i)], A[i])

  i = 0
  for j in range(n):
    B[j] = B[j].next # pomin wartownika
    while B[j] is not None:
      A[i] = B[j].val
      B[j] = B[j].next
      i += 1

  return A


A = [0, 100, 20, 80, 30, 60, 40, 50, 50]
print(bucket_sort(A, min(A), max(A)))
