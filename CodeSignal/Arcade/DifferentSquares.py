"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

>  1 2, 2 2
>  2 1, 2 2
>  2 2, 2 2
>  2 2, 1 2
>  2 2, 2 3
>  2 3, 2 1

"""

def differentSquares(matrix):
    s = set()
    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[i])-1):
            t = " ".join(str(n) for n in matrix[i][j:j+2]).join(str(n) for n in matrix[i+1][j:j+2])
            s.add(t)
    return len(s)


matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

print(differentSquares(matrix))