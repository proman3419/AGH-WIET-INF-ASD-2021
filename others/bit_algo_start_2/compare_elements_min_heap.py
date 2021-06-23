from math import log, floor


# O(logn)
def min_heapify(A, n, pi):
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


# O(nlogn)
def build_min_heap(A, n):
  last_parent = n//2 - 1

  for i in range(last_parent, -1, -1): # O(n//2-1) <= O(n)
    min_heapify(A, n, i) # O(logn)

  return A


def display(A):
  n = len(A)
  steps = floor(log(n, 2)) + 1

  i = 0
  for s in range(steps):
    for j in range(2**s):
      if i >= n:
        break
      print(A[i], end=' ')
      i += 1
    print()
  print()


# A[k] >= x ?
def compare_elements(A, k, x):
  n = len(A)
  smaller_cnt = 0
  res = True
  def investigate_subtree(i):
    nonlocal A, k, x, n, smaller_cnt, res

    if A[i] < x:
      smaller_cnt += 1
      if smaller_cnt >= k:
        res = False

    if not res:
      return 

    l = 2*i + 1
    if l < n:
      investigate_subtree(l)

    r = 2*i + 2
    if r < n:
      investigate_subtree(r)

  if k > n:
    return None

  investigate_subtree(0)

  return res


A = [7, 12, 17, 10, 6, 15, 14, 10]
A = build_min_heap(A, len(A))

# True
print(compare_elements(A, 5, 11))
