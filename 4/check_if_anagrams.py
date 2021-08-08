from random import randint


# O(n+k)
def check_if_anagrams(A, B, k=26, first_char='a'):
  n = len(A) # zal len(A) == len(B)
  ord_fc = ord(first_char)
  occurances = [0]*k

  for i in range(n):
    occurances[ord(A[i])-ord_fc] += 1

  for i in range(n):
    occurances[ord(B[i])-ord_fc] -= 1

  for i in range(k):
    if occurances[i] != 0:
      return False

  return True


def alloc(n):
  return [randint(0, 1000000000) for i in range(n)]


# O(n)
def check_if_anagrams_2(A, B, k=26, first_char='a'):
  n = len(A) # zal len(A) == len(B)
  ord_fc = ord(first_char)
  occurances = alloc(k) # w pythonie jest to O(k) ale traktujemy jak wykonanie malloca
  # poniewaz jest to zalezne od jezyka, nie od algorytmu i nie wykorzystujemy calej tej tablicy.
  # przygotowujemy elemnty w tablicy, ktorych bedziemy uzywac
  for i in range(n):
    occurances[ord(A[i])-ord_fc] = occurances[ord(B[i])-ord_fc] = 0

  for i in range(n):
    occurances[ord(A[i])-ord_fc] += 1
    occurances[ord(B[i])-ord_fc] -= 1

  for i in range(n):
    if occurances[ord(A[i])-ord_fc] != 0 or occurances[ord(B[i])-ord_fc] != 0:
      return False

  return True


# True
A = 'listen'; B = 'silent'

# False
A = 'sadf'; B = 'vzoc'

print(check_if_anagrams(A, B))
print(check_if_anagrams_2(A, B))
