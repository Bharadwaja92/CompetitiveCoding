"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

class Solution:
    def countBits(self, n: int) -> list[int]:
        bits = [0 for _ in range(n+1)]
        curr_base = 1

        for i in range(1, n+1):
            if curr_base * 2 == i:
                curr_base = i
            bits[i] = 1 + bits[i - curr_base]

        return bits


s = Solution()


n = 2
print(n, '-->', s.countBits(n))


n = 5
print(n, '-->', s.countBits(n))


n = 10
print(n, '-->', s.countBits(n))
