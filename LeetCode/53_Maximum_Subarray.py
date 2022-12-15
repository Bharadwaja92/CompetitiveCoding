"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""
"""
6.1 Dasgupta book

6.1. A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. For instance, if S is
5, 15, −30, 10, −5, 40, 10,
then 15, −30, 10 is a contiguous subsequence but 5, 15, 40 is not. Give a
linear-time algorithm for the following task:
Input: A list of numbers, a1, a2,..., an.
Output: The contiguous subsequence of maximum sum (a subsequence
of length zero has sum zero).
For the preceding example, the answer would be 10, −5, 40, 10, with a sum of 55.
(Hint: For each j ∈ {1, 2,..., n}, consider contiguous subsequences ending
exactly at position j.)
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        MAS = [0 for _ in range(len(nums))]
        MAS[0] = nums[0] 

        for i in range(1, len(nums)):
            MAS[i] = nums[i] + max(0, MAS[i-1])
            print(MAS)
        return max(MAS)


s = Solution()

nums = [5, 15, -30, 10, -5, 40, 10]
print(s.maxSubArray(nums))

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(s.maxSubArray(nums))

# nums = [1]
# print(s.maxSubArray(nums))

# nums = [5,4,-1,7,8]
# print(s.maxSubArray(nums))

