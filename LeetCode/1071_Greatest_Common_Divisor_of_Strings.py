"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        min_len = min(len1, len2)

        def is_valid(k):
            if len1 % k or len2 % k: # There are some leftovers -- Remainder not zero
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == base * n1 and str2 == base * n2

        for i in range(min_len, 0, -1):
            if is_valid(i):
                return str1[:i]

        return ''


s = Solution()

str1 = "ABCABC"
str2 = "ABC"
print(str1, '->', str2, '->', s.gcdOfStrings(str1, str2))

str1 = "ABABAB"
str2 = "ABAB"
print(str1, '->', str2, '->', s.gcdOfStrings(str1, str2))

str1 = "LEET"
str2 = "CODE"
print(str1, '->', str2, '->', s.gcdOfStrings(str1, str2))

"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ''
        if len(str1) == 0 or len(str2) == 0: return gcd
        min_len = min(len(str1), len(str2))# - 1
        i = 0
        while i < min_len and str1[i] == str2[i]:            
            gcd += str1[i]
            print('gcd =', gcd)
            i += 1
        return gcd
"""