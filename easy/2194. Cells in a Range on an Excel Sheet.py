def cells_in_range(s):

    ans = []

    for i in range(ord(s[0]), ord(s[3]) + 1):

        for j in range(int(s[1]), int(s[4]) + 1):
            ans.append("{}{}".format(chr(i), j))

    return ans
