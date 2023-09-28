# Max Digit
# You have a number and you need to determine which digit in this number is the biggest.

# Input: A positive integer (int).

# Output: An integer 0-9 (int).

# Examples:

# assert max_digit(0) == 0
# assert max_digit(52) == 5
# assert max_digit(634) == 6
# assert max_digit(1) == 1

################################################ SOLUTION#####################################################
from math import floor, log10


def max_digit(value: int) -> int:
    max_num = 0
    for i in str(value):
        if int(i) > int(max_num):
            max_num = i

    return int(max_num)


print("Example:")
print(max_digit(10))

################################################### OR########################################################


def max_digit(number): return int(max(str(number)))
################################################### OR########################################################


def max_digit(number: int) -> int:
    for i in range(10)[::-1]:
        if str(i) in str(number):
            return i
    return 0
################################################### OR########################################################


def max_digit(number: int) -> int:
    return max(map(int, str(number)))
