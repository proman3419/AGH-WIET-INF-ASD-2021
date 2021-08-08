# zakladam numerowanie kolorow od 0


# O(n+k)
def find_min_range_colors(A, k):
  n = len(A)
  occurances = [0]*k

  for i in range(n):
    occurances[A[i]] += 1

  i = 0
  j = len(A) - 1
  while i < j:
    changed = False
    while i < j and occurances[A[i]] - 1 > 0:
      occurances[A[i]] -= 1
      i += 1
      changed = True

    while i < j and occurances[A[j]] - 1 > 0:
      occurances[A[j]] -= 1
      j -= 1
      changed = True

    if not changed:
      break

  return (i, j)


# (0, 7)
A = [1, 2, 3, 4, 5, 6, 7, 0]; k = 8

# (3, 6)
A = [0, 3, 3, 2, 3, 1, 0]; k = 4

# (5, 10)
A = [4, 4, 3, 3, 3, 4, 2, 1, 3, 0, 1, 3]; k = 5

print(find_min_range_colors(A, k))
