def final_value_after_operations(operations):

    cache = {'--X': -1,
             'X--': -1,
             'X++': 1,
             '++X': 1}
    ans = 0
    for i in operations:
        ans += cache[i]

    return ans