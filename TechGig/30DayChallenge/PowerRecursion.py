""""""
"""
This program takes two integers from user ( base number and a exponent) and calculates the power. Instead of using 
loops to calculate power, this program uses recursion to calculate the power of a number. 

Input Format
For this challenge, you need to take 2 integer inputs from stdin which are separated by a single space. 

Constraints
1 < N < 50
0 <= P <= 12
Output Format: You will print the answer to the stdout. 
Sample TestCase 1
Input
4 3
Output
64
"""


def calcPower(n, p, a=1):
    # print(n, p, a)
    if p == 0:
        return a
    a *= n
    return calcPower(n, p-1, a)


def main():
    nums = list(map(int, input().split(' ')))
    n, p = nums[0], nums[1]
    print(calcPower(n, p), end='')

main()