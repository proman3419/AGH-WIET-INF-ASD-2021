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


def find_bucket(val, n, _min, _max):
  i = int((val-_min)/(_max-_min)*n)
  if i == n: i -= 1
  
  return i


# 3n + n^2 -> O(n^2) - najgorszy przypadek
# 4n -> O(n) - rozklad jednostajny
def bucket_sort(A, _min, _max):
  n = len(A)
  B = [0]*n

  for i in range(n): # O(n)
    B[i] = []

  for i in range(n): # O(n)
    B[find_bucket(A[i], n, _min, _max)].append(A[i])

  for i in range(n): # O(n)
    insertion_sort(B[i])

  i = 0
  # O(n^2) - najgorszy przypadek
  # O(n) - rozklad jednostajny
  for j in range(n): # O(n)
    for k in range(len(B[j])): # O(len(B[j])) <= O(n)
      A[i] = B[j][k]
      i += 1

  return A


A = [0, 100, 20, 80, 30, 60, 40, 50, 50]
print(bucket_sort(A, min(A), max(A)))
