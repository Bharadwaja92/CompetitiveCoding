"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
"""
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append((nums[i] + prefix_sums[-1]) % k)
        print(prefix_sums)
        return 0


s = Solution()

nums = [4,5,0,-2,-3,1]
k = 5
print(nums, '->', k, '->', s.subarraysDivByK(nums, k))


