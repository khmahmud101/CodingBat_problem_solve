def sum2(nums):
  if len(nums) < 2:
    return sum(nums)
  elif len(nums) == 0:
    return 0
  else:
    return nums[0] + nums[1]
