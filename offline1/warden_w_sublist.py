from random import randint, seed
from math import inf
from time import time




def mergesort(T):
  def sublist(T, i, _len):
    _T = [0]*(_len+1)
    for j in range(_len):
      _T[j] = T[i+j]
    _T[-1] = inf

    return _T

  def ms(T, l, r):
    if r - l <= 1:
      return

    m = (l+r)//2
    ms(T, l, m)
    ms(T, m, r)

    len_L = m - l
    len_R = r - m
    L = sublist(T, l, len_L)
    R = sublist(T, m, len_R)

    i = j = k = 0
    while i < len_L or j < len_R:
      if L[i] < R[j]:
        T[l+k] = L[i]
        i += 1
      else:
        T[l+k] = R[j]
        j += 1        
      k += 1

  ms(T, 0, len(T))

  return T
  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10**6) ]

#print("przed sortowaniem: T =", T) 
start = time()
T = mergesort(T)
print(time()-start)
#print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")