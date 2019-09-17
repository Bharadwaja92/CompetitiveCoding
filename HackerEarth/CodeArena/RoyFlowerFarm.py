""""""
"""
https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/roy-and-flower-farm/

Roy is the owner of a flower plant farm and sells flower plants for a living.  Now the problem with flower plants is 
that they wither in a night if not taken care of. So at the end of the day, to make flower plants wither-resistant Roy 
uses special fertilizers.
There are N number of plants not sold on one particular day (say today), but Roy can sell them the next day (say 
tomorrow) if he fertilizes them tonight.  Roy sells a flower plant for Rs. X. Cost of fertilizing a plant is Rs. Y. 
Currently Roy has P Rupees with him.

Given the selling price X and fertilizing cost Y of N plants, your task is to find minimum amount A (A ≤ P) that he 
should spend in fertilizing plants such that the total money he has after selling plants on the next day is maximized. 
Assume that all the fertilized plants are sold on the next day.

Input Format: First line contains integer T - number of test cases.
Second line contains two space separated integers N and P.
Following N lines each contain two space separated integers X and Y.

Output Format:  Print the two space separated integers A and B in a new line for each test case.

SAMPLE INPUT 
2
2 50
80 40
60 20
5 100
100 40
50 40
40 50
60 20
100 50
SAMPLE OUTPUT 
20 90
90 210

Explanation

Test Case #1:  He has Rs. 50 with him in the beginning. To fertilize both the plants he needs Rs. 60. So he has to 
            choose one of them. Now profit from both the plants is equal i.e Rs. 40. But the cost of fertilizing second 
            plant is less. Hence the Minimum Amount to spend is Rs. 20 and total money he has after selling the plants 
            is 50 - 20 + 60 = 90

Test Case #2:  Profit for each of the plants is 60, 10, -10, 40, 50 respectively. He has Rs. 100 with him. The optimal 
            selection would be fertilize first and last plant. So Minimum Amount to spend is Rs. 90 and total money he 
            has after selling the plants is 100 - 40 - 50 + 100 + 100 =210
"""


# def getBestPossibleCombination(weights, values, sackWgt, numItems):
#
#     # Base case
#     if numItems == 0 or sackWgt == 0:
#         return 0
#     # If the last item exceeds the capacity, don't include it.
#     if weights[numItems-1] > sackWgt:
#         return getBestPossibleCombination(weights, values, sackWgt, numItems-1)
#
#     valueIfIncluded = values[numItems-1]+ getBestPossibleCombination(weights, values, sackWgt-weights[numItems-1], numItems-1)
#     valueIfNotIncluded = getBestPossibleCombination(weights, values, sackWgt, numItems-1)
#
#     return max(valueIfIncluded, valueIfNotIncluded)
# weights = [1, 2, 3]
# values = [6, 10, 12]
# sackWgt = 5
# numItems = len(values)
# print(getBestPossibleCombination(weights, values, sackWgt, numItems))
# print(getBestPossibleCombination1(sackWgt, weights, values, numItems))

t = int(input())

while t > 0:
    sellingPrice, costs, profits = [], [], []
    l1 = list(map(int, input().split(" ")))
    n, p = l1[0], l1[1]                         # p = initial money
    for i in range(n):
        l2 = list(map(int, input().split(" ")))
        px, cx = l2[0], l2[1]
        sellingPrice.append(px)
        costs.append(cx)                         # weights
        profits.append(px-cx)                     # values

    dp = [[0 for p1 in range(n+1)] for n1 in range(p+1)]
    exps = [[0 for p1 in range(n+1)] for n1 in range(p+1)]

    print(len(dp), len(dp[0]))

    for i in range(p+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j], exps[i][j] = 0, 0
                continue

            dp[i][j], exps[i][j] = dp[i][j-1], exps[i][j-1]

            if costs[j-1] <= sellingPrice[j-1] and i >= costs[j-1]:
                if dp[i][j] < dp[i - costs[j - 1]][j - 1] + sellingPrice[j - 1] - costs[j - 1]:
                    dp[i][j] = dp[i-costs[j-1]][j-1]+sellingPrice[j-1]-costs[j-1]
                    exps[i][j] = exps[i-costs[j-1]][j-1]+costs[j-1]
            if dp[i][j] == dp[i - costs[j - 1]][j - 1] + sellingPrice[j - 1] - costs[j - 1] and \
                        exps[i][j] > exps[i - costs[j - 1]][j - 1] + costs[j - 1]:
                exps[i][j] = exps[i - costs[j - 1]][j - 1] + costs[j - 1]

    profit = dp[p][n] + p
    print(str(exps[p][n]) + ' -> ' + str(profit))

    t -= 1



