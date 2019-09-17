""""""
"""
For n = 37 and k = 3, the output should be
killKthBit(n, k) = 33.

37_10 = 100101_2 ~> 100001_2 = 33_10.

For n = 37 and k = 4, the output should be
killKthBit(n, k) = 37.

The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.
"""

def killKthBit(n, k):
    return n & ~(1 << (k - 1))


print(killKthBit(37, 3))
