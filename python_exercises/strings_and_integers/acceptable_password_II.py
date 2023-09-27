#Acceptable Password II
# In this mission you need to create a password verification function.

# The verification conditions are:

# the length should be bigger than 6;
# should contain at least one digit.
# Input: A string (str).

# Output: A logic value (bool).

# Examples:

# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == False
# assert is_acceptable_password("ashort") == False
# assert is_acceptable_password("muchlonger5") == True
# 1
# 2
# 3
# 4
# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

####################################SOLUTION##########################################
def is_acceptable_password(password: str) -> bool:
    digit= False
    some = False
    for char in password:
        if char.isdigit():
            digit=True           

    if len(password)>=6 and digit==True:
        some = True
    return some


print("Example:")
print(is_acceptable_password("short"))
#######################################OR#############################################
def is_acceptable_password(password: str) -> bool:    
    return len(password) > 6 and any(i.isdigit() for i in password)
#######################################OR#############################################
is_acceptable_password = lambda p: len(p)>6 and any([l.isdigit() for l in p])
#######################################OR#############################################
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(ch.isdigit() for ch in password)
