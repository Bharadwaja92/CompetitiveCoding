"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
"""
from collections import Counter

def deleteDigit1(n):
    nums = list(map(int, list(str(n))))
    # cr = Counter(nums)
    nums.remove(min(nums))
    a = ""
    for x in nums:
        a += str(x)
    return a

def deleteDigit(n1):
    m, d = 0, 1
    while d <= n1:
        m = max(m, int((n/d)/10)*d + n%d)
        d *= 10
    return m


"""
    for(d = 1;d <= n; d*=10)
        m = Math.max(m, ((n/d)/10)*d + n%d);
    return m;
"""

n = 152
n = 1001
n = 22219
n = 2102
n = 823829
print(deleteDigit(n))
print(deleteDigit1(n))
