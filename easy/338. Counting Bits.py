# 1st Solution, used bin()

def count_bits(n):

    # количество единиц в двоичном виде для всех чисел от 0 до n
    ans = []

    num = 0

    while num <= n:
        ones = bin(num)[2:].count('1')

        ans.append(ones)
        num += 1

    return ans

# 2nd Solution, w/o bin()

def count_bits_2(n):

    ans = []

    for i in range(n+1):

        cur = 0

        while i:
            cur += i & 1
            i >>= 1

        ans.append(cur)

    return ans
