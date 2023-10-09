# Absolute Sorting

# Let's try some sorting. Here is sequence with the specific rules.

# The sequence has various numbers. You should sort it, but sort it by absolute value in ascending order.
# For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should
# return the sorted list or tuple.

# Input: List of integers (int).

# Output: Sorted list of integers (int).

# Addition: The results of your function will be shown as list in the tests explanation panel.

# Examples:

# assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
# assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
# assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
# 1
# 2
# 3
# How it is used: Sorting is a part of many tasks, so it will be useful to know how to use it.

# Preconditions: len(set(abs(x) for x in array)) == len(array)
# 0 < len(array) < 100
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)

################################################ SOLUTION#####################################################
from functools import partial as c


def checkio(values: list) -> list:

    return sorted(values, key=abs)


print("Example:")
print(checkio([-20, -5, 10, 15]))
################################################### OR########################################################


def checkio(numbers_array):
    """
    The magic of the key :)
    """
    return tuple(sorted(numbers_array, key=abs))


################################################### OR########################################################
checkio = c(sorted, key=abs)
################################################### OR########################################################


def checkio(numbers_array):
    b = sorted(numbers_array, key=lambda x: (abs(x)))
    return b
################################################### OR########################################################


def checkio(numbers_array):
    import numpy
    D = numpy.array(numbers_array)
    # also handles absolute value of complex numbers
    return (D[numpy.argsort(numpy.absolute(D))].tolist())
