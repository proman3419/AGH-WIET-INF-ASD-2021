# algorytm
# wybieramy jako x mediane A, wyliczamy sume odleglosci wedlug wzoru


# dowod
# jezeli x bedzie nalezal do przedzialu (A[n//2-1], A[n//2+1]) to suma odleglosci
# elementow poza n//2-tym bedzie stala.
# dlatego, ze zmiana wartosci x na x +/- i, gdzie A[n//2-1] < x + i < A[n//2+1],
# skutkuje tym, ze dla wszystkich elementow < n//2: sum +/-= i oraz dla > n//2: sum -/+= i => nawzajem sie redukuja

# wracajac do elementu n//2-ego, abs(A[n//2] - x) osiaga min dla x = A[n//2]

# jezeli x bedzie nalezal do przedzialu spoza (A[n//2-1], A[n//2+1]) to 
# suma jeszcze bardziej wzrosnie poniewaz trzeba bedzie doliczyc dystans na
# 'wracanie sie'


def dists_sum(A):
  n = len(A)

  if n == 0: return 0
  if n == 1: return A[0]

  _sum = 0
  x = n//2
  for i in range(n):
    _sum += abs(A[i]-x)

  return (x, _sum)


A = [1, 10, 20, 30, 100]
A.sort()
print(A)
print(dists_sum(A))
