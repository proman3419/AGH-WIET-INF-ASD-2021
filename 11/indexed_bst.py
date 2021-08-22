# szacowanie zlozonosci dla drzewa zbalansowanego


class BSTNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None
    self.nodes_cnt = 1


# O(logn)
def add(tree, key, parent=None):
  if tree is None:
    tree = BSTNode(key)
    tree.parent = parent
  else:
    tree.nodes_cnt += 1
    if key < tree.key:
      tree.left = add(tree.left, key, tree)
    elif key > tree.key:
      tree.right = add(tree.right, key, tree)
  
  return tree


def array_to_bst(A):
  if len(A) == 0:
    return None

  tree = BSTNode(A[0])

  for i in range(1, len(A)):
    tree = add(tree, A[i])

  return tree


# O(logn)
def find(tree, key):
  while tree is not None:
    if tree.key == key:
      return tree
    elif key < tree.key:
      tree = tree.left
    else:
      tree = tree.right

  return None


# O(logn)
def find_ith_node(tree, i):
  n = tree.nodes_cnt

  if i >= n:
    return None

  j = 0 if tree.left is None else tree.left.nodes_cnt # indeks roota
  curr = tree

  while j != i:
    if j < i:
      curr = curr.right
      l_ns = 0 if curr.left is None else curr.left.nodes_cnt
      j = j + l_ns + 1
    else:
      curr = curr.left
      r_ns = 0 if curr.right is None else curr.right.nodes_cnt
      j = j - r_ns - 1

  return curr.key


# O(logn)
def find_node_order(tree, node):
  if node is None:
    return None

  prev = None
  curr = node
  i = 0

  while True:
    # jezeli nie przyszlismy z lewej (wtedy liczylibysmy te same nody)
    if prev is None or curr.left != prev:
      if curr.left is not None:
        i += curr.left.nodes_cnt

    if curr.parent is None: # doszlismy do roota
      break

    prev, curr = curr, curr.parent

    if curr.right == prev: # parent jest mniejszy
      i += 1

  return i


# A = [20, 10, 27, 5, 15, 13, 22, 30, 28, 35, 40]
A = [10, 5, 2, 6, 7, 8, 9, 3, 1, 0, 4, 11, 20, 19, 18, 15, 17, 99, 98, 100]
tree = array_to_bst(A)

A.sort()
for i in range(len(A)):
  res_1 = find_ith_node(tree, i)
  res_2 = find_node_order(tree, find(tree, A[i]))

  print(f'i: {i}, find_ith_node: {res_1}')
  print(f'A[i]: {A[i]}, find_node_order: {res_2}')
  print()

  if A[i] != res_1:
    print('find_ith_node failed')
    break

  if i != res_2:
    print('find_node_order failed')
    break
else:
  print('OK')
