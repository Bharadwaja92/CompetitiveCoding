""""""
"""
https://www.spoj.com/problems/PRIME1/

Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers 
between two given numbers!

Input
The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two 
numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an 
empty line.

Example
Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
"""
from math import sqrt

primes = [2]
for i in range(3, int(sqrt(1000000000)), 2):
    is_prime = True
    cap = sqrt(i) + 1

    for j in primes:
        if j >= cap:
            break
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

# print('primes are', primes)

t = int(input())

while t > 0:
    l1 = list(map(int, input().split(' ')))
    m, n = l1[0], l1[1]
    cap = sqrt(n) + 1

    m = 2 if m < 2 else m

    isprime = [True]*100001

    for i in primes:
        if i >= cap:
            break

        if i >= m:
            start = i*2
        else:
            start = m + ((i - m % i) % i)

        falseblock = [False] * len(isprime[start - m:n + 1 - m:i])
        isprime[start - m:n + 1 - m:i] = falseblock

    for i in range(m, n + 1):
        if isprime[i - m]:
            print(str(i))

    print('')

    t -= 1



