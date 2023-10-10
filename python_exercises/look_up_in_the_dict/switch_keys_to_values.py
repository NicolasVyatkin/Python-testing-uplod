# Switch Keys to Values

# You are given a dictionary, where keys and values are strings. Your function should return a dictionary as
# well, where keys and values from input dictionary are switched: input keys become output values and vice
# versa. Looks easy? It is so! The only thing left to mention: the values in the result dictionary should
# be sets (so the input key(s) - the element(s) of the set). Good luck!

# Input: A dictionary.

# Output: A dictionary.

# Examples:

# assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
#     "red": {"car", "rouses"},
#     "blue": {"sky"},
# }
# assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
#     "one": {"3", "1"},
#     "two": {"4", "2"},
# }
# assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
#     "b": {"a"},
#     "c": {"b"},
#     "a": {"c"},
# }

################################################ SOLUTION#####################################################
from pandas import DataFrame
from typing import Dict
from collections import defaultdict


def switch_dict(data: dict[str, str]) -> dict[str, str]:
    res_dict = {}

    for key in data:
        value = data[key]
        new_value = res_dict.get(value, set())
        new_value.add(key)
        res_dict[value] = new_value

    return res_dict


################################################### OR########################################################


def switch_dict(data):
    result = defaultdict(set)
    for key, value in data.items():
        result[value].add(key)
    return result

################################################### OR########################################################


def switch_dict(data: dict) -> dict:
    lst = list(data.items())
    res = defaultdict(set)
    for k, v in lst:
        res[v].add(k)

    return dict(res)
################################################### OR########################################################


def switch_dict(data: dict) -> dict:
    res = {}

    for k, v in data.items():
        if v not in res:
            res[v] = {k}
        else:
            res[v].add(k)

    return res

################################################### OR########################################################


def switch_dict(data: Dict) -> Dict:
    return {value: {key for key in data if data[key] == value}
            for value in data.values()}


def switch_dict(data: Dict) -> Dict:
    df = DataFrame({'keys': data.keys(), 'values': data.values()})
    grouped = df.groupby('values')['keys'].apply(lambda x: x.values.tolist())

    return {key: set(values) for key, values in grouped.items()}
