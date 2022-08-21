def running_sum(nums):

    for i in range(1, (len(nums))):
        nums[i] += nums[i-1]

    return nums