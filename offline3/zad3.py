from random import randint, shuffle, seed


def insertion_sort(A, l, r):
  for i in range(l, r+1):
    key = A[i]
    j = i - 1
    while j >= l and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key


def magic_fives(A, l, r, k):
  n = r - l + 1
  # jeżeli problem jest wystarczająco mały kończymy rekurencyjne rozwiązywanie go
  if n <= 5:
    insertion_sort(A, l, r)
    return l + k

  # i - obecny indeks, m_i - obecny indeks mediany
  i = m_i = l
  while i + 4 <= r:
    # sortujemy podciągi o długości 5
    insertion_sort(A, i, i+4)
    # umieszczamy ich mediany na początku badanego przedziału tablicy A
    A[m_i], A[i+2] = A[i+2], A[m_i]
    m_i += 1
    i += 5

  # ostatni podciąg może być krótszy, rozważamy oddzielnie
  # żeby indeks nie wyszedł poza tablicę oraz, żeby odpowiednio dobrać medianę w podciągu
  if n%5 != 0:
    insertion_sort(A, i, r)
    m = (r-i+1)//2
    A[m_i], A[m] = A[m_i], A[m]

  # n//10 = n/5//2
  # median jest ceil(n/5), mediana median będzie środkowym elementem, dlatego //2
  # dla parzystej ilości median raz będzie wybierana górna, raz dolna
  return magic_fives(A, l, m_i, n//10)


def partition(A, l, r, m_i):
  # zamieniamy medianę z ostatnim elementem
  A[r], A[m_i] = A[m_i], A[r]
  # reszta funkcji to standardowy partition
  i = l - 1
  for j in range(l, r):
    if A[j] < A[r]:
      i += 1
      A[i], A[j] = A[j], A[i]

  i += 1
  A[i], A[r] = A[r], A[i]

  return i


def linearselect( A, k ):
  def ls(A, l, r, k):
    # jeżeli problem jest wystarczająco mały kończymy rekurencyjne rozwiązywanie go
    if r - l <= 5:
      insertion_sort(A, l, r)
      return A[k]

    m_i = magic_fives(A, l, r, k)
    pi = partition(A, l, r, m_i)

    if pi == k: # jest k elem <= A[pi] => A[k] jest rozwiązaniem
      return A[k]
    elif k < pi: # jest pi elem <= A[pi], k < pi => rozwiązanie znajduje się w przedziale [l, pi-1]
      return ls(A, l, pi-1, k)
    else: # jest pi elem <= A[pi], k > pi => rozwiązanie znajduje się w przedziale [pi+1, r]
      return ls(A, pi+1, r, k)

  return ls(A, 0, len(A)-1, k)


seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
    
print("OK")
