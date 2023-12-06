"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
from typing import List
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        # print('Check rows')
        row_num = 0
        while row_num < len(board):
            row = [int(v) for v in board[row_num] if v != '.']
            values_cntr = sorted(list(set(Counter(row).values())))
            # print('row =', row, '--> values =', values_cntr)
            if not values_cntr:
                pass
            elif len(values_cntr) > 1 or values_cntr[0] != 1: return False
            row_num += 1
        # Check cols
        # print('Check cols')
        col_num = 0
        while col_num < len(board):
            col = [int(board[row_val][col_num]) for row_val in range(len(board)) if board[row_val][col_num] != '.']
            values_cntr = sorted(list(set(Counter(col).values())))
            # print('col =', col, '--> values =', values_cntr)
            if not values_cntr:
                pass
            elif len(values_cntr) > 1 or values_cntr[0] != 1: return False
            col_num += 1
        # Check grids
        # print('Check grids')
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sub_grid = [[board[row][col] for row in range(r, r+3)] for col in range(c, c+3)]
                sub_grid = [int(item) for sublist in sub_grid for item in sublist if item != '.']
                values_cntr = sorted(list(set(Counter(sub_grid).values())))
                # print(sub_grid =', sub_grid)
                if not values_cntr:
                    pass
                elif len(values_cntr) > 1 or values_cntr[0] != 1: return False

        return True


s = Solution()

# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
#     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# print(s.isValidSudoku(board))
#
# board = [["8","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]
# print(s.isValidSudoku(board))
#
# board = [ ["5", "3", ".", ".", "7", ".", ".", ".", "."]
#         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#         , [".", "9", "3", ".", ".", ".", ".", "6", "."]
#         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# print(s.isValidSudoku(board))

board = [[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]
print(s.isValidSudoku(board))

