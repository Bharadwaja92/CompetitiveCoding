"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:  # Go left
                right = mid - 1
            else:
                left = mid + 1
        return -1


s = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(nums, '-->', target, '-->', s.search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(nums, '-->', target, '-->', s.search(nums, target))


""" RECURSIVE
def do_binary_search(nums, left, right, target):
    if right >= left:
        mid = (right + left) // 2
        print('left = {}, mid = {}, right = {}, current = {}'.format(left, mid, right, nums[mid]))
        if nums[mid] == target: return mid
        elif nums[mid] > target:  # Go Left
            print('Go left')
            return do_binary_search(nums, left, mid-1, target)
        else:
            print('Go right')
            return do_binary_search(nums, mid+1, right, target)
    else:
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return do_binary_search(nums, 0, len(nums)-1, target)
"""