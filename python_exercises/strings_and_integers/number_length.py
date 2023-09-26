# Number Length
# You have a non-negative integer. Try to find out how many digits it has.

# Input: A non-negative integer (int).

# Output: An integer (int).

# Examples:

# assert number_length(10) == 2
# assert number_length(0) == 1
# assert number_length(4) == 1
# assert number_length(44) == 2

######################SOLUTION######################
def number_length(value: int) -> int:
    return len(str(value))


print("Example:")
print(number_length(10))
#########################OR#########################
import math


def number_length(a: int) -> int:
    return int(math.log10(a)) + 1 if a else 1
#########################OR#########################
from bisect import bisect
K = [0, 
    10, 
    100, 
	1000, 
	10000, 
	100000, 
	1000000,
    10000000, 
	100000000, 
	1000000000,
    10000000000]

def number_length(n):
    return bisect(K, n)
#########################OR#########################
from numpy import log10, floor

def number_length(a: int) -> int:
    if a == 0:
        return 1
    return int(floor(log10(a))+1)