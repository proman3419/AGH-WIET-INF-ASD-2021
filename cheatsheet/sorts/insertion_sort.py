# O(n^2)
def insertion_sort(A):
  n = len(A)
  for i in range(1, n): # O(n)
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key: # <= O(j) <= O(n)
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

  return A


print(insertion_sort([4, 12, 8, 3, -2, -5, 6]))
