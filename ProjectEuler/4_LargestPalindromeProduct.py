"""     https://projecteuler.net/problem=4      """
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

maxvalue = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        pr = i*j
        p = str(pr)
        if list(p) == list(reversed(p)):
            if maxvalue < pr:
                maxvalue = pr
            print(pr)

print('------------')
print(maxvalue)
