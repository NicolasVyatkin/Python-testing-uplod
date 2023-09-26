# Backward String
# You should return a given string in reverse order.

# example

# Input: A string (str).

# Output: A string (str).

# Examples:

# assert backward_string("val") == "lav"
# assert backward_string("") == ""
# assert backward_string("ohho") == "ohho"
# assert backward_string("123456789") == "987654321"

######################SOLUTION######################
def backward_string(val: str) -> str:
    n = val[::-1]
    return n
#########################OR#########################
backward_string = lambda val: val[::-1]
#########################OR#########################
from operator import itemgetter
backward_string = itemgetter(slice(None, None, -1))
#########################OR#########################
def backward_string(val: str) -> str:
    return val[::-1]