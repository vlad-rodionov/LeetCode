def valid_perfect_sqare(num):

    if num == 1:
        return True

    left, right = 1, num // 2

    while left <= right:

        mid = (left + right) // 2

        square = mid * mid

        if square == num:
            return True

        if square > num:
            right = mid - 1
        else:
            left = mid + 1

    return False
