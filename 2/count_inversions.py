from math import inf


def cnt_invs(T, l, r, invs=0):
  n = r - l
  if n <= 1:
    return invs

  if n == 2:
    if T[l] > T[l+1]:
      T[l], T[l+1] = T[l+1], T[l]
      invs += 1
    return invs

  m = (l+r)//2
  invs = cnt_invs(T, l, m, invs) + cnt_invs(T, m, r, invs)

  L = T[l:m]
  R = T[m:r]

  len_L = len(L)
  len_R = len(R)
  i = j = 0
  k = l
  while i < len_L and j < len_R:
    if L[i] < R[j]:
      T[k] = L[i]
      i += 1
    else:
      T[k] = R[j]
      invs += m - l - i
      j += 1
    k += 1  

  while i < len_L:
    T[k] = L[i]
    i += 1
    k += 1

  while j < len_R:
    T[k] = R[j]
    j += 1
    k += 1

  return invs


T = [1, 2, 7, 6, 5, 3, 2]
print(cnt_invs(T, 0, len(T)))
