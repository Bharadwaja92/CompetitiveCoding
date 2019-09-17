"""""""""
Daenerys Targaryen set her eyes on The Kingdom of The North which is ruled by the House Stark. There is a huge market 
in the Castle of Winterfell that sells products of all prices starting from 1 coin i.e. there are products worth Rs 
1, 2, 3 . . . 10^17 .

Ned Stark is the Lord of Winterfell. He gives Daenerys some coins. Each coin has its own denomination (in Rs). 
The coins need not be of distinct denomination. He asks Daenerys to predict the cheapest product that she will not be 
able to buy from the market using the coins given to her. If she can correctly predict it, she'll win the Castle of 
Winterfell and hence conquer one kingdom successfully.

If she can buy all products from the market (i.e all products upto price Rs 10^17 ), then output -1.

You're appointed as her advisor after she sent away Ser Jorah Mormont. So you need to solve the problem for her.

Input
The first line contains T, the number of test cases.
The first line of each test case contains an integer N denoting the number of coins Daenerys has.
The next line contains N space separated integers indicating the denominations of the coins (A_i).

Output: The only line of output should contain 1 integer denoting the price of the cheapest product that she cannot buy. 
If she can buy all the products, then this line contains -1.

Constraints: 
1 <= T <= 100
1 <= N <= 10^5
1 <= A_i <= 10^9 for i = 1, 2, .., N

Warning:  Large I/O files. Use scanf/printf instead of cin/cout or else use ios::sync_with_stdio(false).

Note: Partial marks are awarded if any test case passes.

SAMPLE INPUT 
2
10
1 2 4 8 16 32 64 128 256 512
5
1 3 4 5 7
SAMPLE OUTPUT 
1024
2
Explanation
In the first test case, Daenerys can buy all items upto 1023 since the coins available with her are powers of 2 
(in other words binary place values).

In the second test case, Daenerys needs Rs 2 coin in order to buy the Rs 2 product.
"""


def subsetSums(arr, l, r, sum=0):
    global sums
    if l > r:
        if sum not in sums or sum > 0:
            sums.append(sum)
        return

    subsetSums(arr, l + 1, r, sum + arr[l])
    subsetSums(arr, l + 1, r, sum)


t = int(input())

while t > 0:
    sums = []
    n = int(input())
    coins = list(map(int, input().split(' ')))
    # print('coins are', coins)
    subsetSums(coins, 0, n - 1)
    # print('--->', sums)
    minSum, maxSum = min(sums), max(sums)
    flag = True
    x = minSum
    while flag:
        x += 1
        flag = x in sums

    print('-->>>', x)
    t -= 1



