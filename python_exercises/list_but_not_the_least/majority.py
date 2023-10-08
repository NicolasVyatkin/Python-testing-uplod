# Majority

# We have a list of logic values (bool). Let's check if the majority of elements are True.


# Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have
# an equal amount, function should return False.

# Input: A list of logic values (bool).

# Output: A logic value (bool).

# Examples:

# assert is_majority([True, True, False, True, False]) == True
# assert is_majority([True, True, False]) == True
# assert is_majority([True, True, False, False]) == False
# assert is_majority([True, True, False, False, False]) == False

################################################ SOLUTION#####################################################
import numpy as np
from typing import List


def is_majority(items: list[bool]) -> bool:
    counter = 0
    for i in items:
        if i == True:
            counter += 1
    print(counter)
    cond_two = counter != 0
    return cond_two and counter > len(items)/2


print("Example:")
print(is_majority([True, True, False, True, False]))
################################################### OR########################################################


def is_majority(items: list) -> bool:
    return sum(items) > len(items) / 2
################################################### OR########################################################


def is_majority(items: list) -> bool:
    return sum(items) > len(items) / 2

################################################### OR########################################################


def is_majority(items: List[bool]) -> bool:
    return sum(items) > len(items)//2

################################################### OR########################################################


def is_majority(items: list) -> bool:
    return True if np.sum(np.array(items)) > len(items)/2 else False
