# 1st Solution
def plus_one(digits):

    digit = 1

    for i in range(len(digits)):
        digit += digits[i] * 10 ** (len(digits) - i - 1)

    return [int(x) for x in str(digit)]

# 2nd Solution
def plus_one_2(digits):

    carry = 1

    for i in range(len(digits)-1, -1, -1):

        carry, digits[i] = divmod(digits[i] + carry, 10)

    return digits if not carry else [carry] + digits