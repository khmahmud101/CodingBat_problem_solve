def cigar_party(cigars, is_weekend):
  if (cigars>=40 and cigars <= 60) and is_weekend is False:
    return True
  elif (cigars>=40 and cigars <= 60) and is_weekend is True:
    return True
  elif  (cigars > 60) and is_weekend is True:
    return True
  else:
    return False