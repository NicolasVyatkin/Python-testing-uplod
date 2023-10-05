# Leap Year Checking  - add more solutions

# Check if the given year is leap year. A year is a leap year if it is divisible by 4, except for end-of-century
# years which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

# Input: Integer (int).

# Output: Logic value (bool).

# Examples:

# assert is_leap_year(2000) == True
# assert is_leap_year(1900) == False
# assert is_leap_year(2004) == True
# assert is_leap_year(2100) == False

# How it’s used: this function can be used in calendars, scheduling applications, or any system which deals with
# yearly data.

# Precondition:

# 1 <= year <= 10**5

################################################ SOLUTION#####################################################

def is_leap_year(year: int) -> bool:
    if (year % 400 == 0) and (year % 100 == 0):
        # print("{0} is a leap year".format(year))
        return True

# not divided by 100 means not a century year
# year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        # print("{0} is a leap year".format(year))
        return True

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
    else:
        # print("{0} is not a leap year".format(year))
        return False


print("Example:")
print(is_leap_year(2000))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
