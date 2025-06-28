def common_part(a, b):
  a_1, b_1 = a
  a_2, b_2 = b

  if a_1 > a_2:
    a_1, b_1, a_2, b_2 = a_2, b_2, a_1, b_1

  if b_1 > a_2:
    if b_1 <= b_2:
      l = b_1 - a_2
      return l, [a_2, b_1]
    else:
      l = b_2 - a_2
      return l, [a_2, b_2]

  return 0, []

print(common_part((1, 4), (1, 4))
