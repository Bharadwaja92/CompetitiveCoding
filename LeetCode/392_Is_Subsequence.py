"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


from operator import le


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i2 = 0
        i = 0
        while i2 < len(s) and i < len(t):
            c = t[i]
            if c == s[i2]:
                i2 += 1
            # print(c, i, i2)
            i += 1
        return i2 == len(s)


s1 = Solution()


s = "abc"
t = "ahbgdc"
print(s, '-->', t, '-->', s1.isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(s, '-->', t, '-->', s1.isSubsequence(s, t))

s = "acaca"
t = "aaaaaaaaaaaa"
print(s, '-->', t, '-->', s1.isSubsequence(s, t))

