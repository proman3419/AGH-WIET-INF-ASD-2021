def min_max(A):
  _min = _max = A[0]
  n = len(A)

  for i in range(1, n-1, 2):
    if A[i] < A[i+1]:
      curr_min = A[i]
      curr_max = A[i+1]
    else:
      curr_max = A[i]
      curr_min = A[i+1]

    if curr_min < _min: _min = curr_min
    if curr_max > _max: _max = curr_max

  if n%2 == 0:
    if A[-1] < _min:
      _min = A[-1]
    elif A[-1] > _max:
      _max = A[-1]

  return (_min, _max)


def randomized_partition(A, l, r):
  x = A[r]
  i = l - 1
  for j in range(l, r):
    if A[j] < x:
      i += 1
      A[i], A[j] = A[j], A[i]

  i += 1
  A[i], A[r] = A[r], A[i]

  return i


def randomized_select(A, l, r, i):
  if l == r:
    return A[l]

  pi = randomized_partition(A, l, r)
  k = pi - l + 1
  if i == k:
    return A[pi]
  elif i < k:
    return randomized_select(A, l, pi-1, i)
  else:
    return randomized_select(A, pi+1, r, i-k)


def median(A):
  n = len(A)
  if n%2 == 1:
    return randomized_select(A, 0, n-1, n//2)
  else:
    return (randomized_select(A, 0, n-1, n//2), randomized_select(A, 0, n-1, n//2+1))
