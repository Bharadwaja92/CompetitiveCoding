"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number
 in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines
  we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
"""

def minesweeper(matrix):
    mat = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            count = 0
            for i1 in range(-1, 2):
                for j1 in range(-1, 2):
                    x, y = i-i1, j-j1
                    if x in range(0,len(matrix)) and y in range(0,len(matrix[0])): # and x!=i and y!=j):
                        print('x = ', x, 'y = ', y, ' for i=', i, 'j =', j)
                        if matrix[x][y]:
                            count += 1
                            print('Count incremented')
            if matrix[i][j]:
                count -= 1
            print('\n\n')
            row.append(count)
        mat.append(row)

    return mat


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

matrix = [[True,False,False,True],
 [False,False,True,False],
 [True,True,False,True]]

print(minesweeper(matrix))