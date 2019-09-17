""""""
"""
Pussycat Sonya has an array A consisting of N integers (N is even). She can perform operations of two types:

increase value of some element Ai by 1
delete some adjacent elements Ai and Ai+1 such that they are consecutive prime numbers (Ai is a prime number and Ai+1 
is the next prime number)
She wants to delete all elements from array A. What is the minimal number of operations that she needs to perform?
Input:
The first line of input contains one even integer N - the number of elements in array A.
The second line contains N space separated positive integers - elements of array A.

Output:  Print the minimal number of operations that Sonya needs to perform.

Note:   A prime number is an integer greater than 1 that has no positive divisors other than 1 and itself.

SAMPLE INPUT 
4
1 2 4 3
SAMPLE OUTPUT 
5
Explanation
increase the 2-nd element {1, 2, 4, 3} => {1, 3, 4, 3}
increase the 3-rd element {1, 3, 4, 3} => {1, 3, 5, 3}
delete the 2-nd and 3-rd elements {1, 3, 5, 3} => {1, 3}
increase the 1-st element {1, 3} => {2, 3}
delete the 1-st and 2-nd elements {2, 3} => { }
"""

MAX = 100005
INT_MAX = 10000000


def sieveForPrimes(prev, nxt):
    pr = [0 for i in range(MAX)]

    pr[1] = 1
    for i in range(1, MAX):
        if pr[i]:
            continue
        for j in range(i * 2, MAX, i):
            pr[j] = 1

    # Computing next prime each number.
    for i in range(MAX - 2, -1, -1):
        if (pr[i] == 0):
            nxt[i] = i
        else:
            nxt[i] = nxt[i + 1]

            # Computing previous prime each number.
    for i in range(1, MAX):
        if pr[i] == 0:
            prev[i] = i
        else:
            prev[i] = prev[i - 1]


def cost(a, b, prev, nxt):
    sub = a + b
    if a <= b and prev[b - 1] >= a:
        return nxt[b] + prev[b - 1] - a - b

    a = max(a, b)
    a = nxt[a]
    b = nxt[a + 1]
    return a + b - sub


def minOperation(a, nxt, prev, n):
    dp = [[0 for i in range(n+5)] for i in range(n+5)]

    for r in range(n):
        for l in range(r-1, -1, -2):
            dp[l][r] = INT_MAX

            for ad in range(l, r, 2):
                dp[l][r] = min(dp[l][r], dp[l][ad] + dp[ad + 1][r - 1] + cost(a[ad], a[r], prev, nxt))

    return dp[0][n - 1] + n // 2


n = int(input())
a = list(map(int, input().split(" ")))

nxt = [0 for i in range(MAX)]
prev = [0 for i in range(MAX)]
sieveForPrimes(prev, nxt)

print(minOperation(a, nxt, prev, n))


