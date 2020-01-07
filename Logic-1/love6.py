def love6(a, b):
  res = a+b
  sub = a-b
  sub2 = b-a
  if (a is 6 or b is 6) or res == 6 or sub == 6 or sub2 == 6:
    return True
  else:
    return False
