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
def remove(tree, key):
  node = find(tree, key)

  if node is None:
    return tree

  parent = node.parent

  # node jest lisciem
  if node.left is None and node.right is None:
    if parent is None:
      return None
    else:
      if parent.left == node:
        parent.left = None
      else:
        parent.right = None

  # node ma 2 dzieci
  elif node.left is not None and node.right is not None:
    prec = find_precursor(tree, node.key)
    node.key = prec.key
    remove(prec, prec.key)

  # node ma 1 dziecko
  else:
    # None or BSTNode -> BSTNode
    # BSTNode or None -> BSTNode
    # BSTNode1 or BSTNode2 -> BSTNode1
    if parent is None:
      return node.left or node.right

    if node == parent.left:
      parent.left = node.left or node.right
    else:
      parent.right = node.left or node.right

  return tree


def array_to_bst(A):
  if len(A) == 0:
    return None

  tree = BSTNode(A[0])

  for i in range(1, len(A)):
    tree = add(tree, A[i])

  return tree


# O(logn)
def find_precursor(tree, key) -> BSTNode:
  node = find(tree, key)

  if node is None:
    return None

  # w lewo i max w prawo
  if node.left is not None:
    node = node.left
    while node.right is not None:
      node = node.right

    return node

  # do gory dopoki obecny nie jest prawym dzieckiem lub nie ma rodzica
  parent = node.parent
  while parent is not None and parent.right != node:
    node = parent
    parent = node.parent

  if parent is None:
    return None
  else:
    return parent


# O(logn)
def find_successor(tree, key) -> BSTNode:
  node = find(tree, key)

  if node is None:
    return None

  # w prawo i max w lewo
  if node.right is not None:
    node = node.right
    while node.left is not None:
      node = node.left

    return node

  # do gory dopoki obecny nie jest lewym dzieckiem lub nie ma rodzica
  parent = node.parent
  while parent is not None and parent.left != node:
    node = parent
    parent = node.parent

  if parent is None:
    return None
  else:
    return parent


def print_node(node):
  print(f'key: {node.key}')
  print(f'nodes_cnt: {node.nodes_cnt}')

  if node.left is not None:
    print(f'left: {node.left.key}')
  else:
    print('left: None')

  if node.right is not None:
    print(f'right: {node.right.key}')
  else:
    print('right: None')


def print_nodes(tree):
  if tree is None:
    return

  print_nodes(tree.left)
  print_node(tree)
  print()
  print_nodes(tree.right)


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
