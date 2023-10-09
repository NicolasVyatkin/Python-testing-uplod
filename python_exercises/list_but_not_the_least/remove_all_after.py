# Remove All After

# Not all of the elements are important. What you need to do here is to remove all of the elements after
# the given one from sequence.

# example

# For illustration, we have a sequence [1, 2, 3, 4, 5] and we need to remove all the elements that go after
# 3 - which are 4 and 5.

# We have two edge cases here:

# if a cutting element cannot be found, then the sequence shouldn't be changed;
# if the sequence is empty, then it should remains empty.
# Input: List of integers (int).

# Output: List or other Iterable (tuple, iterator, generator ...) of integers (int).

# Examples:

# assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
# assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
# assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
# assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]

################################################ SOLUTION#####################################################
import numpy as np
from typing import Iterable
from collections.abc import Iterable


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    final_list = []
    for i in items:
        final_list.append(i)
        if i == border:
            break
    return final_list
################################################### OR########################################################


def remove_all_after(items: list, border: int) -> list:
    try:
        return items[: items.index(border) + 1]
    except ValueError:
        return items
################################################### OR########################################################


def remove_all_after(items, border):
    return items[:items.index(border) + 1 if border in items else None]

################################################### OR########################################################


def remove_all_after(items: list, border: int) -> Iterable:
    # your code here
    return items[:1+np.where(np.array(items) == border)[0][0]] if border in items else items
