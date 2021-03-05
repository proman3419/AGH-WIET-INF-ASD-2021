from random import randint, seed
from time import time




def mergesort(T):
  def ms(T, l, r):
    if r - l <= 1:
      return

    m = (l+r)//2
    ms(T, l, m)
    ms(T, m, r)

    L = T[l:m]
    R = T[m:r]

    i = j = k = 0
    len_L = m - l
    len_R = r - m
    while i < len_L and j < len_R:
      if L[i] < R[j]:
        T[l+k] = L[i]
        i += 1
      else:
        T[l+k] = R[j]
        j += 1        
      k += 1

    while i < len_L:
      T[l+k] = L[i]
      i += 1
      k += 1

    while j < len_R:
      T[l+k] = R[j]
      j += 1
      k += 1

  ms(T, 0, len(T))

  return T
  
  
  

seed(42)

n = 10
Ts = [[ randint(1,10) for i in range(n) ],
      [],
      [1, 1],
      [1, 3, 2],
      [0],
      [-45, 32, -113, 482]]

for T in Ts:
  print("przed sortowaniem: T =", T) 
  start = time()
  T = mergesort(T)
  stop = time()
  print("po sortowaniu    : T =", T)
  print("czas             :", stop-start)

  for i in range(len(T)-1):
    if T[i] > T[i+1]:
      print("Błąd sortowania!")
      break
  else:
    print("OK")
  print()
    