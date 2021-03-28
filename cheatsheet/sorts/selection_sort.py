# O(n^2)
def selection_sort(A):
  n = len(A)
  for i in range(n): # O(n)
    min_i = i
    for j in range(i+1, n): # O(n-i-1) <= O(n)
      if A[j] < A[min_i]:
        min_i = j
    A[i], A[min_i] = A[min_i], A[i]

  return A


print(selection_sort([-2, 9, 3, 17, 4, -16, 5]))
