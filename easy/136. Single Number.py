from functools import reduce


def single_number(nums):
    return reduce(lambda prev_num, num: prev_num ^ num, nums)
