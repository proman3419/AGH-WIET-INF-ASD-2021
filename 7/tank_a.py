# algorytm
# za kazdym razem jedziemy do najbardziej oddalonej stacji w kierunku t


# dowod
# zal, ze istnieje taka stacja i, ze wybierajac ja zmniejszymy ilosc skokow
# j, k - stacje, ktore sa w sciezce
# 0 < j < i < k

# znajdujemy sie na stacji j, wybieramy stacje i na nastepna zamiast k.
# mamy wiec wiekszy dystans do pokonania o k - i i taka sama ilosc skokow.
# oznacza to, ze wybor takiego i nie jest optymalny.
# nie mozemy wybrac i > k poniewaz nie starczy nam paliwa na dojechanie z j do takiego i


# obliczyc minimalna ilosc tankowan, zeby dojechac do t
def tank_a(L, S, P, n, t):
  pos = -1
  cnt = 0
  curr = (0, 0)
  path = []
  
  while True:
    path.append(curr[0])

    # jezeli mozna dojechac z obecnej stacji do celu
    if t - curr[0] <= L:
      path.append(t)
      return (cnt + 1, path)

    # jezeli rozwazylismy wszystkie stacje i nie moglismy dojechac do celu
    if pos + 1 >= n:
      return (-1, None)
        
    pos += 1
    best = A[pos]
    # nie da sie dojechac do nastepnej stacji
    if best[0] - curr[0] > L:
      return (-1, None)

    i = pos + 1
    while i < n and A[i][0] <= curr[0] + L:
      pos = i
      i += 1

    # jedziemy do nastepnej stacji
    curr = A[pos]
    cnt += 1


# zakladam, ze stacje sa w posortowanej kolejnosci
S = [2, 7, 12, 15, 20] # odleglosci stacji od punktu 0
P = [4, 3, 10, 1, 4] # koszty paliw na poszczegolnych stacjach
n = len(S) # ilosc stacji
L = 10 # pojemnosc baku
t = 23 # pole, do ktorego chcemy dojechac
A = list(zip(S, P)) # A[i][0] = S[i], A[i][1] = P[i]

print(tank_a(L, S, P, n, t))
