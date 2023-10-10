# YAML. Simple Dict

# Have you ever heard of such markup language as YAML? It’s a friendly data serialization format. In fact it’s
# so friendly that both people and programs can read it quite well. You can play around with the standard by
# following this link.

# YAML is a text, and you need to convert it into an object. But I’m not asking you to implement the entire YAML
# standard, we’ll implement it step by step.

# The first step is the key-value conversion. The key can be any string consisting of Latin letters and numbers.
# The value can be a single-line string (which consists of spaces, Latin letters and numbers) or a number (int).

# I’ll show some examples:

# name: Alex
# age: 12
# Converted into a dictionary.

# {
#   "name": "Alex",
#   "age": 12
# }


# Note that the number automatically gets type int.

# Another example shows that the string may contain spaces.

# name: Alex Fox
# age: 12

# class: 12b
# Will be converted into the next dictionary.

# {
#   "age": 12,
#   "name": "Alex Fox",
#   "class": "12b"
# }

# Pay attention to a few things. Between the string "age" and the string "class" there is an empty string
# that doesn’t interfere with parsing. The class starts with numbers, but has letters, which means it cannot
# be converted to numbers, so its type remains a str.

# Input: A format string.

# Output: An object (dictionary).

# Examples:

# assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
# assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
#     "age": 12,
#     "name": "Alex Fox",
#     "class": "12b",
# }

# Precondition: YAML 1.2 is being used with JSON Schema.

################################################ SOLUTION#####################################################
from operator import methodcaller
from typing import Dict


def yaml(a: str) -> dict:
    b = dict([l.split(": ") for l in sorted(a.splitlines()) if l])
    for k, v in b.items():
        if v.isnumeric():
            b[k] = int(v)
    return b


print("Example:")
print(
    yaml(
        """name: Alex
age: 12"""
    )
)
################################################### OR########################################################


def yaml(a):
    t = [i.strip() for i in a.split('\n') if i]
    d = {}
    for elem in t:
        key, val = (i.strip() for i in elem.split(':'))
        d[key] = int(val) if val.isdecimal() else val
    return d

################################################### OR########################################################


def yaml(a):
    res = {}
    for key, value in map(methodcaller('split', ': '), filter(None, a.splitlines())):
        res[key] = int(value) if value.isnumeric() else value
    return res

################################################### OR########################################################


def yaml(a: str) -> Dict:
    d = {}
    for line in a.splitlines():
        if line:
            key, value = line.split(': ')
            d[key] = int(value) if value.isdigit() else value
    return d
################################################### OR########################################################
