from random import randint
from math import log, ceil, inf


class Pair:
  def __init__(self, val=inf, cnt=0):
    self.val = val
    self.cnt = cnt


def insertion_sort(A, n, x):
  j = n - 1
  while j >= 0 and A[j].val > x:
    A[j+1].val = A[j].val
    j -= 1
  A[j+1].val = x


def insert(A, n, x):
  flag = (n == 0 or A[-1].val < x)
  A.append(Pair(x, 1))
  if flag:
    return

  insertion_sort(A, n, x)


def bin_search(A, n, x):
  if n == 0:
    return None

  l = c = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if A[c].val < x:
      l = c + 1
    elif A[c].val > x:
      r = c - 1
    else:
      while c > 0 and A[c-1].val == x:
        c -= 1
      break

  if A[c].val != x:
    return None
  return c


def counting_sort(A, n, uniques, _n):
  for i in range(1, _n):
    uniques[i].cnt += uniques[i-1].cnt

  B = [0]*n
  for i in range(n-1, -1, -1):
    j = bin_search(uniques, _n, A[i])
    B[uniques[j].cnt-1] = A[i]
    uniques[j].cnt -= 1

  for i in range(n):
    A[i] = B[i]


def sort_logn_unique_vals(A):
  uniques = []
  _n = 0

  for e in A:
    # log(log(n))
    res = bin_search(uniques, _n, e)
    # log(n) razy
    if res is None:
      insert(uniques, _n, e) # log(n)
      _n += 1
    # n - log(n) razy
    else:
      uniques[res].cnt += 1

  counting_sort(A, n, uniques, _n)


n = 100
_n = ceil(log(n, 2))
A = [randint(0, _n) for i in range(n)]
print(A)
sort_logn_unique_vals(A)
print(A)
