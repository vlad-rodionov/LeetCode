def convert_to_title(n):

    ans = ''

    while n:
        ans += chr(65 + (n - 1) % 26)

        n = (n - 1) // 26

    return ans[::-1]
