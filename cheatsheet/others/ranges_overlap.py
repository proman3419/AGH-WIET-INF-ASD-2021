def ranges_overlap(_r1, _r2):
  def one_way(r1, r2):
    if r1[0] == r1[1] == r2[0] == r2[1]: # jeden punkt
      return False

    res = (r1[0] <= r2[0] and r2[1] <= r1[1]) # r2 c r1
    res = res or (r1[0] < r2[0] < r1[1]) # poczatek r2 c r1
    res = res or (r1[0] < r2[1] < r1[1]) # koniec r2 c r1

    return res

  return one_way(_r1, _r2) or one_way(_r2, _r1)


tests = [
         [(0, 2), (1, 3), True],
         [(1, 3), (0, 2), True],
         [(0, 1), (1, 2), False],
         [(1, 2), (0, 1), False],
         [(1, 3), (0, 3), True],
         [(0, 3), (1, 3), True],
         [(0, 3), (0, 2), True],
         [(0, 2), (0, 3), True],
         [(0, 4), (2, 3), True],
         [(2, 3), (0, 4), True],
         [(0, 1), (2, 3), False],
         [(2, 3), (0, 1), False]]

for t in tests:
  print(t[0], t[1], 'expected:', t[2])
  res = ranges_overlap(t[0], t[1])

  if res != t[2]:
    print('failed')
    break
else:
  print('OK')
