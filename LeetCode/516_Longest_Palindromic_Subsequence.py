"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""
"""
6.7. A subsequence is palindromic if it is the same whether read left to right or right
to left. For instance, the sequence
A, C, G, T, G, T, C, A, A, A, A, T, C, G
has many palindromic subsequences, including A, C, G, C, A and A, A, A, A (on
the other hand, the subsequence A, C, T is not palindromic). Devise an
algorithm that takes a sequence x[1 ... n] and returns the (length of the) longest
palindromic subsequence. Its running time should be O(n2).
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        LPSSeq = [[0 for r in range(n)] for c in range(n)]

        for r in range(n):
            LPSSeq[r][r] = 1  

            for c1 in range(2, n+1):
                for i in range(n - c1 + 1):
                    j = i + c1 - 1
                    if s[i] == s[j] and c1 == 2:  # A subsequence like aa
                        LPSSeq[i][j] = 2 
                    elif s[i] == s[j]:
                        LPSSeq[i][j] = 2 + LPSSeq[i+1][j-1]
                    else:
                        LPSSeq[i][j] = max(LPSSeq[i][j-1], LPSSeq[i+1][j]);
                    
        print(LPSSeq)
        return LPSSeq[0][n-1]



s1 = Solution()


s = "bbbab"
print(s, '-->', s1.longestPalindromeSubseq(s))


s = "cbbd"
print(s, '-->', s1.longestPalindromeSubseq(s))


