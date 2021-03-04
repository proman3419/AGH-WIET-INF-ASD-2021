def bin_search(A, x):
  n = len(A)
  l = -1
  r = n
  while l < r:
    c = (l+r)//2
    if A[c] < x:
      l = c + 1
    elif A[c] > x:
      r = c - 1
    else:
      while c > 0 and A[c-1] == x:
        c -= 1
      break

  return c


print(bin_search([1, 3, 3, 3, 7], 7))
