"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows, num_cols = len(matrix), len(matrix[0])

        min_rows, min_cols, max_rows, max_cols = 0, 0, num_rows, num_cols

        while min_rows < max_rows and min_cols < max_cols:
            row_index, col_index = min_rows, min_cols
            # Go right
            print('Go right')
            while col_index < max_cols:
                # print(row_index, col_index)                
                print(matrix[row_index][col_index])
                col_index += 1

            # Go down
            print('Go down')
            col_index -= 1
            row_index += 1 
            while row_index < max_rows:            
                # print(row_index, col_index)
                print(matrix[row_index][col_index])
                row_index += 1          

            # Go left
            print('Go left')
            row_index -= 1
            col_index -= 1
            while col_index >= min_cols:
                # print(row_index, col_index)
                print(matrix[row_index][col_index])
                col_index -= 1

            # Go up
            print('Go up')
            col_index += 1 
            row_index -= 1
            while row_index > min_rows:            
                # print(row_index, col_index)
                print(matrix[row_index][col_index])
                row_index -= 1
                
            min_rows += 1
            min_cols += 1
            max_rows -= 1
            max_cols -= 1

        return None



s = Solution()

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]]
# print(s.spiralOrder(matrix))


# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
#     ]
# print(s.spiralOrder(matrix))

# matrix = [
#     [1,2,3,4]
#     ]
# print(s.spiralOrder(matrix))

matrix = [
    [1],[2],[3],[4]
    ]
print(s.spiralOrder(matrix))
