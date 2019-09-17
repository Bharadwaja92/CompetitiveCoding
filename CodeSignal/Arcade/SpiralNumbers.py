""""""
"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from 
top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
"""


def spiralNumbers(n):
    mat = [[0]*n for x in range(n)]
    print('mat is', mat)
    num = 1
    for row in range(n):
        if row % 2 == 0:
            x = [x+(row*n)+1 for x in range(n)]
            print('x is', x)
    return []


n = 3
print(spiralNumbers(n))