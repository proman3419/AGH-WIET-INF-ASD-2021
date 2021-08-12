from math import inf


# O(n^2)
def find_max_path(G, V):
  n = len(G)

  # F[i] - max waga sciezki do i-tego wierzcholka wlacznie
  F = [-inf]*n
  F[0] = V[0] # zakladam, ze korzen to wierzcholek 0

  def rec(i):
    nonlocal G, V, F, n

    for j in range(n):
      if G[i][j] == 1:
        F[j] = max(F[j], F[i] + V[j])
        G[i][j] = G[j][i] = 0
        rec(j)

  rec(0)

  return max(F)


# 111
G = [[0, 1, 1, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0, 0, 0], 
     [1, 0, 0, 1, 1, 1, 0], 
     [0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 1, 0, 0, 0, 1], 
     [0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 0, 1, 0, 0]]

V = [0, 10, 15, 11, -4, 16, 100] # wagi wierzcholkow

# 9409
G = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

V = [10, -100, 40, 100, 1000, -500, 14, 27, 15, 9999]

print(find_max_path(G, V))
