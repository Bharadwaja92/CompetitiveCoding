"""     https://projecteuler.net/problem=5      """
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from collections import Counter

allNums = list(range(2, 21))
print(allNums)

# Remove those that are already there


def getFactors(num):
    facs = [i for i in range(2, num+1) if num % i == 0]
    return facs


notremoved = []
allFactors = []
for n in allNums[::-1]:
    facs = getFactors(n)
    allFactors.extend(facs)

onlyOnce = [k for k, v in Counter(allFactors).items() if v == 1]
print(onlyOnce)
