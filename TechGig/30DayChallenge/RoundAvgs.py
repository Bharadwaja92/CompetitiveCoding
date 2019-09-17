"""
https://www.techgig.com/practice/question/day-24/OTYxSGxpR0FjWW9qRW5yeFhoRHNpSjJpZFduL2xOM2RkZ0UvM3lKb08rRW84UkFFZGQvYjgwNVd1anliUHdwRg==/1
"""
"""
For this challenge, you need to take number of elements as input on one line and array elements as an input on another 
line. You need to find the average of even numbers, then the average of odd numbers and add them (round the averages 
to the nearest integers). 

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated 
as input on another line. 

Constraints
1 < N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after addition of the two averages to the stdout. 

Sample TestCase 1
Input
6
11 22 33 44 55 66
Output
77
"""

n = int(input())
nums = list(map(int, input().split(' ')))
e0, e1, o0, o1 = 0, 0, 0, 0
for num in nums:
    # print(num)
    if num % 2 == 0:
        # print('Even ->', num)
        e1 += num
        e0 += 1
    else:
        # print('Odd ->', num)
        o1 += num
        o0 += 1

print(e0, e1, o0, o1)

if e0 > 0:
    e = round(e1 / e0)
else:
    e = 0

if o0 > 0:
    o = round(o1 / o0)
else:
    o = 0

print(e + o)

"""
7
1 5 6 4 7 8 15
"""

# odds, evens = [num for num in nums if num % 2 == 1], [num for num in nums if num % 2 == 0]
# oddAvg = 0 if len(odds) == 0 else round(sum(odds) / len(odds))
# evenAvg = 0 if len(evens) == 0 else round(sum(evens) / len(evens))
# print(odds, evens)
# print(oddAvg, evenAvg)
# print(oddAvg + evenAvg, end='')
