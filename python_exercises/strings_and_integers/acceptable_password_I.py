# Acceptable Password I
# You are at the beginning of a password series. Every mission is based on the previous one. 
# The missions that follow will become slightly more complex.

# In this mission, you need to create a password verification function.

# The verification condition is:

# the length should be bigger than 6.
# Input: A string (str).

# Output: A logic value (bool).

# Examples:

# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

#####################SOLUTION#####################
def is_acceptable_password(password: str) -> bool:
    some = True   
    if len(password)<=6:
        some = False
    return some


print("Example:")
print(is_acceptable_password("short"))
########################OR########################
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6
########################OR########################
def is_acceptable_password(password: str) -> bool:
    return bool(password[7::])