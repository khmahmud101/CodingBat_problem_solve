def sum67(nums):
    tot = 0
    found = False
    for i in range(len(nums)):
        if nums[i] == 6:
            found = True
        if not found:
            tot += nums[i]
        if nums[i] == 7 and found:
            found = False
    return tot

