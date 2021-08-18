# algorytm
# sprawdzamy ceny na wszystkich stacjach, do ktorych mozemy dojechac (na pelnym baku).
# po znalezieniu najtanszej, poronujemy cene z ta na obecnej.
# jezeli obecna jest tansza to tankujemy do pelna po czym, w obu
# przypadkach, jedziemy do nastepnej najtanszej


# dowod
# zal, ze istnieje stacja i taka, ze jezeli wezmiemy ja do sciezki to 
# koszt calkowity zmaleje.
# j, k - stacje, ktore znajduja sie w sciezce
# 0 < j < i < k

# koszt zmniejszylby sie wtw
# 1) P[i] < P[k], lub
# 2) tankujac w i w nastepnym kroku bedziemy mogli dojechac dalej niz k + L

# 1) falsz poniewaz z zal algo P[k] = min(P[(j, k>]) => P[k] < P[i]
# 2) falsz poniewaz bedziemy mogli dojechac najdalej do i + L gdzie i < k => i + L < k + L

# z 1) i 2) nie istnieje takie i, ze koszt calkowity sciezki bylby mniejszy


# obliczyc minimalny koszt tankowan, zeby dojechac do t, na kazdej stacji mozna tankowac tylko do pelna
def tank_b2(L, A, n, t):
  l = L # obecny stan paliwa
  pos = -1
  cost = 0
  curr = (0, 0)
  path = []

  while True:
    path.append(curr[0])

    if t - curr[0] <= l:
      #print(f'mozna dojechac bez dotankowania')
      path.append(t)
      return (cost, path)
    # jezeli mozna dotankowujac
    elif t - curr[0] <= L:
      #print(f'mozna dojechac dotankowujac, dodatkowy koszt: {curr[1]*(L-l)}')
      path.append(t)
      return (cost + curr[1]*(L-l), path)

    # jezeli rozwazylismy wszystkie stacje i nie moglismy dojechac do celu
    if pos + 1 >= n:
      return (-1, None)
        
    pos += 1
    best = A[pos]
    # nie da sie dojechac do nastepnej stacji
    if best[0] - curr[0] > L:
      return (-1, None)

    # szukamy nastepnej stacji z minimalnym kosztem paliwa
    i = pos + 1
    while i < n and A[i][0] <= curr[0] + L:
      if A[i][1] < best[1]:
        best = A[i]
        pos = i
      i += 1

    # jezeli na obecnej stacji jest tansze paliwo niz nastepnej najtanszej to tankujemy
    if curr[1] < best[1]:
      #print(f'dotankowano: {L - l}, dodatkowy koszt: {(L - l) * curr[1]}')
      cost += (L - l) * curr[1]
      l = L

    # jezeli nie mamy wystarczajaco paliwa, zeby dojechac do nastepnej stacji to tankujemy
    if l < best[0] - curr[0]:
      #print(f'dotankowano: {L - l}, dodatkowy koszt: {(L - l) * curr[1]}')
      cost += (L - l) * curr[1]
      l = L

    # jedziemy do nastepnej stacji
    l -= best[0] - curr[0]
    curr = best


# zakladam, ze stacje sa w posortowanej kolejnosci

# (29, [0, 7, 15, 23]
S = [2, 7, 12, 15, 20] # odleglosci stacji od punktu 0
P = [4, 3, 10, 1, 4] # koszty paliw na poszczegolnych stacjach
L = 10 # pojemnosc baku
t = 23 # pole, do ktorego chcemy dojechac

# (18, [0, 3, 6, 9])
S = [2, 3, 6]
P = [4, 3, 3]
L = 3
t = 9

# (2, [0, 2, 20])
S = [2, 4, 8, 9, 15, 18]
P = [1, 1, 1, 1, 1, 2]
L = 19
t = 20

# (-1, None)
S = [2, 4, 8, 9, 15, 18]
P = [1, 1, 1, 1, 1, 2]
L = 4
t = 20

n = len(S) # ilosc stacji
A = list(zip(S, P)) # A[i][0] = S[i], A[i][1] = P[i]
print(tank_b2(L, A, n, t))

# opis algorytmu i dowod to kopiuj wklej z b1, moze kiedys napisze dla b2
