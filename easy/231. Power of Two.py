def is_power_of_two(n):
    cnt = 0
    while n > 0:
        if n & 1 == 1:
            cnt = cnt + 1
        n = n >> 1

    if cnt == 1:
        return True

    return False
