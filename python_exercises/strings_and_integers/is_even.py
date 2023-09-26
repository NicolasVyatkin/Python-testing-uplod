# Is Even
# Check if the given number is even or not. Your function should return True if the number is even, 
# and False if the number is odd.

# Input: An integer (int).

# Output: Logic value (bool).

# Examples:

# assert is_even(2) == True
# assert is_even(5) == False
# assert is_even(0) == True

#####################SOLUTION#####################
def is_even(num: int) -> bool:
    is_number_even = False
    if num % 2 == 0:
        is_number_even = True
    return is_number_even


print("Example:")
print(is_even(2))
########################OR########################
def is_even(num: int) -> bool:
    return num & 1 == 0
########################OR########################
def is_even(num: int) -> bool:
    return bin(num)[-1]=='0'
########################OR########################
def is_even(num: int) -> bool:    
    return not(num & 1)