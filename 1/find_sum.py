def find_sum(A, x):
  n = len(A)

  for i in range(n):
    j = n - 1
    while j > i:
      _sum = A[i] + A[j]
      if _sum < x:
        break
      elif _sum == x:
        return (i, j)
      j -= 1

  return (-1, -1)


print(find_sum([1, 2, 3, 4, 5, 113, 4068], 4071))
