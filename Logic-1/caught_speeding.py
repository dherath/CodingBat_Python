def caught_speeding(speed, is_birthday):
  val=0
  if is_birthday :
    val=5
  if speed>=81+val :
    return 2
  elif speed >= 61+val :
    return 1
  else :
    return 0
  
