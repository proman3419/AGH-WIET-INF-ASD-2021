# wydaje mi sie, ze w poleceniu jest blad i ma byc x < z < y, wtedy doprecyzowanie w nawiasie ma sens


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


# O(nlogn)
def find_max_gap(A):
  n = len(A)
  A = quick_sort(A, 0, n-1)

  max_gap = 0
  for i in range(n-1):
    curr_gap = A[i+1] - A[i]

    if curr_gap > max_gap:
      max_gap = curr_gap

  return max_gap


# 5
A = [7, 2, 8, 1, 13, 4]

print(find_max_gap(A))
