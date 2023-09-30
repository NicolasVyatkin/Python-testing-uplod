# Rectangle Perimeter - edit later

# This function should take two positive numbers (length and width) as inputs and return the perimeter of a rectangle.

# example

# Input: Two integers (int).

# Output: Integer (int).

# Examples:

# assert rectangle_perimeter(2, 4) == 12
# assert rectangle_perimeter(3, 5) == 16
# assert rectangle_perimeter(10, 20) == 60
# assert rectangle_perimeter(7, 2) == 18

# How it’s used:

# in architectural and engineering applications for calculating the perimeter of buildings or rooms;
# in computer graphics to calculate the perimeter of a rectangle on a screen.
# Preconditions:

# length, width ∈ R;
# length, width > 0.

################################################ SOLUTION#####################################################

# def rectangle_perimeter(length: int, width: int) -> int:

#     return int(width * 2 + length * 2) if length > 0 and width > 0 else 0


################################################### OR########################################################

def rectangle_perimeter(length: int, width: int) -> int:
    if width > 0 and length > 0:
        result = width + width + length + length
    return result


print("Example:")
print(rectangle_perimeter(2, 4))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
