def combo_string(a, b):
  if a == b:
    return "str can not be same"
  elif len(a) > len(b):
    return b + a + b
  else:
    return a + b + a
