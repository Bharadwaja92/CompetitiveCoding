""""""
"""
No time to explain! The World Government made contact with intelligent alien life, and needs you to send a message to 
the outer space. The aliens only receive messages that are stored in a sequence of lists of sizes 0, 1, 1, 2, 3, 5, ...,
 in other words those whose length increase according to the Fibonacci sequence.

The Government is too busy composing the message, and needs you to prepare the list in which the message should be sent.
 Given an integer n, return a list of n lists, where the first element consists is empty (consists of 0 zeros), 
 the second element consists of 1 zero, and so on.

Example

For n = 6, the output should be

fibonacciList(n) = [[], 
                    [0], 
                    [0], 
                    [0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0, 0, 0]]
"""

import functools

def fibonacciList(n):
    fs = []
    [fs.append(1 if i < 2 else (fs[-1] + fs[-2])) for i in range(10)]
    print(fs)
    fs = functools.reduce((lambda i, j: i+j if i < 2 else (fs[-1] + fs[-2])), range(n), 0)
    print(fs)

    return [[0] * x for x in functools.reduce((lambda i, j: i+[i[-1]+i[-2]]), range(n-1), [0,1])]


print(fibonacciList(6))

