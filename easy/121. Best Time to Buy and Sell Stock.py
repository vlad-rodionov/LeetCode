def max_profit(prices):

    buy = prices[0]
    current_profit = 0

    for i in range(1, len(prices)):

        buy = min(prices[i], buy)
        sell = prices[i]
        profit = sell - buy

        if profit > current_profit:
            current_profit = profit

    return current_profit
