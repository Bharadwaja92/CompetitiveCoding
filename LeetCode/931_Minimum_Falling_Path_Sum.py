"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is 
either directly below or diagonally left/right. 
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
"""


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        matrix_sums = [[0 for _ in range(n)] for x in range(n)]
        matrix_sums[-1] = matrix[-1]
        for r in range(n-2, -1, -1):
            sum_row = [matrix[r][0] + min(matrix_sums[r+1][0], matrix_sums[r+1][1])]
            # print(r, '-->', matrix[r], '-->', sum_row)
            c = 0
            for c in range(1, n-1):
                sum_row.append(matrix[r][c] + min(matrix_sums[r+1][c-1], matrix_sums[r+1][c], matrix_sums[r+1][c+1]))
                # print(r, '-->', matrix[r], '-->', sum_row)
            sum_row.append(matrix[r][-1] + min(matrix_sums[r+1][c], matrix_sums[r+1][c+1]))
            # print(r, '-->', matrix[r], '-->', sum_row)
            matrix_sums[r] = sum_row              
        #     print('-->', matrix[r], '-->', matrix_sums[r])  
        # print(matrix_sums)
        return min(matrix_sums[0])


s = Solution()

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(matrix, '-->', s.minFallingPathSum(matrix))

# print('*'*30)

matrix = [[-19,57],[-40,-5]]
print(matrix, '-->', s.minFallingPathSum(matrix))

"""
[2,1,3]                   15, 13, 15
[6,5,4]   6+7, 5+7, 4+8   13, 12, 12   
[7,8,9]   7,     8,   9 | 7,   8,  9      


[-19,57],  -59, -17 
[-40,-5]   -40,  -5

"""
"""
def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        matrix_sums = [[0 for _ in range(n)] for x in range(n)]
        matrix_sums[-1] = matrix[-1]
        for r in range(n-2, -1, -1):
            sum_row = [matrix[r][0] + min(matrix_sums[r+1][0], matrix_sums[r+1][1])]
            for c in range(1, n-1):
                sum_row.append(matrix[r][c] + min(matrix[r+1][c-1], matrix[r+1][c], matrix[r+1][c+1]))
            sum_row.append(matrix[r][-1] + min(matrix_sums[r+1][c+1], matrix_sums[r+1][c]))
            matrix_sums[r] = sum_row              
            print('-->', matrix[r], '-->', matrix_sums[r])  
        print(matrix_sums)
        return min(matrix_sums[0])
"""