# Integer Sign Determination  - add new solutions later

# Identify whether a given integer is positive, negative, or zero and return a respective string: "positive", "negative" or "zero".

# example

# Input: Integer (int).

# Output: String (str).

# Examples:

# assert determine_sign(5) == "positive"
# assert determine_sign(0) == "zero"
# assert determine_sign(-10) == "negative"
# assert determine_sign(1) == "positive"

# How it’s used: understanding the sign of a number can be useful in financial software, scientific simulations, and many algorithms to determine subsequent logic.

# Precondition:

# num ∈ Z.

################################################ SOLUTION#####################################################

def determine_sign(num: int) -> str:
    result = ''
    if num > 0:
        result = 'positive'
    elif num < 0:
        result = 'negative'
    else:
        result = 'zero'
    return result


print("Example:")
print(determine_sign(11))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
