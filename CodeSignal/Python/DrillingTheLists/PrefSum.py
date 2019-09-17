""""""
"""
There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. 
It is based on the usage of prefix sums. Given array a, your task is to calculate all its prefix sums.

Example

For a = [1, 2, 3], the output should be
prefSum(a) = [1, 3, 6].

Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].
"""

fs = [0, 1]

[fs.append(fs[-1]+fs[-2]) for i in range(10)]       # Fibonacchi series

# print(fs)
import functools

def prefSum(a):
    # x = [a[0]]
    # y = x
    # for i in range(len(a)-1):
    #     x.append(a[i+1]+x[-1])
    # x.append([a[i+1]+x[-1] for i in range(len(a)-1)])
    y = functools.reduce(lambda x1, x2: x1 + [x1[-1]+x2], a, [0])
    y = functools.reduce(lambda x1, x2: x1 + x2, a)
    return list(y)


a = [1, 2, 3, 4]
print(a, '\n')
print(prefSum(a))
print('\n', [1, 3, 6, 10])

