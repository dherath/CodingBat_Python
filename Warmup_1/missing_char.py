def missing_char(str, n):
  if n==0 :
    return str[1:]
  elif n==len(str) :
    return str[:-1]
  else :
    return str[0:n]+str[n+1:]
