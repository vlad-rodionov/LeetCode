def longest_common_prefix(strs):
    lcp = min(strs, key=len)

    for word in strs:
        while not word.startswith(lcp):
            lcp = lcp[:len(lcp) - 1]
            if lcp == '':
                return lcp

    return lcp
