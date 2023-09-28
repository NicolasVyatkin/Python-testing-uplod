# Acceptable Password V
# In this mission you need to create a password verification function.

# The verification conditions are:

# the length should be bigger than 6;
# should contain at least one digit, but it cannot consist of just digits;
# having numbers or containing just numbers does not apply to the password longer than 9;
# a string should not contain the word "password" in any case.
# Input: A string (str).

# Output: A logic value (bool).

# Examples:

# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

# How it�s used: For password verification form. Also it's good to learn how the task can be evaluated.

################################################ SOLUTION#####################################################
from re import search


def is_acceptable_password(password: str) -> bool:
    cond_one = len(password) >= 6
    cond_two = any(map(str.isdigit, password)) and not password.isdigit()
    cond_three = len(password) >= 9
    cond_four = 'password' not in password and 'PASSWORD' not in password
    return cond_one and (cond_two or cond_three) and cond_four


print("Example:")
print(is_acceptable_password("short"))
################################################### OR########################################################


def is_acceptable_password(password):
    cd = 0
    cnd = 0
    if 'password' in password.lower():
        return False
    for i in password:
        if i.isdigit():
            cd += 1
        else:
            cnd += 1
        if cd > 0 and cnd > 0:
            break
    if len(password) < 9:
        return True if len(password) > 6 and cd > 0 and cnd > 0 else False
    else:
        return True
    return None

################################################### OR########################################################


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        for x in password:
            if x.isdigit():
                return True
        return False
    else:
        return False
################################################### OR########################################################


def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6 and any(char.isdigit() for char in password) and not password.isnumeric())
################################################### OR########################################################


def is_acceptable_password(password: str) -> bool:
    return (len(password) > 9 or (len(password) > 6 and any(char.isdigit() for char in password) and not password.isnumeric()))

################################################### OR########################################################


def is_acceptable_password(a):
    return \
        not search(r"password", a.lower())\
        and\
        (len(a) > 9 or
         (
            len(a) > 6
            and
            any(char.isdigit() for char in a)
            and
            not a.isnumeric()
        )
        )
