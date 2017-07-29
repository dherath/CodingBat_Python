def alarm_clock(day, vacation):
  if vacation :
    st1="10:00"
    st2="off"
  else:
    st1="7:00"
    st2="10:00"
  
  if day==0 or day==6 :
    return st2
  else:
    return st1
    
