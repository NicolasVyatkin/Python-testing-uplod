# Best Stock

# You are given the current stock prices. You have to find out which stocks cost more.

# Input: The dictionary where the market identifier code is a key and the value is a stock price.

# Output: The market identifier code (ticker symbol) as a string.

# Example:

# assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
# assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
# 1
# 2
# Preconditions: All the prices are unique.

################################################ SOLUTION#####################################################

import pandas as pd


def best_stock(data: dict[str, float]) -> str:
    return max(data, key=data.get)


print("Example:")
print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))
################################################### OR########################################################


def best_stock(data):
    return max(data, key=data.__getitem__)

################################################### OR########################################################


def best_stock(d): return next(x for x in d if d[x] == max(d.values()))
################################################### OR########################################################


def best_stock(data):
    # your code here
    return (pd.Series(data).idxmax())
################################################### OR########################################################
