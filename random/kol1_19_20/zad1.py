def cnt_digits(x, digits):
  _x = x
  while _x > 0:
    digits[_x%10] += 1
    _x //= 10

  j_cnt = w_cnt = 0
  for i in range(10):
    if digits[i] > 1:
      w_cnt += 1
    elif digits[i] == 1:
      j_cnt += 1

  return (j_cnt, w_cnt, x)


def counting_sort(A, n, _id):
  O = [0]*10

  for i in range(n):
    _i = A[i][_id]
    O[_i] += 1

  for i in range(1, 10):
    O[i] += O[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1):
    _i = A[i][_id]
    B[O[_i]-1] = A[i]
    O[_i] -= 1

  for i in range(n):
    A[-i-1] = B[i]


def radix_sort(A, n):
  counting_sort(A, n, 1)
  counting_sort(A, n, 0)


def pretty_sort(T):
  n = len(T)
  digits = [0]*10

  for i in range(n):
    T[i] = cnt_digits(T[i], digits)

    for j in range(10):
      digits[j] = 0

  radix_sort(T, n)

  for i in range(n):
    T[i] = T[i][2]


test = [3322, 1266, 114577, 123, 455, 2344, 67333, 1234455, 12344, 12, 134, 12, 13, 432, 543, 5434, 22]

pretty_sort(test)
print(test)
