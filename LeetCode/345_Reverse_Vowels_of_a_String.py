"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vs = [c for c in s if c in vowels]
        j = len(vs) - 1
        sl = list(s)
        for i in range(len(sl)):
            if sl[i] in vowels:
                sl[i] = vs[j]
                j -= 1
        return ''.join(sl)
        