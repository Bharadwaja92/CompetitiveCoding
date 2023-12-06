"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. 
Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, 
the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        num_full_weeks = n // 7
        remaining_days = n % 7
        # print(n, num_full_weeks, remaining_days)

        week_sum = 28 #  7 * (7+1) // 2
        full_weeks_sum = (week_sum * num_full_weeks) + 7 * (num_full_weeks * (num_full_weeks-1) / 2)        

        remaining_days_sum = remaining_days * (remaining_days+1) / 2 + (num_full_weeks * remaining_days)
        # remaining_days_sum = 0
        
        # print(week_sum, full_weeks_sum, remaining_days_sum)

        return full_weeks_sum + remaining_days_sum
    

s = Solution()


n = 4
print(s.totalMoney(n))

n = 10
print(s.totalMoney(n))

n = 20
print(s.totalMoney(n))

n = 30
print(s.totalMoney(n))



