# Even the Last

# You are given list of integers (int). You should find the sum of the elements with even
# indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the list
# together. Don't forget that the first element has an index of 0.

# For an empty list, the result will always be 0 (zero).

# example

# Input: List of integers (int).

# Output: An integer (int).

# Examples:

# assert checkio([0, 1, 2, 3, 4, 5]) == 30
# assert checkio([1, 3, 5]) == 30
# assert checkio([6]) == 36
# assert checkio([]) == 0

# How it is used: Indexes and slices are important elements of coding. This will come in handy down the road!

# Preconditions: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)

################################################ SOLUTION#####################################################
def checkio(array: list[int]) -> int:
    summary = 0
    if array:  # true is non-empty
        for i, value in enumerate(array):
            if i % 2 == 0:
                summary += value
                print('sum =', summary, 'index =', i)
        res = summary * array[-1]
        return res

    return 0


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

################################################### OR########################################################


def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]

################################################### OR########################################################


def checkio(array): return sum(array[::2]) * sum(array[-1:])
################################################### OR########################################################


def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    return sum(array[0::2])*array[-1] if 0 < len(array) else 0
