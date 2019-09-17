"""     https://projecteuler.net/problem=7         """
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

n = 1000

def isPrime(n):
    for i in range(2, (n // 2)+1):
        if n % i == 0:
            return False
    return True


count, i = 0, 1
while count < 10001:
    i += 1
    if isPrime(i):
        count += 1
        print('Prime #{} is {}'.format(count, i))

print(i)