"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first
 half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
"""

def isLucky(n):
    n1 = list(map(int, list(str(n))))
    l = int(len(n1)/2)
    return sum(n1[:l]) == sum(n1[l:])


print(isLucky(12330))

