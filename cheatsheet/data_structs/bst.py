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

    child = node.left or node.right
    if node == parent.left:
      parent.left = child
    else:
      parent.right = child
    child.parent = parent

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


# O(n)
def bst_traversal(tree):
  prev = None
  curr = tree

  while curr.left is not None:
    curr = curr.left

  sorted_order = []

  while curr is not None:
    if prev is None:
      if curr.left is not None:
        curr = curr.left
      elif curr.right is not None:
        sorted_order.append(curr.key)
        curr = curr.right
      else:
        sorted_order.append(curr.key)
        prev, curr = curr, curr.parent
    elif prev.key < curr.key and curr.right is not None:
      sorted_order.append(curr.key)
      prev, curr = None, curr.right
    else:
      if curr.right is None:
        sorted_order.append(curr.key)
      prev, curr = curr, curr.parent

  return sorted_order


def print_node(node):
  print(f'key: {node.key}')

  if node.left is not None:
    print(f'left: {node.left.key}')
  else:
    print('left: None')

  if node.right is not None:
    print(f'right: {node.right.key}')
  else:
    print('right: None')

  if node.parent is not None:
    print(f'parent: {node.parent.key}')
  else:
    print('parent: None')


def print_nodes(tree):
  if tree is None:
    return

  print_nodes(tree.left)
  print_node(tree)
  print()
  print_nodes(tree.right)


def print_depth_first(tree):
  if tree is None:
    return

  print_depth_first(tree.left)
  print(tree.key)
  print_depth_first(tree.right)


def print_breadth_first(tree):
  if tree is None:
    print('Empty')
    return

  children = [tree]
  while len(children) > 0:
    _children = []
    
    for node in children:
      print(node.key, end=' ')
      if node.left is not None:
        _children.append(node.left)
      if node.right is not None:
        _children.append(node.right)

    print()
    children = _children 


def pretty_print_aux(self):
  # brak dziecka
  if self.right is None and self.left is None:
    line = '%s' % self.key
    width = len(line)
    height = 1
    middle = width // 2
    return [line], width, height, middle

  # tylko lewe dziecko
  if self.right is None:
    lines, n, p, x = pretty_print_aux(self.left)
    s = '%s' % self.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
    second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
    shifted_lines = [line + u * ' ' for line in lines]
    return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

  # tylko prawe dziecko
  if self.left is None:
    lines, n, p, x = pretty_print_aux(self.right)
    s = '%s' % self.key
    u = len(s)
    first_line = s + x * '_' + (n - x) * ' '
    second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
    shifted_lines = [u * ' ' + line for line in lines]
    return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

  # dwojka dzieci
  left, n, p, x = pretty_print_aux(self.left)
  right, m, q, y = pretty_print_aux(self.right)
  s = '%s' % self.key
  u = len(s)
  first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
  second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
  if p < q:
    left += [n * ' '] * (q - p)
  elif q < p:
    right += [m * ' '] * (p - q)
  zipped_lines = zip(left, right)
  lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
  return lines, n + m + u, max(p, q) + 2, n + u // 2


def pretty_print(self):
  lines, *_ = pretty_print_aux(self)
  for line in lines:
    print(line)


A = [20, 10, 27, 5, 15, 13, 22, 30, 28, 35, 40]
tree = array_to_bst(A)

pretty_print(tree)
print()

print(bst_traversal(tree))
print()

# lisc
tree = remove(tree, 5)
print_node(find(tree, 10))
print(bst_traversal(tree))

# 1 dziecko
print()
tree = remove(tree, 15)
print_node(find(tree, 13))
print(bst_traversal(tree))

# 2 dzieci
print()
tree = remove(tree, 30)
print_node(find(tree, 27))
print(bst_traversal(tree))

print()
pretty_print(tree)
