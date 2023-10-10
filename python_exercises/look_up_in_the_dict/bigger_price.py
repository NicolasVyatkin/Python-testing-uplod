# Bigger Price

# You have a list with all available products in a store. The data is represented as a list of dicts

# Your mission here is to find the most expensive products in the list. The number of products we are looking
# for will be given as the first argument and the list of all products as the second argument.

# Input: int and list of dicts. Each dict has the two keys "name" and "price"

# Output: The same format as the second input argument.

# Example:

# assert bigger_price(
#     2,
#     [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1},
#     ],
# ) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
# assert bigger_price(
#     1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
# ) == [{"name": "whiteboard", "price": 170}]

################################################ SOLUTION#####################################################
import pandas as pd


def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    return (sorted(data, key=lambda x: x['price'], reverse=True))[:limit]


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)
################################################### OR########################################################


def bigger_price(limit, data):
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]

################################################### OR########################################################


def bigger_price(l, d): return sorted(d, key=lambda e: -e["price"])[:l]
################################################### OR########################################################


def bigger_price(limit, data):
    '''
    For large data and small limit it is better to find max values on the list
    one by one, the boundry can be calculated by having regard to sorting complexity
    therefore limit*n is versus n*log(n, 2) where n is data size
    '''
    from math import log
    size = len(data)
    if limit+1 > log(size, 2):  # +1 for finding min value
        # it is also possible to speed up
        # calcuations of log base 2 (not this time)
        return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]

    min_value = min(data, key=lambda x: x['price'])  # O(n)
    result = []
    for _ in range(limit):
        max_index = max(range(size), key=lambda x: data[x]['price'])  # O(n)
        result += [data[max_index]]
        data[max_index] = min_value  # we do not want to pop from the list here
        # as this has O(n) complexity, let's use O(1)
    return result

################################################### OR########################################################


def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code here
    df = pd.DataFrame(data)
    df.sort_values(by="price", ascending=False, inplace=True)
    df = df.iloc[0:limit].transpose().to_dict()
    return [df[i] for i in df]
