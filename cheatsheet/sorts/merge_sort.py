from math import inf


# rekurencja wykona sie O(logn) razy
# na kazdym etapie sortujemy lacznie n elementow, zatem:
# O(nlogn)
def merge_sort(A):
  def ms(A, l, r):
    n = r - l + 1
    if n <= 1:
      return

    if n == 2:
      if A[l] > A[l+1]:
        A[l], A[l+1] = A[l+1], A[l]
      return 

    m = (l+r)//2
    ms(A, l, m) # rekurencja wykona sie O(logm) razy
    ms(A, m, r) # rekurencja wykona sie O(logm) razy

    L = A[l:m] # O(m-l)
    L.append(inf) # inf -> wartownik, zamortyzowany O(1)
    R = A[m:r] # O(r-m)
    R.append(inf) # zamortyzowany O(1)

    i = j = 0
    for k in range(l, r): # O(r-l)
      if L[i] < R[j]:
        A[k] = L[i]
        i += 1
      else:
        A[k] = R[j]
        j += 1        

  ms(A, 0, len(A)-1)

  return A


print(merge_sort([4, -6, 1, 13, 9, 2, 20]))
