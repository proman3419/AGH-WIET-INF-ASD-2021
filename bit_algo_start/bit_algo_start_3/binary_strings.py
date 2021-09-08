def cnt_binary_strings(n):
  # F[i] - ilosc binarnych stringow o dlugosci i+1 bez jedynek obok siebie
  F = [0]*n
  F[0] = 2
  F[1] = 3

  for i in range(2, n):
    # F[i-1] - zawsze mozemy dodac 0
    # F[i-2] - wtedy mozemy rowniez dodac 1
    F[i] = F[i-1] + F[i-2]

  return F[-1]


n = 4
print(cnt_binary_strings(n))
