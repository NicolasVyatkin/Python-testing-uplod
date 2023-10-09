# Stock Profit

# Your function must return this maximum possible profit for given price fluctuations. If it's not
#     possible to make any profit with given prices (it's <= 0), your function should return 0.

# Input: Stock prices as list of integers (int).

# Output: Maximum possible profit as an integer (int).

# Examples:

# assert stock_profit([2, 3, 4, 5]) == 3
# assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
# assert stock_profit([4, 3, 2, 1]) == 0
# assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4

# Preconditions:

# len(stock) > 1;
# 0 <= price <= 1000.

################################################ SOLUTION#####################################################
import numpy as np


def stock_profit(stock: list[int]) -> int:
    max_profit_val, current_max_val = 0, 0
    for price in reversed(stock):
        current_max_val = max(current_max_val, price)
        potential_profit = current_max_val - price
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))
################################################### OR########################################################


def stock_profit(stock: list) -> int:
    # Initialize Variables
    current_maximum = 0
    # Initialize Variables
    maximum_profit = 0
    # Loop over all prices in reversed order as max has to be found before min
    for price in reversed(stock):
        # ... if current value is a new max, this will be our new max.
        current_maximum = max(price, current_maximum)
        # ... calculate a possible profit
        possible_profit = current_maximum - price
        # ... and get the maximum of current possible and max profit
        maximum_profit = max(possible_profit, maximum_profit)
    return maximum_profit


################################################### OR########################################################
stock_profit = p = lambda s: len(s) and max(max(s)-s[0], p(s[1:]))
################################################### OR########################################################


def stock_profit(stock: list[int]) -> int:
    max_profit = 0
    buy = stock[0]
    for sell in stock:
        profit = sell - buy
        max_profit = max(max_profit, profit)
        if sell < buy:
            buy = sell
    return max_profit

################################################### OR########################################################


def stock_profit(stock: list[int], max_val: int = 0) -> int:
    # compare max value with first value (recursive function)
    tmp_val = stock[np.argmax(stock)] - stock[0]

    # store max value
    if max_val < tmp_val:
        max_val = tmp_val

    if len(stock) == 2:
        # end of recursion
        return max_val
    else:
        return stock_profit(stock[1:], max_val)
