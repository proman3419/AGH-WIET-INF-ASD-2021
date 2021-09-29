# O(n+T)

# symulujemy wykonywane wcisniecia przelacznikow zapamietujac obecny stan wszystkich lampek.
# gdy nastepuje zmiana koloru sprawdzamy czy zmieniony zostal z niebieskiego lub na niebieski
# i odpowiednio odejmujemy lub dodajemy 1 do licznika zapalonych niebieskich.
# na koniec rozpatrywania danej operacji sprawdzamy czy licznik zapalonych niebieskich
# jest wiekszy od dotychczasowego maksymalnego i go aktualizujemy, jezeli trzeba


from zad3testy import runtests


def lamps( n,T ):
  m = len(T)

  states = [0]*n # 0 - zielony, 1 - czerwony, 2 - niebieski
  max_b = curr_b = 0

  for i in range(m):
    s, e = T[i]
    for j in range(s, e+1):
      if states[j] == 2:
        curr_b -= 1
      elif states[j] == 1:
        curr_b += 1

      states[j] = (states[j]+1)%3

    if curr_b > max_b:
      max_b = curr_b

  return max_b

  
runtests( lamps )
