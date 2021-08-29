from math import inf


def pick_plates(A, P):
  N = len(A)
  k = len(A[0])

  S = [[A[t][0] if i == 1 else 0 for i in range(k+1)] for t in range(N)]

  for t in range(N):
    for i in range(2, k+1):
      S[t][i] = S[t][i-1] + A[t][i-1]

  m = min(P, N*k) + 1

  # F[i][j] - max piekno dla i pierwszych stosow wlacznie przy j wzietych talerzach
  F = [[0 if i == 0 else -inf for i in range(m)] for t in range(N)]

  for i in range(1, k+1):
    F[0][i] = S[0][i]

  for t in range(1, N):
    for i in range(1, m):
      for x in range(i+1):
        _sum = S[t][i-x] if i - x <= k else max(S[t])
        F[t][i] = max(F[t][i], F[t-1][x] + _sum)

  return max(F[-1])


# 0 - wierzch stosu
A = [[1, 4, 1, 8, 5],
     [3, 1, 2, 1, 3],
     [2, 2, 3, 6, 7],
     [1, 1, 5, 4, 2]]

# 25
print(pick_plates(A, 7))

A = [[3, 100, 1, 1], 
     [4, 1, 10, 3], 
     [1, 3, 2, 2000]]

# 2113
print(pick_plates(A, 7))
