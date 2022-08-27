def add_digits(num):

    while len(str(num)) > 1:
        num = sum([int(char) for char in str(num)])

    return num


# 2nd solution. Digital Root
def add_digits_2(num):
    if num <= 9:
        return num

    return 1 + (num - 1) % 9

# 3rd  Solution. Divmod
def add_digits_3(num):

    while num >= 10:

        cur = num
        new_num = 0

        while cur:
            cur, dec = divmod(cur, 10)
            new_num += dec

        num = new_num

    return num
