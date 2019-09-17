""""""
"""
For this challenge, you need to take number of elements as input on one line and array elements as an input on another 
line and find the second largest array element and print that element to the stdout. 

Input Format: In this challenge, you will take number of elements as input on one line and array elements which are 
space separated as input on another line. 

Constraints
1 < = n < = 100000
1 < = a[i] < = 10^9

Output Format
You will print the second largest element to the stdout. 

Sample TestCase 1
Input
6
11 22 33 44 55 66
Output
55
"""


def run():
    n = int(input())
    nums = list(map(int, input().split(' ')))
    v1, v2 = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
    for i in range(2, n):
        v1, v2 = (nums[i], v1) if nums[i] > v1 else (v1, nums[i]) if nums[i] > v2 else (v1, v2)
    print(v2)


run()
