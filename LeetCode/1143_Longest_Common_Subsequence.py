"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1)+1, len(text2)+1            
        LCS = [[0]* l2]*l1    # THIS IS WRONG
        LCS = [[0 for j in range(l2)]  for i in range(l1)] 
        text1 = '@' + text1
        text2 = '!' + text2
        for i in range(1, l1):
            for j in range(1, l2):
                # print('i =', i, '  j =', j)
                # print('text1[i] =', text1[i], ' text2[j] =', text2[j])
                if text1[i] == text2[j]:                    
                    # print('Case 1')
                    LCS[i][j] = 1 + LCS[i-1][j-1]
                else:
                    # print('Case 2')
                    LCS[i][j] = max([LCS[i-1][j], LCS[i][j-1]])
            print(LCS)

        return LCS[l1-1][l2-1]

    


s = Solution()

# text1 = "abcde"
# text2 = "ace" 
# print(s.longestCommonSubsequence(text1, text2))

# text1 = "abc"
# text2 = "abc"
# print(s.longestCommonSubsequence(text1, text2))

# text1 = "abc"
# text2 = "def"
# print(s.longestCommonSubsequence(text1, text2))

# text1 = "ezupkr"
# text2 = "ubmrapg"
# print(s.longestCommonSubsequence(text1, text2))

text1 = "abcba"
text2 = "abcbcba"
print(s.longestCommonSubsequence(text1, text2))

# print(s.longestCommonSubsequence(text2, text1))



"""
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LCS = [[0]* (len(text2)+1)]*(len(text1)+1)
        # LCS = [[0 for j in range(len(text2)+1)]  for i in range(len(text1)+1)] 
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                # print('i =', i, 'j =', j)
                if text1[i] == text2[j]:                    
                    LCS[i][j] = 1 + LCS[i+1][j+1]
                else:
                    LCS[i][j] = max(LCS[i][j+1], LCS[i+1][j])
            print(text1[i], '-->', LCS, '\n')

        return LCS[0][0]
"""