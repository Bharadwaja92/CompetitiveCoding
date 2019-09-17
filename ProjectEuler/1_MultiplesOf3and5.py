"""   https://projecteuler.net/problem=1  """
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

sum = 0

for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)

"""           EFFICIENT SOLUTION        """

limit = 1000


def getSum(n):
    p = limit // n
    return n*(p*(p+1)) // 2


print(getSum(3) + getSum(5) - getSum(15))

