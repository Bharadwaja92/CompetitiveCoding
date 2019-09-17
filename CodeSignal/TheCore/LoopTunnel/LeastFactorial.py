""""""
"""
Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example
For n = 17, the output should be
leastFactorial(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).
"""

def leastFactorial(n):
    f, m = 1, 0
    while f < n:
        m += 1
        f *= m
    print('f is', f)
    return m

print(leastFactorial(17))
print(leastFactorial(1700))

