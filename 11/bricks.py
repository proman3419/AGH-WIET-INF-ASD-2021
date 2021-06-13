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
  # dodawnay klocek nachodzi od:
  # 1. prawej
  # 2. lewej
  elif (key[0] < tree.key[1] and tree.key[0] < key[1]) or \
       (tree.key[0] < key[1] and key[0] < tree.key[1]):
    tree.key = (min(tree.key[0], key[0]), max(tree.key[1], key[1]))
    tree.right = add(tree.right, key, tree)
  # nie nachodzi
  else:
    tree.left = add(tree.left, key, tree)
  
  return tree


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


def print_nodes(tree):
  if tree is None:
    return

  print_nodes(tree.left)
  print_node(tree)
  print()
  print_nodes(tree.right)


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


def get_height(tree):
  height = 0
  while tree is not None:
    height += 1
    tree = tree.right

  return height


def bricks(ranges):
  n = len(ranges)
  tree = BSTNode(ranges[0])
  for i in range(1, n):
    tree = add(tree, ranges[i])

  return get_height(tree)


# 3
ranges = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]

# 4
ranges = [(1, 3), (1, 5), (0, 5), (0, 6)]

# 3
ranges = [(0, 1), (2, 3), (0, 3), (0, 1)]

print(bricks(ranges))
