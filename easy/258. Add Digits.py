def add_digits(num):

    while len(str(num)) > 1:
        num = sum([int(char) for char in str(num)])

    return num
