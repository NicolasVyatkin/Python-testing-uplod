# Multiply (Intro)
# This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. 
# If you want to know how to get the maximum out of using CheckiO, check out our blog post "From Basic 
# to Advance usage".

# This mission is the easiest one. Write a function that will receive 2 numbers as input and it should 
# return the multiplication of these 2 numbers.

# Input: Two arguments. Both are of type int.

# Output: Int.

# Examples:

# assert mult_two(3, 2) == 6
# assert mult_two(0, 1) == 0

####################SOLUTION####################

def mult_two(a: int, b: int) -> int:
    c = a * b
    return c

print("Example")
print(mult_two(1, 2))

#######################OR#######################
mult_two = int.__mul__
#######################OR#######################
from operator import mul as mult_two
#######################OR#######################
import numpy as np

def mult_two(a, b):
    return np.product([a, b])

if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))