# 1st Solution

def is_subsequence(s: str, t: str) -> bool:
    if s == '':
        return True

    i = 0
    len_s = len(s)

    for char in t:

        if s[i] == char:
            i += 1

        if i == len_s:
            return True

    return i == len(s)


# 2nd Solution

def is_subsequence_2(s: str, t: str) -> bool:
    stack = list(s)[::-1]

    for char in t:

        if stack and stack[-1] == char:
            stack.pop()

    return len(stack) == 0
