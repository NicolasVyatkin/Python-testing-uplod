# Between Markers (simplified)

# You are given a string and two markers (the initial one and final). You have to find a substring enclosed
# between these two markers. But there are a few important conditions.

# The initial and final markers are always different.
# The initial and final markers are always 1 char size.
# The initial and final markers always exist in a string and go one after another.
# example

# Input: Three arguments. All of them are strings (str). The second and third arguments are the initial
# and final markers.

# Output: A string (str).

# Examples:

# assert between_markers("What is >apple<", ">", "<") == "apple"
# assert between_markers("What is [apple]", "[", "]") == "apple"
# assert between_markers("What is ><", ">", "<") == ""
# assert between_markers("[an apple]", "[", "]") == "an apple"

# How it is used: For text parsing.

# Precondition: There can't be more than one final and one initial markers.

################################################ SOLUTION#####################################################
def between_markers(text: str, start: str, end: str) -> str:
    if text.find(start) == -1 and text.find(end) == -1:
        final = text
    elif text.find(start) == -1:
        final = text[:text.find(end)]
    elif text.find(end) == -1:
        final = text[text.find(start)+len(start):]
    elif text.find(start) > text.find(end):
        final = ''
    else:
        final = text[text.find(start)+len(start):text.find(end)]

    return final


print("Example:")
print(between_markers("What is >apple<", ">", "<"))
################################################### OR########################################################


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    return text[text.index(begin)+1:text.index(end)]

################################################### OR########################################################


def between_markers(t, b, e, f=lambda x, y): return x.find(y): t[f(t, b)+1:f(t, e)]
################################################### OR########################################################


def between_markers(text, begin, end):
    i = text.find(begin) + 1
    j = text.find(end, i)
    return text[i:j]

################################################### OR########################################################


def between_markers(text, start, end): return text[text.find(
    start) + len(start):text.rfind(end)]
