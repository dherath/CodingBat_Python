def not_string(str):
  temp = str[:3]
  if temp == 'not':
    return str
  else:
    return "not "+str
