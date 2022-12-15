"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pt = [[1],[1,1]]
        if numRows == 1: return [pt[0]]

        for r in range(2, numRows):
            row_values = [1 for _ in range(r+1)]
            for i in range(1, (r+1)//2 + 1):
                value_to_add = pt[r-1][i-1] + pt[r-1][i]
                print('r =', r, '--> i =', i, '-->', value_to_add)
                row_values[i] = value_to_add
                row_values[r-i] = value_to_add
            print('row_values = ', row_values)
            pt.append(row_values)

        return pt


s = Solution()

numRows = 1
print(s.generate(numRows))

numRows = 2
print(s.generate(numRows))
