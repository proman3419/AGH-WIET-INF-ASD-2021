def bin_search_string(S, s):
  n = len(S)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if S[c] < s:
      l = c + 1
    elif S[c] > s:
      r = c - 1
    else:
      while c > 0 and S[c-1] == s:
        c -= 1
      break

  if S[c] != s:
    return None
  return c


def find_width_of_string(S, t):
  n, m = len(t), len(S)
  S.sort()
  F = [[-1 for _ in range(n)] for _ in range(n)] # maksymalna szerokosc reprezentacji dla napisu t[i..j], -1 gdy sie nie da

  for l in range(1, n+1):
    for i in range(n-l+1):
      j = i + l - 1

      s_i = bin_search_string(S, t[i:j+1])
      if s_i is not None:
        F[i][j] = max(F[i][j], len(S[s_i]))

      for k in range(i+1, j-1):
        F[i][j] = max(F[i][j], min(F[i][k], F[k+1][j]))

  return F[0][-1]


S = ['ab', 'abab', 'ba', 'bab', 'b']

# 3
t = 'ababbab'

# 2
t = 'ababababab'

print(find_width_of_string(S, t))
