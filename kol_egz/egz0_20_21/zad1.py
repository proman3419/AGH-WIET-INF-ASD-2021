from zad1testy import runtests
from collections import deque


# O(nt)
def tanagram_2(x, y, t):
  n = len(x)
  used = [0]*n

  for i in range(n):
    found = False
    for j in range(i-t, i+t+1):
      if 0 <= j < n:
        if x[i] == y[j] and used[j] == 0:
          found = True
          used[j] = 1
          break

    if not found:
      return False

  return True


# O(n)
def tanagram(x, y, t):
  n = len(x)
  positions = [deque() for _ in range(26)]

  for i in range(n):
    positions[ord(y[i])-97].append(i)

  for i in range(n):
    closest = positions[ord(x[i])-97].popleft()
    if abs(closest-i) > t:
      return False

  return True


runtests( tanagram )
