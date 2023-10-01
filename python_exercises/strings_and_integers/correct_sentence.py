# Correct Sentence
# For the input of your function, you will be given one sentence. You have to return a corrected version,
# that starts with a capital letter and ends with a period (dot).

# Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a
# period (dot), then adding another one will be a mistake.

# Input: A string (str).

# Output: A string (str).

# Examples:

# assert correct_sentence("greetings, friends") == "Greetings, friends."
# assert correct_sentence("Greetings, friends") == "Greetings, friends."
# assert correct_sentence("Greetings, friends.") == "Greetings, friends."
# assert correct_sentence("greetings, friends.") == "Greetings, friends."

# Precondition: No leading and trailing spaces, text contains only spaces, a-z, A-Z, "," and ".".

################################################ SOLUTION#####################################################
from string import ascii_uppercase
import numpy as np


def correct_sentence(text: str) -> str:
    text = text[0].upper()+text[1:]
    if not text.endswith('.'):
        text += '.'
    return text


print("Example:")
print(correct_sentence("greetings, friends"))
################################################### OR########################################################


def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

################################################### OR########################################################


def correct_sentence(t): return t[0].upper() + t[1:] + '.'*(t[-1] != '.')
################################################### OR########################################################


def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

################################################### OR########################################################


def correct_sentence(text: str) -> str:
    text = np.array(list(text), dtype=str)
    dot_at_the_end = text[-1] in '.'
    capital_at_start = text[0] in ascii_uppercase
    if not capital_at_start:
        text[0] = str(text[0]).upper()
    if not dot_at_the_end:
        text = np.append(text, '.')
    return "".join(text)
