# Sort by Extension

# You are given a sequence of files as strings. You need to sort this the sequence by the file extension.
# The files with the same extension (or without one) should be sorted by name.

# Some possible cases:

# Filename cannot be an empty string;
# Sorting order: files without name, files without extension, files with name and extension;
# Filename .config or config. is all name with an empty extension;
# Filename like str1.str2.str3 has an extension str3 and a name str1.str2;
# Filename like .str1.str2 has an extension str2 and a name .str1.
# Input: List of strings (str).

# Output: List of strings (str).

# Examples:

# assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
#     "1.aa",
#     "1.bat",
#     "2.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
#     ".bat",
#     "1.aa",
#     "1.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
#     ".aa",
#     ".bat",
#     "1.bat",
#     "1.cad",
# ]

################################################ SOLUTION#####################################################
import pandas as pd
import re
from typing import List, Tuple
from typing import List


def ext(file):
    splitted_file = file.split('.')
    if ('' == splitted_file[0] and len(splitted_file) == 2):
        splitted_file = [''.join(splitted_file[1:]), '']
    return splitted_file[::-1]


def sort_by_ext(files: List[str]) -> List[str]:
    return sorted(files, key=ext)
################################################### OR########################################################


def sort_by_ext(files):
    def skey(s): return (bool(s[:(i := s.rfind('.'))]), s[i+1:], s[:i])
    return sorted(files, key=skey)

################################################### OR########################################################


def sort_by_ext(s): return sorted(
    s, key=lambda f: (f[(p := f.rfind('.')):]*(p > 0), f))
################################################### OR########################################################


def extension_and_name(filename: str) -> Tuple[str]:
    i = filename.rfind('.')
    if i <= 0:
        return ('', filename)
    return (filename[i+1:], filename[:i])


def sort_by_ext(files: List[str]) -> List[str]:
    files.sort(key=extension_and_name)
    return files

################################################### OR########################################################


def sort_by_ext(files: List[str]) -> List[str]:

    # seems to lack an additional rule: files without name go before files with name
    # this is because of the following assertion:
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']

    index_no_name = [re.search('\w+\.', f) is None for f in files]

    extensions = [re.search(r'\.[a-z]*$', f).group(0) for f in files]

    name_regex = [re.search('\w+\.', f) for f in files]

    names = []

    for n in name_regex:
        if n is not None:
            names.append(n.group(0))
        else:
            names.append('')

    files_df = pd.DataFrame(
        {'files': files, 'no_name': index_no_name, 'extension': extensions, 'name': names})

    files_df = files_df.sort_values(
        by=['no_name', 'extension', 'name'], ascending=[False, True, True])

    return list(files_df['files'])
