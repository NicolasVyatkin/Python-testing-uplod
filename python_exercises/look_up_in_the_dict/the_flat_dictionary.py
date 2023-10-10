# The Flat Dictionary

# Input: An original dictionary as a dict.

# Output: The flattened dictionary as a dict.

# Examples:

# assert flatten({"key": "value"}) == {"key": "value"}
# assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
#     "key/deeper/more/enough": "value"
# }
# assert flatten({"empty": {}}) == {"empty": ""}
# assert flatten(
#     {
#         "name": {"first": "One", "last": "Drone"},
#         "job": "scout",
#         "recent": {},
#         "additional": {"place": {"zone": "1", "cell": "2"}},
#     }
# ) == {
#     "name/first": "One",
#     "name/last": "Drone",
#     "job": "scout",
#     "recent": "",
#     "additional/place/zone": "1",
#     "additional/place/cell": "2",
# }

# How it is used: This concept can be useful if you need to parse config files and simplify structures for
# grandfathered systems and file structures. You can easily modify this idea for your own specifications.
# Besides that, it's a useful skill to be able to read code and search for bugs.

# Preconditions:

# keys in a dictionary are non-empty strings;
# values in a dictionary are strings or dicts;
# root_dictionary != {}.

################################################ SOLUTION#####################################################
import ast
import pandas as pd


def flatten(dictionary: dict[str, str | dict]) -> dict[str, str]:
    flat_dict = {}
    for i, j in dictionary.items():
        if not isinstance(j, dict):
            flat_dict[i] = j
        else:
            if j == {}:
                flat_dict[i] = ''
            else:
                for i_j, j_i in flatten(j).items():
                    flat_dict[i + '/' + i_j] = j_i
    return flat_dict
################################################### OR########################################################


def flatten(D, path=[]):
    if not D:
        D = ""
    if isinstance(D, dict):
        res = {}
        for key, val in D.items():
            res.update(flatten(val, path + [key]))
        return res
    if isinstance(D, str):
        return {"/".join(path): D}
################################################### OR########################################################


def flatten(d, p=''):
    if not isinstance(d, dict) or not d:
        return [(p, d or '')]
    r = sum([flatten(v, p+'/'*bool(p)+k) for k, v in d.items()], [])
    return r if p else dict(r)
################################################### OR########################################################


def flatten(d, names=[]):
    # your code here
    temp = {}
    [temp.update({"/".join(names+[k]): v} if type(v) is str else flatten(v,
                 names+[k]) if v else {"/".join(names+[k]):""}) for k, v in d.items()]
    return temp

################################################### OR########################################################


def flatten(dictionairy):
    str1 = str(dictionairy)
    str2 = str1.replace('{}', "''")
    dd = ast.literal_eval(str2)
    df = pd.json_normalize(dd, sep='/')
    y = (df.to_dict(orient='records')[0])
    return y
