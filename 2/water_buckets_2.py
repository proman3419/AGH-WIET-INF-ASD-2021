def partition(A, l, r):
  x = A[r][2]
  i = l - 1
  for j in range(l, r):
    if A[j][2] < x:
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


def water_buckets(buckets, water):
  n = len(buckets)
  visited = [0]*n
  corners = []
  for i in range(n):
    bucket_width = buckets[i][2] - buckets[i][0]
    # (bucket_id, x, y, bucket_width, pos)
    # pos: 0 -> down, 1 -> up}
    corners.append((i, buckets[i][0], buckets[i][1], bucket_width, 1))
    corners.append((i, buckets[i][2], buckets[i][3], bucket_width, 0))

  corners = quick_sort(corners, 0, 2*n-1) # sortujemy po y

  prev = corners[0]
  width = 0
  for i in range(2*n): # 2n rogow
    bucket_id, x, y, bucket_width, pos = corners[i]
    height_diff = y - prev[2]
    area = abs(width*height_diff)

    if area > water:
      break

    visited[bucket_id] += 1 # oznaczamy bucket jako odwiedzony
    # jezeli na koniec algorytmu bedzie odwiedzony dwukrotnie (raz na dol, raz na gore)
    # to oznacza, ze bucket zostal zapelniony

    if pos == 0: # down
      width += abs(bucket_width) # zwiekszamy szerokosc poniewaz nowy bucket sie zaczyna.
      # buckety na siebie nie nachodza wiec nie policzymy danej szerokosci wielokrotnie
    else:
      width -= abs(bucket_width) # bucket sie konczy

    water -= area
    prev = corners[i]

  cnt = 0
  for i in range(n):
    if visited[i] == 2:
      cnt += 1

  return cnt


water = 8
# pierwszy punkt jest lewym gornym
# 1
buckets = [[1, -1, 4, -2], [1, 2, 2, 0], [3, 5, 4, 1], [1, 5, 2, 4], [-4, 3, -1, 1]]
# 2
buckets = [[4, 6, 6, 4], [9, 5, 11, 3], [11, 7, 15, 6], [6, 3, 8, 2]]

print(water_buckets(buckets, water))
