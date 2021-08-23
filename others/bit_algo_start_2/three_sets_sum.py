from random import randint


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


# O(llogl + smlogl)
def solve(S, M, L): # short, medium, long
  L = quick_sort(L, 0, len(L)-1)

  for s_e in S:
    for m_e in M:
      x = bin_search(L, s_e+m_e)
      if x is not None:
        return [s_e, m_e, L[x]]

  return None


def check_three_sets_sum(A, B, C):
  m = len(A)
  n = len(B)
  l = len(C)

  if m >= n and m >= l:
    for i in range(n):
      B[i] *= -1
    res = solve(C, B, A)
    res[1] *= -1 
    return (res, 'CBA')
  elif n >= m and n >= l:
    for i in range(m):
      A[i] *= -1
    res = solve(C, A, B)
    res[1] *= -1
    return (res, 'CAB')

  return (solve(A, B, C), 'ABC')


n = 4
v_rr = (-n**2, n**2)
l_rr = (n, n**3)
A = [randint(v_rr[0], v_rr[1]) for _ in range(randint(l_rr[0], l_rr[1]))]
B = [randint(v_rr[0], v_rr[1]) for _ in range(randint(l_rr[0], l_rr[1]))]
C = [randint(v_rr[0], v_rr[1]) for _ in range(randint(l_rr[0], l_rr[1]))]

print(check_three_sets_sum(A, B, C))
