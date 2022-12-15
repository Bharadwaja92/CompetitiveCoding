"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        # Div by 5
        while n % 5 == 0:
            n //= 5
        print('After 5, n =', n)
        # Div by 3
        while n % 3 == 0:
            n //= 3
        print('After 5, 3 =', n)
        # Div by 2
        while n % 2 == 0:
            n //= 2
        print('After 2, n =', n)
        print('n  =', n)
        return n == 1


s = Solution()

n = 17
print(n, s.isUgly(n))

n = 1400
print(n, s.isUgly(n))

n = 1500
print(n, s.isUgly(n))