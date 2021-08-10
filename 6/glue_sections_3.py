from math import inf


def generate_pts(A):
  pts_tmp = []
  for e in A:
    pts_tmp.append(e[0])
    pts_tmp.append(e[1])

  pts_tmp.sort()

  pts = [pts_tmp[0]]
  for e in pts_tmp:
    if e != pts[-1]:
      pts.append(e)

  return pts


def map_pt(p, pts):
  n = len(pts)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if pts[c] < p:
      l = c + 1
    elif pts[c] > p:
      r = c - 1
    else:
      while c > 0 and pts[c-1] == p:
        c -= 1
      break

  if pts[c] != p:
    return None
  return c


# O(n^3)
def find_longest(A, K):
  n = len(A)

  pts = generate_pts(A)
  m = len(pts)

  # F[i][j] - min liczba odcinkow, ktore trzeba skleic zeby powstal odcinek od i do j
  F = [[inf for _ in range(m)] for _ in range(m)]

  for e in A:
    F[map_pt(e[0], pts)][map_pt(e[1], pts)] = 0

  for i in range(m):
    for j in range(i+1, m):
      for k in range(i, j):
        F[i][j] = min(F[i][j], F[i][k] + F[k][j] + 1)

  # sprawdzamy te, ktore mozna otrzymac
  a = b = max_len = -inf
  for i in range(m):
    for j in range(m):
      # i spelniaja warunek na K
      if F[i][j] <= K:
        curr_len = pts[j] - pts[i]
        if curr_len > max_len:
          a = pts[i]
          b = pts[j]
          max_len = curr_len

  return (a, b, max_len)


# (-2, 7, 9)
A = [(0, 3), (3, 7), (4, 3), (-2, 0)]; K = 3

# (-2, 14, 16)
A = [(0, 3), (3, 9), (0, 5), (5, 8), (8, 14), (4, 3), (-2, 0)]; K = 4

print(find_longest(A, K))
