# Index Power

# You are given a list with positive integers (int) and an integer (int) N. You should find the N-th
# power of the element in the list with the index N. If N is outside of the list, then return -1.
# Don't forget that the first element has the index 0.

# Let's look at a few examples:
# - list = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
# - list = [1, 2, 3] and N = 3, but N is outside of the list, so the result is -1.

# Input: Two arguments.A list of integers (int) and an integer (int).

# Output: The result as an integer (int).

# Examples:

# assert index_power([1, 2, 3, 4], 2) == 9
# assert index_power([1, 3, 10, 100], 3) == 1000000
# assert index_power([0, 1], 0) == 1
# assert index_power([1, 2], 3) == -1

# How it is used: This mission teaches you how to use basic arrays and indexes when combined with
# simple mathematics.

# Precondition: 0 < len(array) ≤ 10
# 0 ≤ N
# all(0 ≤ x ≤ 100 for x in array)

################################################ SOLUTION#####################################################
def index_power(ar: list[int], n: int) -> int:
    return ar[n]**n if len(ar) > n else -1


print("Example:")
print(index_power([1, 2, 3], 2))
################################################### OR########################################################


def index_power(array, n):
    try:
        return array[n] ** n
    except IndexError:
        return -1

################################################### OR########################################################


def index_power(a, n): return -(len(a) <= n) or a[n]**n
################################################### OR########################################################


def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    return array[n]**n if len(array) > n else -1
