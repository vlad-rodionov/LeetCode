def is_happy(n):
    cache = {}

    while True:
        cache[n] = 1
        num = sum([int(char) ** 2 for char in str(n)])
        n = num
        if n == 1:
            return True
        if n in cache:
            return False
