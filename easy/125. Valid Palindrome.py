import re


def is_palindrome(s):
    s = "".join(re.split("[^a-zA-Z0-9]*", s)).lower()

    return s == s[::-1]
