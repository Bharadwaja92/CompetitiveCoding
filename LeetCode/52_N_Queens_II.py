"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.


Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""
from typing import List
import copy

def is_not_under_attack(board, row, col):
    return not board[row][col] > 0


def place_queen(board, row, col):
    board[row][col] = 'Q'
    # All row under attack
    for col_num in range(len(board)):
        if col_num != col:
            board[row][col_num] += 1
    # All col under attack
    for row_num in range(len(board)):
        if row_num != row:
            board[row_num][col] += 1
    # Both diagonals under attack
    # Diag 1 - Go up  \
    row_num, col_num = row - 1, col - 1
    while row_num >= 0 and col_num >= 0:
        board[row_num][col_num] += 1
        row_num -= 1
        col_num -= 1
    # Diag 1 - Go down  \
    row_num, col_num = row + 1, col + 1
    while row_num < len(board) and col_num < len(board):
        board[row_num][col_num] += 1
        row_num += 1
        col_num += 1

    # Diag 2 - Go up  /
    row_num, col_num = row - 1, col + 1
    while row_num >= 0 and col_num < len(board):
        board[row_num][col_num] += 1
        row_num -= 1
        col_num += 1
    # Diag 2 - Go down  /
    row_num, col_num = row + 1, col - 1
    while row_num < len(board) and col_num >= 0:
        board[row_num][col_num] += 1
        row_num += 1
        col_num -= 1

    return board


def print_board(board):
    for r in range(n):
        print(', '.join(list(map(str, board[r]))))


def remove_queen(board, row, col):
    # Remove queen
    board[row][col] = 0
    # Remove row attacks
    for col_num in range(len(board)):
        if col_num != col:
            board[row][col_num] -= 1
    # Remove col attacks
    for row_num in range(len(board)):
        if row_num != row:
            board[row_num][col] -= 1

    # Both diagonals under attack
    # Diag 1 - Go up  \
    row_num, col_num = row - 1, col - 1
    while row_num >= 0 and col_num >= 0:
        board[row_num][col_num] -= 1
        row_num -= 1
        col_num -= 1
    # Diag 1 - Go down  \
    row_num, col_num = row + 1, col + 1
    while row_num < len(board) and col_num < len(board):
        board[row_num][col_num] -= 1
        row_num += 1
        col_num += 1

    # Diag 2 - Go up  /
    row_num, col_num = row - 1, col + 1
    while row_num >= 0 and col_num < len(board):
        board[row_num][col_num] -= 1
        row_num -= 1
        col_num += 1
    # Diag 2 - Go down  /
    row_num, col_num = row + 1, col - 1
    while row_num < len(board) and col_num >= 0:
        board[row_num][col_num] -= 1
        row_num += 1
        col_num -= 1

    return board


class Solution:

    def totalNQueens(self, n: int) -> int:
        board = [[0 for _ in range(n)] for __ in range(n)]

        def backtrack_nqueens(n=0, board=None, row=0):
            nonlocal count
            # global successful_placements
            for col in range(n):
                if is_not_under_attack(board, row, col):
                    board = place_queen(board, row, col)
                    if row == n - 1:
                        count += 1
                    else:
                        successful_placements = backtrack_nqueens(n, board, row + 1)

                    # Backtrack. Remove queen and clear the attacking zone
                    board = remove_queen(board, row, col)
            return count

        count = 0
        backtrack_nqueens(n=n, board=board, row=0)
        # print('successful_placements =', successful_placements)

        return count


s = Solution()

n = 4
print(s.totalNQueens(n))

n = 6
print(s.totalNQueens(n))
