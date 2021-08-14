from math import inf


def frog_greedy(A):
  n = len(A)
  pos = 0
  e = A[0]
  jmp_cnt = 0

  while pos + e < n - 1:
    if e <= 0:
      return inf

    max_e_i = pos + 1
    for i in range(pos+1, min(pos+e+1, n)):
      if A[i] >= A[max_e_i]:
        max_e_i = i

    e = e - (max_e_i - pos) + A[max_e_i]
    pos = max_e_i
    jmp_cnt += 1

  if pos < n - 1:
    return jmp_cnt + 1
  return jmp_cnt


# 3
A = [1, 2, 3, 4, 5]

# 3
A = [1, 2, 2, 2, 2, 2]

# 2
A = [2, 2, 1, 0, 0]

# 3
A = [2, 2, 1, 0, 0, 0]

# inf
A = [2, 2, 1, 0, 0, 0, 0]

# 2
A = [4, 5, 2, 5, 1, 2, 1, 0]

print(frog_greedy(A))
