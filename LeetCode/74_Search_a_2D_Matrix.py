"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""


from typing import List


class Solution:
    def doBinarySearch(self, nums, element, l, r):
        if l <= r:
            mid = (l + r) // 2
            # print(l, mid, r)
            if nums[mid] == element:
                # print('Found', element, 'at position', mid)
                return mid
            elif nums[mid] < element:
                # print('Going right')
                return self.doBinarySearch(nums, element, mid + 1, r)
            else:
                # print('Going left')
                return self.doBinarySearch(nums, element, l, mid - 1)
        else:
            return -1
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find which row
        first_elements = [r[0] for r in matrix]
        print('first_elements =', first_elements)
        # Here get the first index of the element that is small than our target
        row_to_search = self.doBinarySearch(nums=first_elements, element=target, l=0, r=len(first_elements)-1)
        print('row_to_search =', row_to_search)
        if row_to_search == -1: 
            return False
        else:
            cols_to_search = matrix[row_to_search]
            print('cols_to_search =', cols_to_search)
            pos = self.doBinarySearch(nums=cols_to_search, element=target, l=0, r=len(cols_to_search)-1)
        return False if pos == -1 else True


s = Solution()

# nums = [1, 3, 5, 7, 10, 11, 16, 20]
# print(s.doBinarySearch(nums, 3, 0, len(nums) - 1))
# print(s.doBinarySearch(nums, 20, 0, len(nums) - 1))


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(s.searchMatrix(matrix, target))
