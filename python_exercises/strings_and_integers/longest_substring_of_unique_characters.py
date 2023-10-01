# Longest Substring of Unique Characters - add new solutions later

# Given a string, find the length of the longest substring without repeating characters.

# example

# Input: String (str).

# Output: Integer (int).

# Examples:

# assert longest_substr("abcabcbb") == 3
# assert longest_substr("bbbbb") == 1
# assert longest_substr("pwwkew") == 3
# assert longest_substr("abcdef") == 6

# How it’s used:

# data validation for passwords to ensure the inclusion of a sufficiently long sequence of non-repeated characters;
# text analysis, especially for cryptography and coding patterns;
# identifying unique patterns in a sequence.

################################################ SOLUTION#####################################################

def longest_substr(s: str) -> int:
    n = len(s)
    # Result
    res = 0
    for i in range(n):
        # Note : Default values in
        # visited are false
        visited = [0] * 256
        for j in range(i, n):
            # If current character is visited
            # Break the loop
            if (visited[ord(s[j])] == True):
                break
            # Else update the result if
            # this window is larger, and mark
            # current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(s[j])] = True
        # Remove the first character of previous
        # window
        visited[ord(s[i])] = False
    return res


print("Example:")
print(longest_substr("abcabcbb"))
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
################################################### OR########################################################
