def max_profit(prices, start, end):

    if end <= start:
        return 0

    # Initialise the profit
    profit = 0
    curr_profit = 0

    # The day at which user should buy the stock
    for i in range(start, end, 1):

        # The day at which the stock must be sold
        for j in range(i + 1, end + 1):

            # If buying the stock at ith day and selling it at jth day is profitable
            if price[j] > price[i]:
                # current profit
                curr_profit = price[j] - price[i]

                # Update the maximum profit so far
                profit = max(profit, curr_profit)

    return profit


# giving price in list
price = [7, 1, 5, 3, 6, 4]
# taking list length to determine End point
n = len(price)
# printing the result
print(max_profit(price, 0, n - 1))
