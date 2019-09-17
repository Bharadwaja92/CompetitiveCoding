""""""
"""
This problem of Oz is very straight forward. You are given N distinct prime integers i.e p1, p2,..., pN and an interval [L,R]. Calculate number of integers in this interval that are divisible by at least one of the given primes.
Input :  First line of input contain an integer T — the number of test cases. T tests follow. First line of each test case contain 3 integers — N, L, R. and the next line contains N distinct prime integers - p1, p2,..., pN.

Output : For each test case output a single number — number of integers in [L,R], that are divisible by at least one of the given primes.

SAMPLE INPUT 
2
1 1 10
3
2 1 10
2 3
SAMPLE OUTPUT 
3
7
Explanation
For second sample : 
Numbers in the interval [1,10] which are divisible by at least one prime from (2,3) are as follow :
2, 3, 4, 6, 8, 9, 10
"""

t = int(input())

while t > 0:
    l1 = list(map(int, input().split(" ")))
    n, l, r = l1[0], l1[1], l1[2]
    totalNums = r - l + 1
    nums = list(range(l, r+1))
    primes = list(map(int, input().split(" ")))
    for p in primes:
        for v in nums:
            if v % p == 0:
                nums.remove(v)
    print(totalNums - len(nums))
    t -= 1




