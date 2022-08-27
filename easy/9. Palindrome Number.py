# 1st Solution
def is_palindrome(x):

    if x < 0:
        return False

    new = 0
    orig = x

    while orig:
        orig, d = divmod(orig, 10)

        new = new * 10 + d

    return new == x

# 2nd Solution
def is_palindrome_2(x):

    return ''.join(reversed(str(x))) == str(x)
