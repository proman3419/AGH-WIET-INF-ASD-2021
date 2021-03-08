def sum_below(pts, y):
  _sum = 0
  cnt = 0
  for p in pts:
    if p[0][1] <= y:
      _sum += (p[1][0]-p[0][0])*(p[0][1]-p[1][1])
      cnt += 1

  return (_sum, cnt)


P = 10**2
pts = [((1, 10), (3, 8)), ((2, 10), (3, 6))]

y_prev = -1
y = pts[0][0][1]
e = 0.1
while abs(y - y_prev) > e:
  res = sum_below(pts, y)
  if res[0] < P:
    y_prev, y = y, 1.5*y
  else:
    y_prev, y = y, 0.5*y

print(res[1])