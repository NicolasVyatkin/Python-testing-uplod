# Digits Multiplication

# You are given a positive number. Your function should calculate the product of the digits excluding any zeroes.

# For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

# Input: A positive integer (int).

# Output: The product of the digits as an integer (int).

# Examples:

# assert checkio(123405) == 120
# assert checkio(999) == 729
# assert checkio(1000) == 1
# assert checkio(1111) == 1
# 1
# 2
# 3
# 4
# How it is used: This task can teach you how to solve a problem with simple data type conversion.

# Precondition:
# 0 < number < 106

################################################ SOLUTION#####################################################
from numpy import prod


def checkio(number: int) -> int:
    numbers = str(number).replace('0', '')
    mult = 1
    for num in numbers:
        mult *= int(num)
    return mult


print("Example:")
print(checkio(123405))
################################################### OR########################################################


def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res

################################################### OR########################################################


def checkio(n): return eval("*".join(i for i in str(n) if i != '0'))

################################################### OR########################################################


def checkio(number): return int(
    prod([int(i) for i in list(str(number)) if i != '0']))
