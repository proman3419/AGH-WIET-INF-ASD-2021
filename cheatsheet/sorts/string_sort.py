def counting_sort(B_i, B_i_len, curr_char):
  O = [0]*26

  for i in range(B_i_len):
    _i = ord(B_i[i][curr_char]) - ord('a')
    O[_i] += 1

  for i in range(1, 26):
    O[i] += O[i-1]

  B = [0]*B_i_len
  for i in range(B_i_len-1, -1, -1):
    _i = ord(B_i[i][curr_char]) - ord('a')
    B[O[_i]-1] = B_i[i]
    O[_i] -= 1

  for i in range(B_i_len):
    B_i[i] = B[i]


def radix_sort(B_i, curr_len): # B_i - ity bucket
  B_i_len = len(B_i)
  for curr_char in range(curr_len):
    counting_sort(B_i, B_i_len, curr_char)


def min_max(A, n):
  _min = _max = len(A[0])

  for i in range(1, n-1, 2):
    if len(A[i]) < len(A[i+1]):
      curr_min = len(A[i])
      curr_max = len(A[i+1])
    else:
      curr_max = len(A[i])
      curr_min = len(A[i+1])

    if curr_min < _min: _min = curr_min
    if curr_max > _max: _max = curr_max

  if n%2 == 0:
    if len(A[-1]) < _min:
      _min = len(A[-1])
    elif len(A[-1]) > _max:
      _max = len(A[-1])

  return (_min, _max)


# k - max dlugosc stringu
# n + n + k(n+k) = 2n + k(n+k) -> O(kn)
def string_sort(A):
  n = len(A)
  if n <= 1:
    return A

  _min_len, _max_len = min_max(A, n) # O(n)

  # tworzymy kubelki na stringi na podstawie ich dlugosci
  k = _max_len - _min_len + 1
  B = [[] for _ in range(k)] # B - buckets
  for i in range(n): # O(n)
    B[len(A[i])-_min_len].append(A[i]) # zamortyzowany O(1)

  # sortujemy od stringow o najdluzszej dlugosci
  radix_sort(B[-1], _max_len)
  curr_len = _max_len - 1
  for i in range(k-2, -1, -1): # O(k)
    B[i].extend(B[i+1]) # O(len(B[i+1])) <= O(n)
    radix_sort(B[i], curr_len) # O(curr_len) <= O(k)
    curr_len -= 1

  return B[0]


A = ['aaaaaa', 'aab', 'ac', 'a', 'b', 'ab', 'zzzzzz', 'z', 'adsf']
print(sorted(A))
print(string_sort(A))
