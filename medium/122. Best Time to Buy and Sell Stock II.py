# 1st

def max_profit(prices):

    buy = prices[0]
    total_profit = 0

    for i in range(1, len(prices)):

        buy = min(prices[i], buy)
        sell = prices[i]

        profit = sell - buy

        if profit > 0:
            total_profit += profit
            buy = sell
        else:
            buy = sell

    return total_profit
