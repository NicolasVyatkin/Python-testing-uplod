# Goes Right After
# In a given word you need to check if one symbol goes only right after another.

# Cases you should expect while solving this challenge:

# one of the symbols is not in the given word - your function should return False;
# any symbol appears in a word more than once - use only the first one;
# two symbols are the same - your function should return False;
# the condition is case sensitive, which means 'a' and 'A' are two different symbols.
# example

# Input: Three arguments. The first one is a given string (str), second is a symbol (str)
# that should go first, and the third is a symbol (str) that should go after the first one.

# Output: A logic value (bool).

# Examples:

# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("panorama", "a", "n") == True

################################################ SOLUTION#####################################################
def goes_after(word: str, first: str, second: str) -> bool:
    cond_one = word.find(second) - 1 == word.find(first)
    cond_two = first in word and second in word
    return cond_one and cond_two


print("Example:")
print(goes_after("world", "w", "o"))
################################################### OR########################################################


def goes_after(w, f, s): return w.index(f) == w.index(s) - \
    1 if f in w and s in w else False
################################################### OR########################################################


def goes_after(word: str, first: str, second: str) -> bool:
    i = word.find(first)
    return i >= 0 and word.find(second) == i+1
