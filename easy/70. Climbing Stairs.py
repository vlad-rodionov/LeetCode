def climbing_stairs(n):

    a = 0
    b = 1
    i = 0

    while i < n:
        a, b = b, a + b
        i += 1

    return b
