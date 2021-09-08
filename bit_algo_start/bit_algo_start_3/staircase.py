def staircase(A):
  n = len(A)
  # F[i] - na ile sposobow mozna dostac sie z 0 na i-ty stopien
  F = [0]*n
  F[0] = 1

  for i in range(1, n):
    for j in range(i):
      # jezeli mozemy z j na i oraz z 0 na j
      if A[j] >= i - j and F[j] != 0:
        F[i] += 1

  return F[-1]


A = [1, 3, 2, 1, 0]
print(staircase(A))
