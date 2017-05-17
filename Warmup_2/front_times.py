def front_times(str, n):
  if len(str) < 3 :
    temp = str
  else :
    temp = str[0:3]
  word =''
  for index in range(n):
    word = word + temp
  return word
