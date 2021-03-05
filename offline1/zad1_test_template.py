from random import randint, seed
from time import time





def mergesort(T):
  print("Tu proszę napisać swoją funckję")
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
