def falling_bricks(A):
  n = len(A)

  F = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(i+1, n):
      if A[i][0] <= A[j][0] and A[i][1] >= A[j][1]:
        continue
      print(i, j, A[i], A[j], A[i][0] <= A[j][0], A[i][1] >= A[j][1])

      F[i][j] += 1

  for r in F:
    print(r)


A = [[0, 4], [1, 6], [2, 6], [3, 5], [3, 7]]

falling_bricks(A)
