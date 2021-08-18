from math import inf


# sprawdzenie czy poczatek i koniec wystepuja
def check_borders(A, S):
  borders_appear = [False, False]
  for e in A:
    if e[0] == S[0]: borders_appear[0] = True
    if e[1] == S[1]: borders_appear[1] = True

  return not (borders_appear[0] and borders_appear[1])


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
def find_min_cost(A, S, C):
  n = len(A)

  if check_borders(A, S):
    return inf

  pts = generate_pts(A)
  m = len(pts)

  # F[i][j] - min koszt sklejenia odcinkow tak, zeby powstal odcinek od i do j
  F = [[inf for _ in range(m)] for _ in range(m)]

  for i in range(n):
    F[map_pt(A[i][0], pts)][map_pt(A[i][1], pts)] = C[i]

  for i in range(m):
    for j in range(i+1, m):
      for k in range(i, j):
        F[i][j] = min(F[i][j], F[i][k] + F[k][j])

  return F[map_pt(S[0], pts)][map_pt(S[1], pts)]


# 60
A = [(0, 3), (3, 7), (0, 1), (1, 2), (2, 7), (4, 3), (-2, 0)]; S = (0, 7)
C = [0, 999, 10, 20, 30, 4, 7]

print(find_min_cost(A, S, C))
