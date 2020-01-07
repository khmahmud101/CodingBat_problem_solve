def max_end3(nums):
    res = max(nums[0], nums[-1])
    li = []
    for i in range(3):
        li.append(res)

    return li