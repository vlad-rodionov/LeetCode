def peak_index_in_mountain_array(arr):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] > arr[mid + 1]:
            right = mid

        if arr[mid] > arr[mid - 1]:
            left = mid
