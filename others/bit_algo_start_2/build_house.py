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
  if i == pi:
    return A[pi]
  elif i < pi:
    return randomized_select(A, l, pi-1, i)
  else:
    return randomized_select(A, pi+1, r, i)


def distance(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)


def calculate_distances(A, n, x):
  _sum = 0
  for i in range(n):
    _sum += abs(x - A[i])

  return _sum


def build_house(A):
  n = len(A)
  x = randomized_select(A, 0, n-1, n//2)
  dists_sum = calculate_distances(A, n, x)

  if n%2 == 0:
    _x = randomized_select(A, 0, n-1, n//2-1)
    _dists_sum = calculate_distances(A, n, x)
    if _dists_sum < dists_sum:
      x = _x
      dists_sum = _dists_sum

  return (x, dists_sum)


# (100, 101)
A = [0, 100, 101]
print(build_house(A))

# (100, 220)
A = [20, 40, 50, 100, 110, 120]
print(build_house(A))
