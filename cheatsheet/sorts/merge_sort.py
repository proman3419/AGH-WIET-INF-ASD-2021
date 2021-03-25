from math import inf


def mergesort(A):
  def ms(A, l, r):
    n = r - l
    if n <= 1:
      return

    if n == 2:
      if A[l] > A[l+1]:
        A[l], A[l+1] = A[l+1], A[l]
      return 

    m = (l+r)//2
    ms(A, l, m)
    ms(A, m, r)

    L = A[l:m] + [inf] # inf -> wartownik
    R = A[m:r] + [inf]

    i = j = 0
    for k in range(l, r):
      if L[i] < R[j]:
        A[k] = L[i]
        i += 1
      else:
        A[k] = R[j]
        j += 1        

  ms(A, 0, len(A))

  return A


A = mergesort(A)
