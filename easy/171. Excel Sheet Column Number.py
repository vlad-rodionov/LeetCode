def title_to_number(column_title):
    ans, pos = 0, 0

    for letter in reversed(column_title):
        digit = ord(letter) - 64
        ans += digit * 26 ** pos
        pos += 1

    return ans
