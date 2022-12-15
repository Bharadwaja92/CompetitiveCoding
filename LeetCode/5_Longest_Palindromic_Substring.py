"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        sub = ''
        sub_len = 0
        for i in range(len(s)):            
            # For each character, spread outward and inward
            # Odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                new_len = r - l + 1
                if new_len > sub_len:
                    sub_len = new_len
                    sub = s[l:r+1]
                l -= 1
                r += 1

            # Even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                new_len = r - l + 1
                if new_len > sub_len:
                    sub_len = new_len
                    sub = s[l:r+1]
                l -= 1
                r += 1


        return sub


s1 = Solution()

s = "babad"
print(s, '-->', s1.longestPalindrome(s))


s = "abbc"
print(s, '-->', s1.longestPalindrome(s))

s = "abbac"
print(s, '-->', s1.longestPalindrome(s))
