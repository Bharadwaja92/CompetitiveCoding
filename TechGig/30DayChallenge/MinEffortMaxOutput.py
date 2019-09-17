""""""
"""
For this challenge, Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that 
sorting this subarray makes the whole array sorted. 

Input Format: On the first line, you need to take an integer input which will be the length of the array. Another line 
will have space separated integer values. 

Constraints
1 < n < 10^5
1 < A[i] < 10^5

Output Format: Space separated integer values present in the subarray. 

Sample TestCase 1
Input
13
1 2 4 7 10 11 7 12 3 7 16 18 19
Output
4 7 10 11 7 12 3 7
"""

n = int(input())
nums = list(map(int, input().split(' ')))

nums1 = sorted(nums)
s, e = 0, 0

while nums[s] == nums1[s]:
    s += 1

while nums[-e] == nums1[-e]:
    e += 1

# print(s, e, nums[s:(n-e+1)])
print(' '.join(list(map(str, nums[s:(n-e+1)]))), end='')