
# Conversion into CamelCase
# Your mission is to convert the name of a function from the Python format (for example "my_function_name")
# into CamelCase ("MyFunctionName") where the first char of every word is in uppercase and all words are
# concatenated without any intervening characters.

# Input: A function name as a string (str).

# Output: The same string (str), but in CamelCase.

# Examples:

# assert to_camel_case("my_function_name") == "MyFunctionName"
# assert to_camel_case("i_phone") == "IPhone"
# 1
# 2
# How it is used: To apply function names in the style in which they are adopted in a specific
# language (Python, JavaScript, etc.).

# Precondition:
# 0 < len(string) <= 100
# Input data won't contain any numbers.

################################################ SOLUTION#####################################################
def to_camel_case(name: str) -> str:
    name = name.split('_')
    cammel_name = ''
    for i in name:
        cammel_name += i.capitalize()

    return cammel_name


print("Example:")
print(to_camel_case("my_function_name"))
################################################### OR########################################################


def to_camel_case(name):
    return name.title().replace('_', '')

################################################### OR########################################################


def to_camel_case(n): return __import__("re").sub(
    '\_\w', lambda m: m.group(0)[1].upper(), n.title())
################################################### OR########################################################


def to_camel_case(name):
    return name.title().replace('_', '')
