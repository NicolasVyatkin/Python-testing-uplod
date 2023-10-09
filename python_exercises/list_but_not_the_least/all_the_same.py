# All the Same

# In this mission you should check if all elements in the given sequence are equal.

# Input: List.

# Output: Logic value (bool).

# Examples:

# assert all_the_same([1, 1, 1]) == True
# assert all_the_same([1, 2, 1]) == False
# assert all_the_same([1, "a", 1]) == False
# assert all_the_same([1, 1, 1, 2]) == False

# The idea for this mission was found on Python Tricks series by Dan Bader

# Precondition: all elements of the input list are hashable

################################################ SOLUTION#####################################################
from numpy import unique
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


print("Example:")
print(all_the_same([1, 1, 1]))
################################################### OR########################################################


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1

################################################### OR########################################################


def all_the_same(e): return e[1:] == e[:-1]
################################################### OR########################################################


def all_the_same(elements: List[Any]) -> bool:
    return all(elements[i] == elements[i+1] for i in range(len(elements)-1))

################################################### OR########################################################


def all_the_same(elements: List[Any]) -> bool:
    return len(unique(elements)) <= 1
