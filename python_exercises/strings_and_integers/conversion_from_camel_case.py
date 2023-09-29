# Conversion from CamelCase
# Your mission is to convert the name of a function from CamelCase ("MyFunctionName") into the Python
# format ("my_function_name") where all chars are in lowercase and all words are concatenated with an
# intervening underscore symbol "_".

# Input: A function name as a CamelCase string (str).

# Output: The same string (str), but in under_score.

# Examples:

# assert from_camel_case("MyFunctionName") == "my_function_name"
# assert from_camel_case("IPhone") == "i_phone"
# 1
# 2
# How it is used: To apply function names in the style in which they are adopted in a specific
# language (Python, JavaScript, etc.).

# Precondition:
# 0 < len(string) <= 100
# Input data won't contain any numbers.

################################################ SOLUTION#####################################################
import re


def from_camel_case(name: str) -> str:
    puthon_format = ''
    for sumb in reversed(name):
        if sumb.isupper():
            puthon_format += sumb.lower() + "_"
        else:
            puthon_format += sumb
    puthon_format = puthon_format[-2::-1]
    return puthon_format


print("Example:")
print(from_camel_case("MyFunctionName"))
################################################### OR########################################################


def from_CamelCase(name):
    return '_'.join(re.findall('([A-Z][^A-Z]*)', name)).lower()

################################################### OR########################################################


def from_camel_case(t): return re.sub("([A-Z])", r"_\1", t).lower().lstrip('_')
################################################### OR########################################################


def from_camel_case(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
