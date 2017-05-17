def array123(nums):
  temp = [1,2,3]
  for i in range (len(nums)-2) :
    sub= nums[i:i+3]
    if temp == sub :
      return True
  return False
