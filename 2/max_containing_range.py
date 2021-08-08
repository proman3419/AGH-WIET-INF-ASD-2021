# O(n^2)
def find_max_containing_range(ranges):
  n = len(ranges)
  max_cnt = max_i = 0
  for i in range(n):
    cnt = 0
    for j in range(n):
      if i != j:
        if ranges[i][0] <= ranges[j][0] and ranges[j][1] <= ranges[i][1]:
          cnt += 1

    if cnt > max_cnt:
      max_cnt = cnt
      max_i = i

  return (ranges[max_i], max_cnt)


def partition(A, l, r):
  x = A[r][0]
  i = l - 1
  for j in range(l, r):
    if A[j][0] < x:
      i += 1
      A[i], A[j] = A[j], A[i]

  i += 1
  A[i], A[r] = A[r], A[i]

  return i


# zakladamy optymalny podzial za pomoca partition (co najmniej 1 elem w kazdym przedziale)
# rekurencja i petla lacznie wykonaja sie O(logn) razy
# na kazdym etapie sortujemy lacznie n elementow, zatem:
# O(nlogn)
def quick_sort(A, l, r):
  while l < r:
    pi = partition(A, l, r)
    
    if pi - l < r - pi:
      quick_sort(A, l, pi-1)
      l = pi + 1
    else:
      quick_sort(A, pi+1, r)
      r = pi - 1

  return A


# nie dziala
# na razie dla naturalnych
# docelowo O(nlogn)
def find_max_containing_range_2(ranges):
  n = len(ranges)
  # (point, range_id, type)
  # type: 0 -> start, 1 -> end
  points = []
  for i, r in enumerate(ranges):
    points.append((r[0], i, 0))
    points.append((r[1], i, 1))

  points = quick_sort(points, 0, 2*n-1)

  m = points[-1][0] + 1 # ile punktow jednostkowych
  F = [0]*m # liczba przedzialow, ktore zaczynaja sie na pozycji x lub wczesniej
  G = [0]*m # liczba przedzialow, ktore koncza sie na pozycji x lub wczesniej

  prev = 0
  for p in points:
    point, range_id, _type = p

    for i in range(prev+1, point+1):
      F[i] = F[i-1]
      G[i] = G[i-1]

    if _type == 0:
      F[point] += 1
    else:
      G[point] += 1

    prev = point

  return max(F[x]-G[x] for x in range(m))


# ((5, 10), 2)
ranges = [(5, 6), (0, 4), (8, 10), (1, 6), (5, 10)]

print(find_max_containing_range(ranges))
print(find_max_containing_range_2(ranges))
