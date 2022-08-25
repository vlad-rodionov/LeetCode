"""
Dutch national flag problem
"""


def sort_colors(nums):

    mid = 1
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        if nums[j] < mid:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] > mid:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        else:
            j += 1
