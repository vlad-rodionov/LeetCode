def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    window_avg = window_sum / k

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]

        cur_avg = window_sum / k

        window_avg = max(window_avg, cur_avg)

    return window_avg
