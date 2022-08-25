"""
Classical Binary Search
"""


def search_insert(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:

        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1

        elif nums[mid] > target:
            end = mid - 1

        else:
            return mid

    return end + 1
