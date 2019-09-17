""""""
"""
You are standing at a magical well. It has two positive integers written on it: a and b. Each time you cast a magic 
marble into the well, it gives you a * b dollars and then both a and b increase by 1. You have n magic marbles. 
How much money will you make?

Example

For a = 1, b = 2, and n = 2, the output should be
magicalWell(a, b, n) = 8.

You will cast your first marble and get $2, after which the numbers will become 2 and 3. When you cast your second 
marble, the well will give you $6. Overall, you'll make $8. So, the output is 8.
"""


def magicalWell1(a, b, n):
    sum = 0
    while n > 0:
        sum += (a*b)
        a += 1
        b += 1
        n -= 1
    return sum


def magicalWell(a, b, n):
    return sum([(a+i)*(b+i) for i in range(n)])


a, b, n = 1, 2, 2
print(magicalWell(a, b, n))
a, b, n = 1, 1, 1
print(magicalWell(a, b, n))
a, b, n = 1607, 333, 0
print(magicalWell(a, b, n))
a, b, n = 491, 1552, 4
print(magicalWell(a, b, n))
