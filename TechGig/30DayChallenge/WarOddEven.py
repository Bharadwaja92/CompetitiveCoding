"""""""""
War between odd and even (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another 
line. You need to find the numbers that are present at odd index, add them. find the numbers that are present at even 
index, add them and then subtract the smallest of the two values from the lager one. 
Note: 
Array indexes always starts from 0. 

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated 
as input on another line. 

Constraints
1 <  N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after subtraction to the stdout.

Sample TestCase 1
Input
6
11 22 33 44 55 66
Output
33
Explanation
Of all the given elements which are in the array, identify numbers that are present at odd index and add them. 
Identify even index numbers and add them. Subtract the smaller vale from the larger one.
"""

n = int(input())
nums = list(map(int, input().split(' ')))

odds = sum([nums[i] for i in range(0, n, 2)])
evens = sum([nums[i] for i in range(1, n, 2)])

val = odds - evens if odds > evens else evens - odds

print(val, end='')
