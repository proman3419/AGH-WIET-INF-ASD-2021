from random import randint


# sqrt(n)*logn + n -> O(sqrt(n)*logn)
def sieve(n):
  n += 1 # zeby w rangeu nie dodawac
  A = [True]*n

  i = 2
  primes_cnt = n - 2 # bez 0 i 1
  while i*i < n: # O(sqrt(n))
    if A[i]:
      for j in range(i*i, n, i): # O(logi) <= O(logn)
        if A[j]:
          primes_cnt -= 1
        A[j] = False
    i += 1

  primes = [-1]*primes_cnt
  j = 0
  for i in range(2, n): # O(n)
    if A[i]:
      primes[j] = i
      j += 1

  return primes, primes_cnt


# sqrt(n)*logn + n*primes_cnt + primes_cnt -> O(n*primes_cnt)
def longest_seq_common_gcd(A, n):
  primes, primes_cnt = sieve(n) # O(sqrt(n)*logn)
  prime_divs_cnt = [0]*primes_cnt
  for i in range(n): # O(n)
    for j in range(primes_cnt): # O(primes_cnt) < O(n)
      if A[i]%primes[j] == 0:
        prime_divs_cnt[j] += 1

  _max = prime_divs_cnt[0]
  for i in range(1, primes_cnt): # O(primes_cnt) < O(n)
    if prime_divs_cnt[i] > _max:
      _max = prime_divs_cnt[i]

  return _max


n = 10
A = [randint(0, n) for _ in range(n)]
print(longest_seq_common_gcd(A, n))
