# O(len(u) + len(v) + len(w))
def possible(u, v, w):
  chars = [0]*26
  ord_a = ord('a')

  for i in range(len(u)): # O(len(u))
    chars[ord(u[i])-ord_a] += 1

  for i in range(len(v)): # O(len(v))
    chars[ord(v[i])-ord_a] += 1

  for i in range(len(w)): # O(len(w))
    chars[ord(w[i])-ord_a] -= 1

  for i in range(26):
    if chars[i] < 0:
      return False

  return True


print(possible('assdf', 'cx', 'asdfx'))  
