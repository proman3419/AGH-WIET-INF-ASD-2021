from zad3testy import runtests
import math


# a^x oraz log(e, a) sa funkcjami rosnacymi czyli
# dla x1 > x2: a^x1 > a^x2 oraz log(e1, a) > log(e2, a).
# x jest rozlozone rownomiernie wiec bucket sort bedzie w czasie liniowym


# O(n^2)
def insertion_sort(A):
  n = len(A)
  for i in range(1, n): # O(n)
    key = A[i]
    j = i - 1
    while j >= 0 and A[j][1] > key[1]: # <= O(j) <= O(n)
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

  return A


def find_bucket(val, n, _min, _max):
  i = int((val-_min)/(_max-_min)*n)
  if i == n: i -= 1
  
  return i


# 3n + n^2 -> O(n^2) - najgorszy przypadek
# 4n -> O(n) - rozklad jednostajny
def bucket_sort(A, _min, _max):
  n = len(A)
  B = [0]*n

  for i in range(n): # O(n)
    B[i] = []

  for i in range(n): # O(n)
    B[find_bucket(A[i][1], n, _min, _max)].append(A[i])

  for i in range(n): # O(n)
    insertion_sort(B[i])

  i = 0
  # O(n^2) - najgorszy przypadek
  # O(n) - rozklad jednostajny
  for j in range(n): # O(n)
    for k in range(len(B[j])): # O(len(B[j])) <= O(n)
      A[i] = B[j][k]
      i += 1

  return A

                 
def fast_sort(tab, a):
  tab = [(e, math.log(e, a)) for e in tab]
  tab = bucket_sort(tab, 0, 1)
  tab = [e[0] for e in tab]

  return tab


runtests( fast_sort )
