# Armstrong Number Checking - add more solutions

# In number theory, an Armstrong number (after Michael F. Armstrong) or narcissistic number in a given number
# base (10 for this mission) is a number that is the sum of its own digits each raised to the power of the number
# of digits. For example, 153 is an Armstrong number because 13 + 53 + 33 == 153.

# Input: Integer (int).

# Output: Logic value (bool).

# Examples:

# assert is_armstrong(153) == True
# assert is_armstrong(370) == True
# assert is_armstrong(947) == False
# assert is_armstrong(371) == True

# How it’s used: this function can be employed in mathematical puzzles, encryption algorithms, and educational tools.

################################################ SOLUTION#####################################################

def is_armstrong(num: int) -> bool:
    result = []
    for i in list(str(num)):
        result.append(int(i).__pow__(len(str(num))))
    return sum(result) == num


print("Example:")
print(is_armstrong(153))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
