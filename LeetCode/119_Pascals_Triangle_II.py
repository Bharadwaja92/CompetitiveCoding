"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pt = [[1],[1,1]]
        if rowIndex == 0: return pt[0]
        if rowIndex == 1: return pt[1]

        for r in range(2, rowIndex+1):
            row_values = [1 for _ in range(r+1)]
            for i in range(1, (r+1)//2 + 1):
                value_to_add = pt[r-1][i-1] + pt[r-1][i]
                print('r =', r, '--> i =', i, '-->', value_to_add)
                row_values[i] = value_to_add
                row_values[r-i] = value_to_add
            print('row_values = ', row_values)
            pt.append(row_values)

        return pt[rowIndex]


s = Solution()

rowIndex = 0
print(s.getRow(rowIndex))

rowIndex = 1
print(s.getRow(rowIndex))

rowIndex = 2
print(s.getRow(rowIndex))

rowIndex = 3
print(s.getRow(rowIndex))