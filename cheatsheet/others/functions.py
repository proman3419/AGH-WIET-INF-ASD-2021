# is_prime
def is_prime(n):
  if n < 2: return False
  if n == 2 or n == 3 or n == 5: return True
  if n%2 == 0 or n%3 == 0 or n%5 == 0: return False

  i = 7
  while i*i <= n:
    if n % i == 0:
      return False
    i += 2
    
  return True


# number_len
from math import log10
def number_len(n):
  return int(log10(n)) + 1


# points distance
def distance(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)


# gcd
def gcd(a, b):
  while b != 0:
    a, b = b, a%b

  return a

# lcm
def lcm(a, b):
  _gcd = gcd(a, b)

  return a//_gcd*b//_gcd


# sum_digits
def sum_digits(n):
  _sum = 0
  while n > 0:
    _sum += n%10
    n //= 10

  return _sum


# cnt_prime_factors
def cnt_prime_factors(n):
  cnt = 0
  i = 2
  while n > 1:
    if n % i == 0:
      cnt += 1
      while n % i == 0:
        n //= i
    i += 1

  return cnt


# sieve
def sieve(n):
  n += 1 # zeby w rangeu nie dodawac
  A = [True]*n
  A[0] = A[1] = False

  i = 2
  while i*i < n:
    if A[i]:
      for j in range(i*i, n, i):
        A[j] = False
    i += 1

  return A


# factorize
def factorize(n):
  factors = []
  i = 2
  while n > 1:
    if n % i == 0:
      factors.append(i)
      while n % i == 0:
        n //= i
    i += 1

  return factors


# revert_list
def revert_list(T):
  N = len(T)
  i = 0
  while i < N//2:
    T[i], T[N-1-i] = T[N-1-i], T[i]
    i += 1
        
  return T


# revert num
def revert_num(n):
  _n = 0
  while n > 0:
    _n = _n*10 + n%10
    n //= 10

  return _n

# is_palindrome
def is_palindrome(n):
  return n == revert_num(n)


# randint array 1D
from random import randint
N = int(input())
rr = (1, 10)
T = [randint(rr[0], rr[1]) for _ in range(N)]


# randint array 2D
from random import randint
N = int(input())
rr = (1, 10)
T = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]


# staircase nested loop
for l in range(2, n):
  for i in range(n-l):
    print(i, i+l)


# iterate diagonally
for k in range(n):
  for j in range(k+1):
    i = k - j
    print(i, j)
  print()

for k in range(n-2, -1, -1):
  for j in range(k+1):
    i = k - j
    _i = n - j - 1
    _j = n - i - 1
    print(_i, _j)
  print()
