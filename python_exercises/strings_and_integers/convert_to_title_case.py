# Convert To Title Case - edit later

# Your function should take a string as an input and convert all the first letters of the words in the string to
# uppercase, making the string a title case (other letters must be in lowercase).

# example

# Input: Original string (str).

# Output: Converted string (str).

# Examples:

# assert to_title_case("hello world") == "Hello World"
# assert to_title_case("openai gpt-4") == "Openai Gpt-4"
# assert to_title_case("this is a title") == "This Is A Title"
# assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"

# How it’s used:

# for text processing and data normalization tasks;
# for rendering text in UI in a standard title case format.
# Preconditions:

# sentence ∈ string;
# length(sentence) >= 0.

################################################ SOLUTION#####################################################

def to_title_case(sentence: str) -> str:
    return sentence.lower().title()


print("Example:")
print(to_title_case("JUMPs ovER a LAZy dog"))

################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
