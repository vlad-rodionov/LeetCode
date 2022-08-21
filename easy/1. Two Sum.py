def two_sum(nums, target):
    cashe = {}

    for i in range(len(nums)):
        if nums[i] in cashe:
            return [cashe[nums[i]], i]
        else:
            cashe[target - nums[i]] = i
