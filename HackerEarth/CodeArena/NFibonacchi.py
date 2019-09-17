""""""
"""
Harold always boasted about his prowess with numbers. So one day Reese challenged him to a problem. 
He gave Harold two numbers X and Y and asked him to find out the Nth number of the series which began with X numbers 
of Y’s and the following elements are equal to the sum of the last X numbers in the series. 
Help Harold find the Nth number of the series.

Input:
The first line contains a number T , number of test cases.
The next T lines each contain 3 integers X, Y and N separated by single space.

Output: 
For each test case print the Nth number of the sequence.

SAMPLE INPUT 
1
3 2 7
SAMPLE OUTPUT 
-
34
Explanation
For X=3,Y=2 the series will be as follow:
2, 2, 2, 6, 10, 18, 34
"""

t = int(input())
# t = 1

while t > 0:
    fibList = []
    l1 = list(map(int, input().split(" ")))
    # l1 = list(map(int, '3 2 7'.split(" ")))
    x, y, n = l1[0], l1[1], l1[2]

    for i in range(x):
        fibList.append(y)
    sum1 = x*y
    fibList.append(sum1)

    for j in range(x, n):
        sum1 = 2*sum1 - fibList[j-x]
        fibList.append(sum1)

        print('fibList is', fibList)

    t -= 1



