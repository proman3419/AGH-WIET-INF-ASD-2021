# constants
vowels = 'aeiouy'


# is_prime
def is_prime(n):
  if n < 2: return False
  if n == 2 or n == 3: return True
  if n % 2 == 0 or n % 3 == 0: return False

  i = 3
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
  if b == 0:
    return a
  return gcd(b, a%b)

# lcm
def lcm(a, b):
  return a//gcd(a, b)*b//gcd(a, b)


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
