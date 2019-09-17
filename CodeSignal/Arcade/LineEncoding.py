"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating
character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".
"""


def lineEncoding(s):
    st = ''
    count = 1
    c = s[0]
    for i in range(1, len(s)):
        if s[i] == c:
            count += 1
        else:
            if count > 1:
                st += str(count)
            st += c
            c = s[i]
            count = 1
    if count > 1:
        st += str(count)
    st += c
    return st



s = "aabbbcc"
# s = "abccc"
print(lineEncoding(s))

import re
encodedString = re.sub(r'(.)(\1+)', lambda char: str(len(char.group())) + char.group(1),s)
