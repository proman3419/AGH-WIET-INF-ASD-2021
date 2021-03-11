class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y


class Rectangle:
  def __init__(self, x1, y1, x2, y2):
    self.P1 = Point(x1, y1)
    self.P2 = Point(x2, y2)

  def field(self, y=None):
    if y == None:
      return abs(self.P1.x-self.P2.x)*abs(self.P1.y-self.P2.y)
    else:
      return abs(self.P1.x-self.P2.x)*abs(y-self.P2.y)


def sum_below(rects, y):
  _sum = 0
  cnt = 0
  for r in rects:
    if r.P1.y <= y:
      _sum += r.field()
      cnt += 1
    elif r.P2.y < y:
      _sum += r.field(y)

  return (_sum, cnt)


def min_max(rects):
  _min = rects[0].P2.y
  _max = rects[0].P1.y
  n = len(rects)

  for i in range(1, n-1, 2):
    if rects[i].P1.y < rects[i+1].P1.y:
      curr_max = rects[i+1].P1.y
    else:
      curr_max = rects[i].P1.y

    if rects[i].P2.y > rects[i+1].P2.y:
      curr_min = rects[i+1].P2.y
    else:
      curr_min = rects[i].P2.y

    if curr_min < _min: _min = curr_min
    if curr_max > _max: _max = curr_max

  if n%2 == 0:
    if rects[-1].P2.y < _min:
      _min = rects[-1].P2.y
    elif rects[-1].P1.y > _max:
      _max = rects[-1].P1.y

  return (_min, _max)


def find_rects_cnt(rects, A):
  prev_A = -1
  prev_A_cmp = 0 # -1 -> < A; 1 -> > A
  prev_cnt = -1
  y = rects[0].P1.y
  _min, _max = min_max(rects)

  # special case _max
  _max_res = sum_below(rects, _max)
  if _max_res[0] <= A: return _max_res[1]

  while y < _max - 0.1:
    res = sum_below(rects, y)

    curr_A_cmp = -1 if res[0] < A else 1

    if res[0] == A or prev_A == res[0] or (prev_A_cmp*curr_A_cmp == -1 and prev_cnt == res[1]):
      break

    if res[0] < A:
      y = (y + _max)/2
    else:
      y = (y + _min)/2

    prev_A = res[0]
    prev_A_cmp = curr_A_cmp
    prev_cnt = res[1]

  return res[1]


# A < 3 => 0
# 3 <= A < 13 => 1
# 13 <= A < 16 => 3
# A >= 16 => 5
A = 12
# assumed that the first point is the upper-left one
rects = [Rectangle(1, -1, 4, -2),
         Rectangle(1, 3, 2, 1),
         Rectangle(3, 5, 4, 1),
         Rectangle(1, 5, 2, 4),
         Rectangle(-4, 3, -1, 1)]

print(find_rects_cnt(rects, A))
