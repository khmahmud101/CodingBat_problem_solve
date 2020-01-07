def first_last6(nums):
  if len(nums) == 0:
    return " list is empty"
  elif nums[0] == 6 or nums[-1] == 6:
    return  True
  else:
    return False
