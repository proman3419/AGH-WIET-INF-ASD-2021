# algorytm
# sprawdzamy ceny na wszystkich stacjach, do ktorych mozemy dojechac (na pelnym baku).
# po znalezieniu najtanszej, porownujemy cene z ta na obecnej.
# jezeli obecna jest tansza to tankujemy do pelna,
# jezeli nie jest to tankujemy tyle, zeby dojechac do najtanszej.
# nastepnie w obu przypadkach, jedziemy do nastepnej najtanszej


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


# obliczyc minimalny koszt tankowan, zeby dojechac do t, na kazdej stacji mozna tankowac ile sie chce
def tank_b1(L, A, n, t):
  l = L # obecny stan paliwa
  pos = -1
  cost = 0
  curr = (0, 0)
  path = []

  while True:
    path.append(curr[0])

    # jezeli mozna dojechac z obecnej stacji do celu przy obecnym stanie paliwa
    if t - curr[0] <= l:
      #print(f'mozna dojechac bez dotankowania')
      path.append(t)
      return (cost, path)
    # jezeli mozna dotankowujac
    elif t - curr[0] <= L:
      #print(f'mozna dojechac dotankowujac, dodatkowy koszt: {curr[1]*(t-curr[0])}')
      path.append(t)
      return (cost + curr[1]*(t-curr[0]), path)

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

    # jezeli na obecnej stacji jest tansze paliwo niz nastepnej najtanszej to tankujemy tutaj do pelna
    if curr[1] < best[1]:
      #print(f'tankujemy do pelna, dotankowano: {L - l}, dodatkowy koszt: {(L - l) * curr[1]}')
      cost += (L - l) * curr[1]
      l = L

    # jezeli nie mamy wystarczajaco paliwa, zeby dojechac do nastepnej stacji to tankujemy tak,
    # zeby dojechac do najtanszej, ktora jest w zasiegu
    l_after = l - (best[0] - curr[0])
    if l_after < 0:
      #print(f'deficyt: {abs(l_after)}, dodatkowy koszt: {abs(l_after) * curr[1]}')
      cost += abs(l_after) * curr[1]
      l = best[0] - curr[0]

    # jedziemy do nastepnej stacji
    l -= best[0] - curr[0]
    curr = best


# zakladam, ze stacje sa w posortowanej kolejnosci
S = [2, 7, 12, 15, 20] # odleglosci stacji od punktu 0
P = [4, 3, 10, 1, 4] # koszty paliw na poszczegolnych stacjach
n = len(S) # ilosc stacji
L = 10 # pojemnosc baku
t = 23 # pole, do ktorego chcemy dojechac
A = list(zip(S, P)) # A[i][0] = S[i], A[i][1] = P[i]

print(tank_b1(L, A, n, t))
