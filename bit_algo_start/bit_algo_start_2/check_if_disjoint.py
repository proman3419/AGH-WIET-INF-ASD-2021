def partition(A, l, r):
  x = A[r]
  i = l - 1
  for j in range(l, r):
    if A[j] < x:
      i += 1
      A[i], A[j] = A[j], A[i]

  i += 1
  A[i], A[r] = A[r], A[i]

  return i


# zakladamy optymalny podzial za pomoca partition (co najmniej 1 elem w kazdym przedziale)
# rekurencja i petla lacznie wykonaja sie O(logn) razy
# na kazdym etapie sortujemy lacznie n elementow, zatem:
# O(nlogn)
def quick_sort(A, l, r):
  while l < r:
    pi = partition(A, l, r)
    
    if pi - l < r - pi:
      quick_sort(A, l, pi-1)
      l = pi + 1
    else:
      quick_sort(A, pi+1, r)
      r = pi - 1

  return A


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


def check_if_disjoint(A, B, m, n):
  # m < n
  # A < B

  # sortowanie i bin search na A
  # mlogm + nlogm

  # sortowanie i bin search na B
  # nlogn + mlogn

  # pierwsze podejscie lepsze poniewaz m < n

  quick_sort(A, 0, m-1)

  for i in range(n):
    if bin_search(A, B[i]) is not None:
      return False

  return True


A = [2, 3, 8, 9]
m = len(A)
B = [1, 4, 7, 15, 6, 12, 10, 43, 17, -10, 99, -2, 0, 9] # ostatni psuje
n = len(B)
print(check_if_disjoint(A, B, m, n))
