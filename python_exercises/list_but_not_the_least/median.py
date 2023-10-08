# Median

# A median is a numerical value separating the upper half of a sorted list of numbers from the lower
# half. In list where there are an odd number of entities, the median is the number found in the middle
# of the list. If the list contains an even number of entities, then there is no single middle value,
# instead the median becomes the average of the two numbers found in the middle. For this mission,
# you are given a non-empty list of integers (int). With it, you must separate the upper half of the
# numbers from the lower half and find the median.

# example

# If you want to practice more with the similar case, try Middle Characters mission.

# Input: List with integers (int).

# Output: The median as an integer or float (int | float).

# Examples:

# assert checkio([1, 2, 3, 4, 5]) == 3
# assert checkio([3, 1, 2, 5, 3]) == 3
# assert checkio([1, 300, 2, 200, 1]) == 2
# assert checkio([3, 6, 20, 99, 10, 15]) == 12.5

# How it is used: The median has usage for Statistics and Probability theory, it has especially
# significant value for skewed distribution. For example: we want to know average wealth of people
# from a set of data - 100 people earn $100 in month and 10 people earn $1,000,000. If we average it out,
# we get $91,000. This is weird value and does nothing to show us the real picture. In this case the median
# would give to us more useful value and a better picture. The Article at Wikipedia.

# Preconditions:

# 1 < len(data) ≤ 1000
# all(0 ≤ x < 10 ** 6 for x in data)

################################################ SOLUTION#####################################################
import statistics


def checkio(data):
    return statistics.median(data)
################################################### OR########################################################


def checkio(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

################################################### OR########################################################


def checkio(d): return (lambda t, n: t[n]+t[-n-1])(sorted(d), len(d)//2)/2
################################################### OR########################################################


def select(a, d, n, k):
    if n <= 5:
        return sorted(a[d:d+n])[k]

    # Find median of medians of 5
    medians = [sorted(a[i:i+5])[2] for i in range(d, d+n-4, 5)]
    m = len(medians)
    median = select(medians, 0, m, m // 2)

    # Partition around the median.
    # a[d:i]     <= median
    # a[j+1:d+n] >= median
    i, j = d, d+n-1
    while i <= j:
        while a[i] < median:
            i += 1
        while a[j] > median:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if d+k < i:
        return select(a, d, i-d, k)
    else:
        return select(a, i, n+d-i, k+d-i)


def checkio(data):
    n = len(data)
    if n % 2 == 1:
        return select(data, 0, n, n//2)
    else:
        return 0.5 * (select(data, 0, n, n//2-1) + select(data, 0, n, n//2))

# These "asserts" using only for self-checking and not necessary for auto-testing
################################################### OR########################################################
