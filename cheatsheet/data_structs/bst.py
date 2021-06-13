class BSTNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None


def add(tree, key, parent=None):
  if tree is None:
    tree = BSTNode(key)
    tree.parent = parent
  elif key < tree.key:
    tree.left = add(tree.left, key, tree)
  elif key > tree.key:
    tree.right = add(tree.right, key, tree)
  
  return tree


def find(tree, key):
  while tree is not None:
    if tree.key == key:
      return tree
    elif key < tree.key:
      tree = tree.left
    else:
      tree = tree.right

  return None


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


tree = BSTNode(20)

tree = add(tree, 10)
tree = add(tree, 27)

tree = add(tree, 5)
tree = add(tree, 15)
tree = add(tree, 13)

tree = add(tree, 22)
tree = add(tree, 30)
tree = add(tree, 28)
tree = add(tree, 35)
tree = add(tree, 40)

print_breadth_first(tree)

# lisc
print()
tree = remove(tree, 5)
print_node(find(tree, 10))

# 1 dziecko
print()
tree = remove(tree, 15)
print_node(find(tree, 10))

# 2 dzieci
print()
tree = remove(tree, 30)
print_node(find(tree, 27))

print()
print_breadth_first(tree)
