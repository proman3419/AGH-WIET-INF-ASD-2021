from random import randint, seed





def mergesort(T):
  def ms(T, l, r):
    if r - l <= 1:
      return

    m = (l+r)//2
    ms(T, l, m)
    ms(T, m, r)

    # wartości inf na końcach tablic są wartownikami, oznaczają koniec tablicy
    # dzięki nim nie trzeba sprawdzać czy wychodzi się poza tablice
    L = T[l:m]
    L += [inf]
    R = T[m:r]
    R += [inf]

    i = j = 0
    for k in range(l, r):
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
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")