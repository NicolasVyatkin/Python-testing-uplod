# Goes Right After (simplified)
# In a given string you need to check if one symbol goes right after another. If so - return True,
# otherwise - False.

# If one of the symbols is not in the given word - your function should return False. If two seeking
# symbols are the same - your function should return False.

# example

# Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should
# go first, and the third is a symbol (str) that should go after the first one.

# Output: A logic value (bool).

# Examples:

# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("list", "l", "o") == False

# Preconditions: all symbols are lowercased and unique.

################################################ SOLUTION#####################################################
def goes_after(word: str, first: str, second: str) -> bool:
    return word.find(second) - 1 == word.find(first)


print("Example:")
print(goes_after("world", "w", "o"))
################################################### OR########################################################


def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(first) - word.index(second) == -1
    except:
        return False

################################################### OR########################################################


def goes_after(word: str, f: str, s: str) -> bool:
    return f + s in word if f != s else False
################################################### OR########################################################


def goes_after(word: str, first: str, second: str) -> bool:
    return f"{first}{second}" in word
