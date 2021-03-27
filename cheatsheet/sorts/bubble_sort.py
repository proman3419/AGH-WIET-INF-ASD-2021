def bubble_sort(A):
  n = len(A)
  for i in range(n):
    swp = False
    for j in range(i+1, n):
      if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]
        swp = True

    if not swp:
      break

  return A


print(bubble_sort([15, -2, 1, 0, 6, 3]))
