# End Zeros
# Try to find out how many zeros a given number has at the end.

# Input: A non-negative integer (int).

# Output: An integer (int).

# Examples:

# assert end_zeros(0) == 1
# assert end_zeros(1) == 0
# assert end_zeros(10) == 1
# assert end_zeros(101) == 0

################################################ SOLUTION#####################################################
import numpy as np


def end_zeros(a: int) -> int:
    zero_couner = 0
    for num in reversed(str(a)):
        if num == '0':
            zero_couner += 1
        else:
            return zero_couner
    return zero_couner


print("Example:")
print(end_zeros(10))
################################################### OR########################################################


def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))


def end_zeros(number):
    import re
    return len(re.search('0*$', str(number)).group())


def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0
    return 1 + end_zeros(number[:-1])


def end_zeros(number):
    if not number:
        return 1
    if not number % 10:
        return 1 + end_zeros(number // 10)
    return 0


def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result


def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')


def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))
################################################### OR########################################################


def end_zeros(num: int) -> int:
    for x in str(num)[::-1]:
        if x != '0':
            return str(num)[::-1].find(x)
    return len(str(num))
################################################### OR########################################################


def end_zeros(num: int) -> int:
    if num == 0:
        return 1

    zeros = 0
    while num % 10 == 0:
        num //= 10
        zeros += 1
    return zeros

################################################### OR########################################################


def end_zeros(b):
    if b == 0:
        return 1
    for i in np.arange(1, len(str(b))+1):
        if float(b/(10**i)).is_integer() == False:
            break
    return i-1


print(end_zeros(0))
