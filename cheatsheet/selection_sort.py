def selection_sort(A):
  n = len(A)
  for i in range(n):
    min_i = i
    for j in range(i+1, n):
      if A[j] < A[min_i]:
        min_i = j
    A[i], A[min_i] = A[min_i], A[i]

  return A
