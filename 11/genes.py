class BSTNode:
  def __init__(self):
    self.A = None
    self.C = None
    self.G = None
    self.T = None
    self.end = False    


# O(log(max_seq_len))
def add(tree, seq):
  curr = tree
  for ch in seq:
    if ch == 'A':
      if curr.A is None: curr.A = BSTNode()
      curr = curr.A
    elif ch == 'C':
      if curr.C is None: curr.C = BSTNode()
      curr = curr.C
    elif ch == 'G':
      if curr.G is None: curr.G = BSTNode()
      curr = curr.G
    elif ch == 'T':
      if curr.T is None: curr.T = BSTNode()
      curr = curr.T

  if curr.end:
    return None

  curr.end = True
  
  return tree


# O(n*log(max_seq_len))
def check_genes(A):
  if len(A) == 0:
    return None

  tree = BSTNode()

  for seq in A:
    tree = add(tree, seq)

    if tree is None:
      return False

  return True


# True
A = ['GACTTG',
     'G',
     'CAGTAC',
     'CGA']

# False
A = ['AGCTCGGCA',
     'AGCTCGGCA']

print(check_genes(A))
