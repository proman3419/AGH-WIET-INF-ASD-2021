# jezeli A[0] != 0 to nie istnieje taki indeks poniewaz
# mamy nadwyzke w wartosciach, ktorej nie jestesmy w stanie zredukowac
def find_equal_index_val_N(A):
  return A[0] == 0


# szukamy pierwszej nieujemnej liczby, jezeli znajduje sie ona pod indeksem k oraz:
# - A[k] == k -> k
# - A[k] < k -> szukamy zmodyfikowanym bin searchem
def find_equal_index_val_Z(A):
  pass
