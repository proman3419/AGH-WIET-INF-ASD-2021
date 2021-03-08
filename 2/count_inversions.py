from math import inf
def cnt_invs(T, l, r, invs):
  n = r - l
  if n <= 1:
    return invs

  if n == 2:
    if T[l] > T[l+1]:
      T[l], T[l+1] = T[l+1], T[l]
      invs += 1
    return invs

  m = (l+r)//2
  invs += cnt_invs(T, l, m, invs) + cnt_invs(T, m, r, invs)

  L = T[l:m] + [inf] # inf -> warden
  R = T[m:r] + [inf]

  i = j = 0
  for k in range(l, r):
    if L[i] < R[j]:
      T[k] = L[i]
      i += 1
    else:
      T[k] = R[j]
      invs += i
      j += 1    

  return invs


T = [4, 5, 10, 9]
print(cnt_invs(T, 0, len(T), 0))
