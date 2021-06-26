def ferry(A, L):
  n = len(A)
  # F[i][l][r] - czy da sie umiescic i pierwszych samochodow na pasach z pozostalym
  # miejscem l na lewym pasie oraz r na prawym pasie
  F = [[[0 for _ in range(L+1)] for _ in range(L+1)] for _ in range(n)]

  if A[0] > L:
    return 0

  F[0][L-A[0]][L] = 1
  F[0][L][L-A[0]] = 1

  max_i = 0

  for i in range(1, n):
    for l in range(L, -1, -1):
      for r in range(L, -1, -1):
        prev_l = l + A[i]
        if prev_l <= L and F[i-1][prev_l][r] == 1:
          F[i][l][r] = 1
          max_i = i

        prev_r = r + A[i]
        if prev_r <= L and F[i-1][l][prev_r] == 1:
          F[i][l][r] = 1
          max_i = i

  return max_i + 1 # +1 bo liczylismy od 0


# 7
A = [10, 4, 7, 6, 5, 4, 2]
L = 20

print(ferry(A, L))
