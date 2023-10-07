# Quadratic Equation Roots  - add new solutions later

# A quadratic equation is represented as ax2 + bx + c = 0. The general formula to find its
# roots (x-values for which y = 0) is:


# This formula provides two roots: x1, x2. The value inside the square root, b2-4ac is known as the discriminant (D). Based on the value of the discriminant, a quadratic equation can have:

# two distinct real roots (D > 0);
# one real root (D = 0);
# no real roots (D < 0).
# Your code must return Iterable containing two values: the roots x1, x2, sorted descending.
# If there's only one real root, both values will be the same. If there are no real roots, the
# Iterable should contain the string "No real roots".

# Input: Three integers (int).

# Output: Tuple or other Iterable of two integers (int) or string (str).

# Examples:

# assert list(quadratic_roots(1, -3, 2)) == [2, 1]
# assert list(quadratic_roots(1, 0, -1)) == [1, -1]
# assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
# assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]

# How it’s used: this function can be useful in mathematical computations, physics simulations,
# optimization problems, or anywhere quadratic equations are utilized.

# Preconditions:

# a != 0;
# -10**9 <= a, b, c <= 10**9.

################################################ SOLUTION#####################################################
from collections.abc import Iterable
import math


def quadratic_roots(a: int, b: int, c: int) -> Iterable[int | str]:

    d = b**2-4*a*c  # discriminant
    # print(d)
    try:
        if d < 0:
            print("No real roots")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            # print("This equation has one solutions: "), x
            return [int(x)]
        else:
            x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
            x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
            # print("This equation has two solutions: "), x1, " and", x2
            return [int(x1), int(x2)]
    except TypeError:
        return ['No real roots']


print("Example:")
print(list(quadratic_roots(1, 0, 1)))

################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
