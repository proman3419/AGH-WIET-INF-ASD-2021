A = [1, 7, 2, 6, 5, 3, 4, 8, 9, 0]


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


print(min_max(A))
