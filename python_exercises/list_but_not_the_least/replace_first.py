# # Replace First

# In a given sequence the first element should become the last one. An empty sequence or with only
# one element should stay the same.

# Input: List.

# Output: List or another Iterable (tuple, iterator, generator).

# Examples:

# assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# assert replace_first([1]) == [1]
# assert replace_first([]) == []

################################################ SOLUTION#####################################################
import numpy as np
from typing import Iterable
from collections import deque
from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) > 0:
        res_list = []

        for i in items[:1]:
            res_list.append(i)
        return items[1:] + res_list
    else:
        return items
################################################### OR########################################################
# Change items IN-PLACE.


def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items

# Slices


def replace_first(items: list) -> list:
    return items[1:] + items[:1]


# collections.deque have an useful method: rotate.


def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items

################################################### OR########################################################


def replace_first(l): return l[1 % len(l):]+l[:1 %
                                              len(l)] if not len(l) == 0 else l
################################################### OR########################################################


def replace_first(lst):
    if len(lst):
        lst.append(lst.pop(0))
    return lst

################################################### OR########################################################


def replace_first(items: list) -> Iterable:
    # your code here
    return np.roll(items, -1)
