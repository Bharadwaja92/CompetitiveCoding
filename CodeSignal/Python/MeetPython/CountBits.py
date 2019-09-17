""""""
"""
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its
binary representation.

Note: in this task and most of the following tasks you will be given a code snippet with some part of it replaced by
the ellipsis (...). Only this part is allowed to be changed.

Example

For n = 50, the output should be
countBits(n) = 6.

5010 = 1100102, a number that consists of 6 digits. Thus, the output should be 6.
"""

def countBits(n):
    c, x = 0, 1
    while x <= n:
        x *= 2
        c += 1
    return c+3

def countBits(n):
    return n.bit_length()


print(countBits(50))
print(countBits(0))
print(countBits(1))
print(countBits(2))
print(countBits(3))
print(countBits(4))
print(countBits(5))

