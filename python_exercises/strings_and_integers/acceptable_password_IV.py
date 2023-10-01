# Acceptable Password IV
# In this mission you need to create a password verification function.

# The verification conditions are:

# the length should be bigger than 6;
# should contain at least one digit, but it cannot consist of just digits;
# if the password is longer than 9 - previous rule is not required.
# Input: A string (str).

# Output: A logic value (bool).

# Examples:

# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

# How it's used: For password verification form. Also it's good to learn how the task can be evaluated.

################################################ SOLUTION#####################################################
def is_acceptable_password(password: str) -> bool:
    cond_one = len(password) >= 6
    cond_two = any(map(str.isdigit, password)) and not password.isdigit()
    cond_three = len(password) >= 9
    return cond_one and (cond_two or cond_three)


print("Example:")
print(is_acceptable_password("short"))
################################################### OR########################################################


def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6 and not password.isdigit() and not password.isalpha()) or len(password) > 9

################################################### OR########################################################


def is_acceptable_password(p): return 0 < sum(c.isdigit()
                                              for c in p) < len(p) > 6 or len(p) > 9
################################################### OR########################################################


def is_acceptable_password(password: str) -> bool:
    return len(password) > 9 or (len(password) > 6
                                 and any(ch.isdigit() for ch in password)
                                 and not password.isdigit())
