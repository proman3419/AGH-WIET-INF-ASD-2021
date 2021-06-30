# O(n^2)
def bubble_sort(A):
  n = len(A)
  for i in range(n): # O(n)
    for j in range(n): # O(n)
      if A[i] < A[j]:
        A[i], A[j] = A[j], A[i]

  return A


print(bubble_sort([5, 1, 2, 3, 4]))
