""""""
"""
Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation 
(it is guaranteed that such a bit exists), counting from right to left.
Return the value of 2position_of_the_found_bit.

Example
For n = 37, the output should be
secondRightmostZeroBit(n) = 8.

37_10 = 100101_2. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.
Thus, the answer is 2^3 = 8
"""

def secondRightmostZeroBit(n):
    print(str(bin(n)))
    print("{0:b}".format(n))
    print('index is', str(bin(n))[2:].find('1', str(bin(n))[2:].find('1') + 1))
    # return 2**int(str(bin(n))[2:].find('1', str(bin(n))[2:].find('1') + 1))
    return ~(n|n+1) & -~(n|n+1)


# print(secondRightmostZeroBit(37))
n = int(1073741824)
print(secondRightmostZeroBit(n))


