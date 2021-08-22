# szacowanie zlozonosci dla drzewa zbalansowanego


class BSTNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None


# O(logn)
def add(tree, key, parent=None):
  if tree is None:
    tree = BSTNode(key)
    tree.parent = parent
  elif key < tree.key:
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


# morris traversal
# algorytm sprowadza drzewo do posortowanej linked listy, ktora nastepnie przywraca do oryginalnego drzewa
# time O(n), space O(1)
def sum_bst(tree):
  _sum = 0
  curr = tree

  while curr is not None:
    if curr.left is None:
      # print(curr.key)
      _sum += curr.key
      curr = curr.right
    else:
      # szukamy poprzednika
      pre = curr.left
      # war 1 tworzenie, war 2 naprawianie
      while pre.right is not None and pre.right is not curr:
        pre = pre.right

      if pre.right is None: # tworzenie
        pre.right = curr
        curr = curr.left
      else: # naprawianie
        pre.right = None
        # print(curr.key)
        _sum += curr.key
        curr = curr.right

  return _sum


A = [10, 4, 3, 11, 5, 7, 6, 8]
tree = array_to_bst(A)

expected_sum = sum(A)
_sum = sum_bst(tree)
print(f'sum: {_sum}, expected sum: {expected_sum}')
