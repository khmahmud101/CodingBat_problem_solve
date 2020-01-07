def left2(str):
  if str < 2:
    return str
  else:
   first = str[:2]
   return str[2:] + first