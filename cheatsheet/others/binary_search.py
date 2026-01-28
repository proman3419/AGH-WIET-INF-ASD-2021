def bin_search(A, x):
  l = 0
  r = len(A) - 1
  res = None
  while l <= r:
    c = (l+r)//2
    if A[c] < x:
      l = c + 1
    elif A[c] > x:
      r = c - 1
    else:
      r = c - 1
      res = c
  return res


A = [1, 2, 7, 14, 23, 25]
print(bin_search(A, 10))
print(bin_search(A, 25))
