def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j][1] > key[1]:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

  return A


def find_bucket(val, n, _min, _max):
  i = int((val-_min)/(_max-_min)*n)
  if i == n: i -= 1
  
  return i


def bucket_sort(A, n, _min, _max):
  B = [0]*n

  for i in range(n):
    B[i] = []

  for i in range(n):
    B[find_bucket(A[i][1], n, _min, _max)].append(A[i])

  for i in range(n):
    insertion_sort(B[i])

  i = 0
  for j in range(n):
    for k in range(len(B[j])):
      A[i] = B[j][k]
      i += 1

  return A


def min_max(A):
  _min = _max = A[0][1]
  n = len(A)

  for i in range(1, n-1, 2):
    if A[i][1] < A[i+1][1]:
      curr_min = A[i][1]
      curr_max = A[i+1][1]
    else:
      curr_max = A[i][1]
      curr_min = A[i+1][1]

    if curr_min < _min: _min = curr_min
    if curr_max > _max: _max = curr_max

  if n%2 == 0:
    if A[-1][1] < _min:
      _min = A[-1][1]
    elif A[-1][1] > _max:
      _max = A[-1][1]

  return (_min, _max)


def remove_dists(A, n):
  for i in range(n):
    A[i] = A[i][0]


# O(4n) 
def sort_by_dist(A):
  n = len(A)
  for i in range(n): # O(n)
    A[i] = (A[i], (A[i][0]**2+A[i][1]**2)**1/2)

  _min, _max = min_max(A) # O(n)

  bucket_sort(A, n, _min, _max) # O(n) (rozklad jest jednostajny)

  remove_dists(A, n) # O(n)

  return A


A = [(1, 1), (0, 0), (-1, -1), (4, 4), (-3, -100)]
print(sort_by_dist(A))
