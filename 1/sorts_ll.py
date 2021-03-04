class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def insert(head, val):
  curr = head
  if curr.next == None:
    curr.next = Node(val)
  else:
    temp = curr.next
    curr.next = Node(val)
    curr.next.next = temp


def display(head):
  curr = head
  while curr is not None:
    print(curr.val, end=' ')
    curr = curr.next
  print()


def rem_max(head):
  prev = head
  curr = head.next
  prev_max = prev
  curr_max = curr

  while curr is not None:
    if curr.val > curr_max.val:
      prev_max = prev
      curr_max = curr
    prev, curr = curr, curr.next

  prev_max.next = curr_max.next

  return head, curr_max.val


def selection_sort(head):
  new_head = None
  while head.next is not None:
    rest, max_val = rem_max(head)
    new_head = Node(max_val, new_head)

  return Node(next=new_head)


def insertion_sort(head):
  new_head = Node()
  while head.next is not None:
    _, max_val = rem_max(head)
    insert(new_head, max_val)
  
  return new_head


head = Node()
insert(head, 1)
insert(head, 4)
insert(head, 7)
insert(head, 3)
insert(head, 2)
insert(head, 2)
insert(head, 5)
insert(head, 10)

head = selection_sort(head)
head = insertion_sort(head)
display(head)
