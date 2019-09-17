""""""
"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, 
and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For the first example below, the output should be true. For the other grid, the output should be false: each of the 
nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
"""

def sudoku(grid):
    for row in grid:
        if len(set(row)) != 9 or min(row) != 1 or max(row) != 9:
            return False
        if sum(row) != 45:
            return False
    transpose = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid))]
    for col in transpose:
        if len(set(col)) != 9 or min(col) != 1 or max(col) != 9:
            return False
        if sum(col) != 45:
            return False
    for g in range(0, 3):
        for h in range(0, 3):
            a = [[grid[j][i] for i in range(g*3, (g+1)*3)] for j in range(h*3, (h+1)*3)]
            gridSum = 0
            for r in a:
                gridSum += sum(r)
            if gridSum != 45:
                return False
    return True


grid = [
 [1,3,2,5,4,6,9,8,7],
 [4,6,5,8,7,9,3,2,1],
 [7,9,8,2,1,3,6,5,4],
 [9,2,1,4,3,5,8,7,6],
 [3,5,4,7,6,8,2,1,9],
 [6,8,7,1,9,2,5,4,3],
 [5,7,6,9,8,1,4,3,2],
 [2,4,3,6,5,7,1,9,8],
 [8,1,9,3,2,4,7,6,5]]

grid = [
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5],
 [5,5,5,5,5,5,5,5,5]]


grid = [
 [5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,8],
 [1,9,8,3,4,2,5,6,7],
 [8,5,9,7,6,1,4,2,3],
 [4,2,6,8,5,3,7,9,1],
 [7,1,3,9,2,4,8,5,6],
 [9,6,1,5,3,7,2,8,4],
 [2,5,7,4,1,9,6,3,5],
 [3,4,5,2,8,6,1,7,9]]
print(sudoku(grid))

