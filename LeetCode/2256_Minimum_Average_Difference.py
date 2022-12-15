"""
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the 
average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. 
Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.
 

Example 1:
Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.
Example 2:

Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
"""

class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        forward_sums = [nums[0]]
        for num in nums[1:]:
            forward_sums.append(forward_sums[-1]+num)
        print('forward_sums =', forward_sums)

        reverse_sums = [nums[-1], 0]
        for num in nums[-2::-1]:
            reverse_sums.insert(0, reverse_sums[0]+num)
        print('reverse_sums =', reverse_sums)

        n = len(nums)
        min_index = n+1
        min_avg = 1e6
        for i in range(n-1):
            avg1 = forward_sums[i] // (i+1)
            avg2 = reverse_sums[i + 1] // (n-i-1)
            avg = abs(avg1 - avg2)
            print(i, '-->', avg1, '-->', avg2, '-->', avg)
            if min_avg > avg: min_avg = avg; min_index = i  

        if min_avg > forward_sums[-1] // n: return n-1
        return min_index


s = Solution()

nums = [2,5,3,9,5,3]
print('nums =', nums)
print(nums, '-->', s.minimumAverageDifference(nums))


nums = [0]
print(nums, '-->', s.minimumAverageDifference(nums))

nums = [4, 2, 0]
print(nums, '-->', s.minimumAverageDifference(nums))

