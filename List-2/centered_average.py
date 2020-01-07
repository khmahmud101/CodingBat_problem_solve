
def centered_average(nums):
	small = min(nums)
	big = max(nums)
	nums.remove(small)
	nums.remove(big)

	return int(sum(nums) / len(nums))