from random import randint, shuffle, seed

def linearselect( A, k ):
  # Tu prosze zaimplementowac swoja funkcje
  return 0



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

