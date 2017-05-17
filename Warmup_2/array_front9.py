def array_front9(nums):
  if len(nums) < 4:
    sz = len(nums)
  else :
    sz = 4
  for i in range (sz) :
    if nums[i] == 9 :
      return True
  return False
