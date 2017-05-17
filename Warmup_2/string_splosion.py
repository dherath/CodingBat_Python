def string_splosion(str):
  temp=''
  for i in range (len(str)+1):
    temp = temp + str[0:i]
  return temp  
