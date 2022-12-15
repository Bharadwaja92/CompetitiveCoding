"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_cost = 99999
        num_days = len(prices)

        for d in range(0, num_days):
            curr_cost = prices[d]
            min_cost = min(min_cost, curr_cost)
            curr_profit = curr_cost - min_cost
            max_profit = max(max_profit, curr_profit)

        return max_profit

    def maxProfit_n2(self, prices: list[int]) -> int:
        max_profit = 0
        num_days = len(prices)
        # trxs = [[0 for c in range(num_days)] for r in range(num_days)]

        for r in range(0, num_days-1):
            for c in range(r+1, num_days):
                today_profit = prices[c] - prices[r]
                max_profit = max(max_profit, today_profit)
                # print(prices[c], prices[r], max_profit)
                # trxs[r][c] = today_profit

        # print(trxs)
        return max_profit


s = Solution()

prices = [7,1,5,3,6,4]
print(prices, '-->', s.maxProfit(prices))


prices = [7,6,4,3,1]
print(prices, '-->', s.maxProfit(prices))


prices = [1, 2]
print(prices, '-->', s.maxProfit(prices))


