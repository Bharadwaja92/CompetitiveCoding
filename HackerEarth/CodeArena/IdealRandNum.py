""""""
"""
Assume there is an Ideal Random Number Generator which generates any real number between 0 and given integer. Two 
numbers are generated from the above generator using integer A and B, let's assume the numbers generated are X1 and X2. 
There is another integer C. What is the probability that summation of X1 and X2 is less than C.

Input Format: A single line containing three integers A,B,C

1 <= A,B,C <= 100000

Output Format:  Print the probability in form of P/Q

SAMPLE INPUT 
1 1 1
SAMPLE OUTPUT 
1/2
Explanation:    For example if A and B are 1. Then the random number generated will be any real number between 0 - 1.

0 < x1 < 1  and  0 < x2 < 1

If C is also 1, then you need to determine the probability of that x1 + x2 < C.
"""

l1 = list(map(int, input().split(" ")))
a, b, c = l1[0], l1[1], l1[2]

mid = c//2
combs = 0

for i in range(mid+1):
    if c - i < b:
        print(i, '->', c-i, '->', b, '->', c)



