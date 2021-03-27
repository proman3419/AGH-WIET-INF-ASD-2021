def bin_search(A, x):
  n = len(A)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if A[c] < x:
      l = c + 1
    elif A[c] > x:
      r = c - 1
    else:
      while c > 0 and A[c-1] == x:
        c -= 1
      break

  if A[c] != x:
    return None
  return c


A = [1, 2, 7, 14, 23, 25]
print(bin_search(A, 10))
print(bin_search(A, 25))
