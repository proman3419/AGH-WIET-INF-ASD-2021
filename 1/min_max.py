def min_max(t):
  _min = _max = t[0]
  n = len(t)

  for i in range(1, n-1, 2):
    if t[i] < t[i+1]:
      curr_min = t[i]
      curr_max = t[i+1]
    else:
      curr_max = t[i]
      curr_min = t[i+1]

    if curr_min < _min: _min = curr_min
    if curr_max > _max: _max = curr_max

  if n%2 == 0:
    if t[-1] < _min:
      _min = t[-1]
    elif t[-1] > _max:
      _max = t[-1]

  return (_min, _max)


print(min_max([1, 2, 3, -100, 0, 0]))
