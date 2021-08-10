def ferry(A, L):
  n = len(A)
  # F[i][l][r] - czy da sie umiescic i pierwszych samochodow na pasach z pozostalym
  # miejscem l na lewym pasie oraz r na prawym pasie
  F = [[['_' for _ in range(L+1)] for _ in range(L+1)] for _ in range(n)]

  if A[0] > L:
    return 0

  F[0][L-A[0]][L] = 'L'
  F[0][L][L-A[0]] = 'R'

  max_i = max_l = max_r = 0

  for i in range(1, n):
    for l in range(L, -1, -1):
      for r in range(L, -1, -1):
        prev_l = l + A[i]
        if prev_l <= L and F[i-1][prev_l][r] != '_':
          F[i][l][r] = 'L'
          max_i = i; max_l = l; max_r = r

        prev_r = r + A[i]
        if prev_r <= L and F[i-1][l][prev_r] != '_':
          F[i][l][r] = 'R'
          max_i = i; max_l = l; max_r = r

  return (max_i, max_l, max_r, F)


def get_solution(F, A, i, l, r):
  if i < 0: return []

  if F[i][l][r] == 'L':
    return get_solution(F, A, i-1, l+A[i], r) + ['L']
  elif F[i][l][r] == 'R':
    return get_solution(F, A, i-1, l, r+A[i]) + ['R']


# 7
A = [10, 4, 7, 6, 5, 4, 2]; L = 20

# 4
A = [4, 3, 12, 1, 9]; L = 13

max_i, max_l, max_r, F = ferry(A, L)

print(max_i+1) # +1 bo liczylismy od 0
print(get_solution(F, A, max_i, max_l, max_r))
