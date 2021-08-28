from zad3testy import runtests


class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None


def merge(head1, head2):
  l_w = Node() # lewy wartownik
  l_w.next = head1

  prev1 = l_w
  curr1 = head1
  curr2 = head2
  while curr1 is not None and curr2 is not None:
    if curr1.val < curr2.val:
      prev1, curr1 = curr1, curr1.next
    else:
      temp = curr2.next  # zeby nie stracic referencji
      prev1.next = curr2 # wstaw curr2
      curr2.next = curr1
      prev1 = curr2      # przygotuj prev1 i curr2 na nastepna iteracje
      curr2 = temp

  if curr2 is not None:
    prev1.next = curr2   # przylacz reszte

  return l_w.next


def find_series(curr):
  while curr.next is not None and curr.next.val >= curr.val:
    curr = curr.next
  _next = curr.next
  curr.next = None

  return (curr, _next)


def merge_sort(head):
  l_w = Node() # lewy wartownik
  l_w.next = head

  while True:
    if l_w is None or l_w.next is None:
      return l_w.next

    prev = l_w
    curr = l_w.next
    while curr is not None:
      s1_end, s1_next = find_series(curr)
      # jezeli nie zostal juz zaden element, nie da sie stworzyc niepuste s2
      if s1_next is None:
        break
      s2_end, s2_next = find_series(s1_next)

      curr = merge(curr, s1_next)
      prev.next = curr

      # ustal, ktory element bedzie na koncu nowego ciagu
      if s1_end.val >= s2_end.val:
        s1_end.next = s2_next
        prev = s1_end
      else:
        s2_end.next = s2_next
        prev = s2_end
      curr = s2_next

    # tylko jeden niemalejacy ciag => lista posortowana
    if prev == l_w and curr == l_w.next:
      break

  return l_w.next


def tasks(T):
  for i in range(len(T)-1):
    curr = T[i]
    while curr.next is not None:
      curr = curr.next

    curr.next = T[i+1]

  return merge_sort(T[0])


# to rozwiazanie jest lepsze, gdyby dzialalo :D (nie przechodzi 4. testu, zapetla sie)
# def tasks(T):
#   n = len(T)
#   i = 0
#   while 2**i < n:
#     j = 0
#     while j + 2**i < n:
#       merge(T[j], T[j+2**i])
#       j += 2**i + 1
#     i += 1

#   return T[0]


runtests( tasks )
