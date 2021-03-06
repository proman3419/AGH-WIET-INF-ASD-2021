# max-heap
# for every node other than root:
# A[parent(i)] >= A[i]
# used in heap sort
def max_heapify(A, n, pi): # pi - parent index
  max_i = pi
  l = 2*pi + 1
  r = 2*pi + 2

  if l < n and A[l] > A[max_i]:
    max_i = l
  if r < n and A[r] > A[max_i]:
    max_i = r

  if max_i != pi:
    A[pi], A[max_i] = A[max_i], A[pi]
    max_heapify(A, n, max_i)


def build_max_heap(A, n):
  last_parent = n//2 - 1

  for i in range(last_parent, -1, -1):
    max_heapify(A, n, i)

# min-heap 
# for every node other than root:
# A[parent(i)] <= A[i]
# used in priority queues
def min_heapify(A, n, pi): # pi - parent index
  min_i = pi
  l = 2*pi + 1
  r = 2*pi + 2

  if l < n and A[l] < A[min_i]:
    min_i = l
  if r < n and A[r] < A[min_i]:
    min_i = r

  if min_i != pi:
    A[pi], A[min_i] = A[min_i], A[pi]
    min_heapify(A, n, min_i)


def build_min_heap(A, n):
  last_parent = n//2 - 1

  for i in range(last_parent, -1, -1):
    min_heapify(A, n, i)
