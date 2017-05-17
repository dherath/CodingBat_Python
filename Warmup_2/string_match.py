def string_match(a, b):
  count =0
  times = min (len(b),len(a))
  for i in range (times-1):
    b_str = b[i:i+2]
    a_str = a[i:i+2]
    if a_str == b_str :
      count = count +1
  return count
