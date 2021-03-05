from random import randint, seed
from math import inf





def mergesort(T):
  def ms(T, l, r):
    if r - l <= 1:
      return

    m = (l+r)//2
    ms(T, l, m)
    ms(T, m, r)

    # wartości inf na końcach tablic są wartownikami, oznaczają koniec tablicy
    L = T[l:m] + [inf]
    R = T[m:r] + [inf]

    i = j = 0
    for k in range(l, r):
      # dzięki wartownikom nie trzeba sprawdzać czy wychodzi się poza tablice
      # gdy dojdzie się do końca jednej tablicy poniższy if zapewni, że brane będą elementy z drugiej tablicy
      if L[i] < R[j]:
        T[k] = L[i]
        i += 1
      else:
        T[k] = R[j]
        j += 1        

  ms(T, 0, len(T))

  return T
  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(n) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")