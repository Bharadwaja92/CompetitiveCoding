from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        cntr=Counter(Counter(s).values())
        print('cntr =', cntr)

        repeated_nums = [num for num, count in cntr.items() if count > 1]
        print('repeated_nums =', repeated_nums)

        unique_nums = set(cntr.values())
        print('unique_nums =', unique_nums)
 
        changes = 0
        for num in repeated_nums:
            print('num =', num, '-->', num in unique_nums)
            while num in unique_nums:
                num += 1
                changes += 1
            unique_nums.add(num)

        return changes
    
s1 = Solution()

s = "aab"
print(s1.minDeletions(s))

s = "aaabbbcc"
print(s1.minDeletions(s))

s = "ceabaacb"
print(s1.minDeletions(s))