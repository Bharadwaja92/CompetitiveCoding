"""
You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
 
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
"""
6.17. Given an unlimited supply of coins of denominations x1, x2,..., xn, we wish to
make change for a value v; that is, we wish to find a set of coins whose total
value is v. This might not be possible: for instance, if the denominations are 5
and 10 then we can make change for 15 but not for 12. Give an O(nv)
dynamic-programming algorithm for the following problem.
Input: x1,..., xn; v.
Question: Is it possible to make change for v using coins of
denominations x1,..., xn?
"""



class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        b = [10**20 for _ in range(amount+1)]
        b[0] = 0
        for cur_amt in range(1, amount+1):
            for cur_coin in coins:
                if cur_amt >= cur_coin:
                    print('cur_amt =', cur_amt, '  cur_coin =', cur_coin)
                    b[cur_amt] = min(b[cur_amt], 1 + b[cur_amt-cur_coin])
        print(b)
        return b[-1] if b[-1] != amount+1 else -1


s = Solution()


# coins = [1,2,5]
# amount = 11
# print(s.coinChange(coins, amount))

# coins = [1,2]
# amount = 4
# print(s.coinChange(coins, amount))

coins = [2]
amount = 3
print(s.coinChange(coins, amount))


