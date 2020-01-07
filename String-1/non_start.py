def non_start(a, b):
  omit = "omit"
  if omit in a or omit in b:
    return "not concatenation"
  elif a <1 or b< 1:
    return "str not less than one"
  else:
    return a[1:] + b[1:]