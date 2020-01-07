def rotate_left3(nums):
  result = nums.pop(0)
  nums.append(result)
  return nums