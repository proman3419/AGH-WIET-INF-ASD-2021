# O(n^2)
def lis(A):
  n = len(A)
  # F[i] - dlugosc najdluzszego rosnacego podciagu konczacego sie na A[i]
  # kazdy element tworzy sam w sobie podciag o dlugosci 1
  F = [1]*n # O(n)
  # P[i] - indeks, pod ktorym znajduje sie poprzedni element podciagu, jezeli -1 to brak
  P = [-1]*n # O(n)

  # dla kazdego elementu w tablicy sprawdzamy
  for i in range(1, n): # O(n)
    # czy istnieja elementy przed nim takie, ze:
    for j in range(i): # ~O(n)
      # - moze on z nimi stworzyc ciag rosnacy
      # - czy bedzie on dluzszy niz obecny najdluzszy
      if A[j] < A[i] and F[j] + 1 > F[i]:
        F[i] = F[j] + 1
        # nadpisujemy rodzica
        P[i] = j

  _max_i = n - 1
  for i in range(n-2, -1, -1): # O(n)
    if F[i] > F[_max_i]:
      _max_i = i

  return (_max_i, F, P)


def get_solution(A, P, i):
  if i == -1:
    return []

  return get_solution(A, P, P[i]) + [i]


# binary search
# O(logn)
def find_i(A, l, r, val):
  while r - l > 1:
    m = l + (r-l)//2
    if A[m] >= val:
      r = m
    else:
      l = m

  return l


# O(nlogn)
def lis2(A):
  n = len(A)
  # przechowujemy tylko konce podciagow poniewaz na ich podstawie bedziemy
  # podejmowali decyzje
  tails = [-1]*(n+1) # O(n)

  # pierwszy najdluzszy podciag rosnacy, ktory znajduje sie w tablicy
  # to A[0], mozna go zatem wpisac do tablicy koncow
  tails[0] = A[0]
  # m oznacza dlugosc tablicy koncow, ktora jest wykorzystywana
  m = 1

  # dla wszystkich nastepnych elementow w tablicy glownej
  for i in range(1, n): # O(n)
    # jezeli obecny element jest mniejszy od najmniejszego elementu
    # tworzacego podciagi to go nadpisujemy.
    # jest to element, od ktorego zaczyna sie kolejny podciag rosnacy
    if A[i] < tails[0]:
      tails[0] = A[i]

    # jezeli obecny element jest wiekszy od najwiekszego elementu
    # w podciagach to tworzymy nowy podciag poprzez dopisanie
    # obecnego elementu na koniec najdluzszego podciagu jaki utworzylismy
    # do tej pory (oba podciagi nadal znajduja sie w tablicy koncow)
    elif A[i] > tails[m-1]:
      tails[m] = A[i]
      m += 1

    # jezeli obecny element jest pomiedzy min i max elmentem to szukamy
    # podciagu, do ktorego mozna by dopisac obecny element.
    # chcemy dodac go optymalnie tzn, zeby po dodaniu tego elementu
    # utworzony podciag byl najdluzszy mozliwy.
    # szukamy wiec podciagu konczacego sie na jak najwiekszej wartosci, ktora
    # jest mniejsza niz obecny element
    else:
      tails[find_i(tails, -1, m-1, A[i])+1] = A[i] # O(logn)

  return m


A = [1, 2, 3, -3, -2, 1]

res = lis(A)
sol = get_solution(A, res[2], res[0])
print(f'{sol}\n{len(sol)}')

#print(lis2(A))
