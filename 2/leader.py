def leader(A):
  n = len(A)
  cnt = 1
  candidate = A[0]
  for i in range(1, n):
    if cnt == 0:
      cnt = 1
      candidate = A[i]
    elif A[i] == candidate:
      cnt += 1
    else:
      cnt -= 1

  cnt = 0
  for i in range(n):
    if A[i] == candidate:
      cnt += 1

  return cnt >= n/2


A = [1, 3, 4, 3, 2, 1, 1] # None
B = [1, 2, 2, 3, 3, 3, 3, 2, 3] # 3

print(leader(A))
print(leader(B))
