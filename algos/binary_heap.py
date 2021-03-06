# max-heap
# for every node other than root:
# A[parent(i)] >= A[i]
# used in heap sort
def max_heapify(A, n, i):
  max_i = i
  l = 2*i + 1
  r = 2*i + 2

  if l < n and A[l] > A[max_i]:
    max_i = l
  if r < n and A[r] > A[max_i]:
    max_i = r

  if max_i != i:
    A[i], A[max_i] = A[max_i], A[i]
    max_heapify(A, n, max_i)


def build_max_heap(A, n):
  last_parent = n//2 - 1

  for i in range(last_parent, -1, -1):
    max_heapify(A, n, i)


# min-heap 
# for every node other than root:
# A[parent(i)] <= A[i]
# used in priority queues
def min_heapify(A, n, i):
  min_i = i
  l = 2*i + 1
  r = 2*i + 2

  if l < n and A[l] < A[min_i]:
    min_i = l
  if r < n and A[r] < A[min_i]:
    min_i = r

  if min_i != i:
    A[i], A[min_i] = A[min_i], A[i]
    min_heapify(A, n, min_i)


def build_min_heap(A, n):
  last_parent = n//2 - 1

  for i in range(last_parent, -1, -1):
    min_heapify(A, n, i)
