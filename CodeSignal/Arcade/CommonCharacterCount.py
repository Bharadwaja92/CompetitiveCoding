"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

from collections import Counter
def commonCharacterCount(s1, s2):
    c1,c2 = dict(Counter(s1)), dict(Counter(s2))
    print(c1,c2)
    sum = 0
    for k in c1:
        if k in c2:
            sum += min(c1[k], c2[k])
    print(sum)

s1 = "aabcc"
s2 = "adcaa"

commonCharacterCount(s1, s2)