# jak nie znalazlo sie zadnego dluzszego niz 1 mozna by zwracac jakakolwiek litere ale uznalem to za zbedne
def print_solution(s, F):
  n = len(s)

  for i in range(n):
    for j in range(n-1, i+1, -1):
      if F[i][j]:
        print(s[i:j+1])
        return


def find_longest_palindrome(s):
  n = len(s)

  # F[i][j] - czy substring od i do j jest palindromem
  F = [[i == j for i in range(n)] for j in range(n)]

  for i in range(n-1):
    F[i][i+1] = (s[i] == s[i+1])

  for j in range(2, n):
    for i in range(n-j):
      F[i][j+i] = ((s[i] == s[j+i]) and F[i+1][j+i-1])

  print_solution(s, F)

# kajak
# s = 'romkajakan'

# cbc
s = 'asdfvxcbcmzkmsdafmktriowre'

find_longest_palindrome(s)
