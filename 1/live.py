def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

# best n
# worst n^2
# stable
def bubble_sort(arr):
  n = len(arr)
  for i in range(0, n-1):
    ifSwapped=False
    for j in range(0, n - i -1):
      if(arr[j] > arr[j+1]):
        swap(arr, j, j+1)
        ifSwapped=True
    
    if (ifSwapped==False):
      break
      
  return arr


# best n^2
# worst n^2
# stable
def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_i = i
    for j in range(i+1, n):
      if arr[j] < arr[min_i]:
        min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]

  return arr


# best n
# worst n^2
# stable
def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

  return arr

# >/< => stable
# >=/=< => unstable
# ???


class Node():
  def __init__(self, val, next):
    self.val = val
    self.next = next


def to_list(p):
  arr = []
  while p is not None:
    arr.append(p.val)
    p = p.next
  print(arr)


def insert(l, val):
  p = l
  if p.next is None:
    p.next = Node(val, None)
    return p

  prev = p
  p = p.next
  while p is not None and p.val < val:
    prev = p
    p = p.next
  q = Node(val, prev.next)
  prev.next = q
  return l


p = Node("*", None)
p = insert(p, 4)
p = insert(p, 2)
p = insert(p, 3)
p = insert(p, 6)
to_list(p)


def remove_max(first):
  curr = first.next
  prev = first
  prev_max = prev
  curr_max = curr

  while curr is not None:
    if curr.val > curr_max.val:
      prev_max = prev
      curr_max = curr
    prev, curr = curr, curr.next

  prev_max.next = curr_max.next
  return first, curr_max.val


def selection(first):
  curr = first.next
  new_list = None
  while first.next is not None:
    rest, max_val = remove_max(first)
    new_list = Node(max_val, new_list)

  return Node('*', new_list)
