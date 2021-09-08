def print_path(S, E, F, m, n):
  dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

  def print_rec(i, j):
    nonlocal S, F, dirs, m, n

    if i == S[0] and j == S[1]:
      return

    for k in range(len(dirs)):
      _i = i+dirs[k][0]
      _j = j+dirs[k][1] 

      if 0 <= _i < m and 0 <= _j < n:
        if F[_i][_j] == F[i][j] - 1:
          print_rec(_i, _j)
          print(f'({i}, {j})', end=' ')
          break

  print(S, end=' ')
  print_rec(E[0], E[1])
  print()


def find_longest_path(A, S):
  m = len(A)
  n = len(A[0])

  # F[i][j] - najdluzsza sciezka zaczynajaca sie w S i konczacym sie w (i, j)
  F = [[0 for _ in range(n)] for _ in range(m)]

  dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

  E = (S[0], S[1])
  max_len = 0

  def explore(i, j):
    nonlocal A, S, F, dirs, E, max_len, m, n

    for k in range(len(dirs)):
      _i = i+dirs[k][0]
      _j = j+dirs[k][1]

      if 0 <= _i < m and 0 <= _j < n:
        if A[_i][_j] > A[i][j]:
          F[_i][_j] = max(F[_i][_j], F[i][j]+1)
          
          if F[_i][_j] > max_len:
            max_len = F[_i][_j]
            E = (_i, _j)

          explore(_i, _j)

  explore(S[0], S[1])
  print_path(S, E, F, m, n)

  return max_len


A = [[3, 2, 3, 1, 1, 1, 1],
     [7, 8, 9, 10, 11, 12, 13],
     [8, 3, 12, 11, 7, 1, 7],
     [1, 1, 14, 1, 4, 2, 1],
     [3, 2, 16, 7, 2, 1, 4],
     [1, 4, 19, 4, 5, 2, 1],
     [5, 4, 3, 5, 4, 1, 3],
     [2, 1, 2, 2, 1, 2, 1]]

S = (0, 0)

print(find_longest_path(A, S))
