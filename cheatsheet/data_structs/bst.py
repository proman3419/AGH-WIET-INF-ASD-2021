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


def find_precursor(tree, key):
  node = find(tree, key)

  if node is None:
    return None

  # w lewo i max w prawo
  if node.left is not None and node.left.right is not None:
    node = node.left.right
    while node.right is not None:
      node = node.right

    return node.key

  # do gory dopoki obecny nie jest prawym dzieckiem lub nie ma rodzica
  parent = node.parent
  while parent is not None and parent.right != node:
    node = parent
    parent = node.parent

  if parent is None:
    return None
  else:
    return parent.key


def find_successor(tree, key):
  node = find(tree, key)

  if node is None:
    return None

  # w prawo i max w lewo
  if node.right is not None and node.right.left is not None:
    node = node.right.left
    while node.left is not None:
      node = node.left

    return node.key

  # do gory dopoki obecny nie jest lewym dzieckiem lub nie ma rodzica
  parent = node.parent
  while parent is not None and parent.left != node:
    node = parent
    parent = node.parent

  if parent is None:
    return None
  else:
    return parent.key


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
