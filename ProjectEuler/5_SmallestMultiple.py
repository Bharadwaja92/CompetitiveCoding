"""     https://projecteuler.net/problem=5      """
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math

def getFactors(n):
    fs = []
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            fs.append(i)
            fs.append(n / i)
    return fs


for i in range(2, int(math.sqrt(2520))):
    if 2520 % i == 0:
        print(i, getFactors(i), getFactors(2520/i))


# print(2*3*4*5*6*7*8*9*10)
# print(6*7*8*9*10)
#
# ns = []
# for i in range(2, 11):
#     print('i is', i)
#     for j in range(2, i):
#         if i % j != 0:
#             if i/j not in ns:
#                 ns.append(i/j)
#                 print(j, end=',')
#     print('\n')
#
# print('-------------------')
# print(ns)