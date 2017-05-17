def last2(str):
  if len(str) < 2 :
    return 0
    
  temp= str[len(str)-2:]
  n=0
  
  for i in range(len(str)-2):
    substr=str[i:i+2]
    if substr == temp :
      n = n +1
  
  return n    
  
