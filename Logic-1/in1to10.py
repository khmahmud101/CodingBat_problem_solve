def in1to10(n, outside_mode):
  if outside_mode is False and (n >= 1 and n <= 10):
    return True
  elif outside_mode is True and( n <= 1 or n >= 10 ):
    return True
  else:
    return False