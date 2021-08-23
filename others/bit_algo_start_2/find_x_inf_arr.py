def bin_search(A, x, n):
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


# n - ilosc znaczacych elementow w tablicy
# O(n)
def find_x_inf_arr(A, x):
  l = -1
  r = 1
  while A[r] is not None:
    r *= 2

  # w najgorszym przypadku r w ostatniej iteracji powyzszej petli bylo rowne n-1.
  # po zakonczeniu petli bedzie rowne 2*(n-1) czyli powrot do n w ponizszej petli
  # wykona w n operacjach

  op_cnt = 0
  while A[r-1] is None: # O(n)
    r -= 1
    op_cnt += 1

  return (bin_search(A, x, r), op_cnt)


def generate_inf_arr(A):
  _A = [None]*INF

  for i in range(len(A)):
    _A[i] = A[i]

  return _A


INF = 10**9

A = generate_inf_arr(sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(find_x_inf_arr(A, 10))
print(find_x_inf_arr(A, 0))
print(find_x_inf_arr(A, INF-1))
