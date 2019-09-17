"""
Given a sorted array of integers a, find an integer x from a such that the value of

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
is the smallest possible (here abs denotes the absolute value).
If there are several possible answers, output the smallest one.

For a = [2, 4, 7], the output should be
absoluteValuesSumMinimization(a) = 4.

0 - 2+4+7=13
1 - 1+3+6=10
2 - 0+2+5=7
3 - 1+1+4=6
4 - 2+0+3=5
5 - 3+1+2=6
"""

import math
def absoluteValuesSumMinimization(a):
    return a[math.ceil(len(a)/2)-1];

a = [2, 4, 7]
print(absoluteValuesSumMinimization(a))
