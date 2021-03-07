from random import randint, seed
from math import inf
from time import time





def mergesort(T):
  def find_max(T):
    _max = T[0]
    for i in range(1, len(T)):
      if T[i] > _max:
        _max = T[i]

    return _max

  def sublist(T, l, r):
    n = r - l
    _T = [0]*(n+1)
    for i in range(n):
      _T[i] = T[l+i]
    _T[-1] = inf

    return _T

  def ms(T, l, r):
    n = r - l
    if n <= 1:
      return

    # jeżeli mamy do posortowania dwie wartości to problem jest trywialny
    if n == 2:
      if T[l] > T[l+1]:
        T[l], T[l+1] = T[l+1], T[l]
      return 

    m = (l+r)//2
    ms(T, l, m)
    ms(T, m, r)

    # wartości inf na końcach tablic są wartownikami, oznaczają koniec tablicy
    # jeżeli inf jest niedozwolony można go zastąpić find_max(T) + 1
    # najlepiej wywołać tą funkcję przed pierwszym wywołaniem ms i zapisać do zmiennej, żeby w każdym wywołaniu ms nie szukać jej na nowo
    L = T[l:m] + [inf]
    R = T[m:r] + [inf]
    # nie wiem czy slicing jest dozwolony, jeżeli nie to można dwie powyższe linijki zastąpić tymi poniżej
    # poniższa metoda jest wolniejsza
    #L = sublist(T, l, m)
    #R = sublist(T, m, r)

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
start = time()
T = mergesort(T)
stop = time()
print("po sortowaniu    : T =", T)
print("czas             :", stop-start)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")