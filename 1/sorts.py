A = [3, 1, 6, 4, 5, 2, 8, 7, 9, 0]


# best n
# worst n^2
# stable
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


#print(bubble_sort(A))


# best n^2
# worst n^2
# stable
def selection_sort(A):
  n = len(A)
  for i in range(n):
    min_i = i
    for j in range(i+1, n):
      if A[j] < A[min_i]:
        min_i = j
    A[i], A[min_i] = A[min_i], A[i]

  return A


#print(selection_sort(A))


# best n
# worst n^2
# stable
def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

  return A


print(insertion_sort(A))
