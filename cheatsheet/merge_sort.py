from math import inf


def merge_sort(T, l, r):
  n = r - l
  if n <= 1:
    return

  if n == 2:
    if T[l] > T[l+1]:
      T[l], T[l+1] = T[l+1], T[l]
    return 

  m = (l+r)//2
  merge_sort(T, l, m)
  merge_sort(T, m, r)

  L = T[l:m] + [inf] # inf -> wartownik
  R = T[m:r] + [inf]

  i = j = 0
  for k in range(l, r):
    if L[i] < R[j]:
      T[k] = L[i]
      i += 1
    else:
      T[k] = R[j]
      j += 1        
