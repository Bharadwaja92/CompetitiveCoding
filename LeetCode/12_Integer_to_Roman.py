"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
"""

from operator import le


class Solution:
    def intToRoman(self, num: int) -> str:

        symbol_dict = {
            1: 'I', 
            5: 'V', 
            10: 'X', 
            50: 'L', 
            100: 'C', 
            500: 'D', 
            1000: 'M', 
        } 

        roman = ''
        bases = list(symbol_dict.keys())[::-1]
        bases1 = [x - 1 for x in bases][:-1]
        # print('bases =', bases)
        # print('bases1 =', bases1)
        while num:
            # Get the biggest base in the dictionary
            i = 0
            while i < len(bases) and bases[i] > num: 
                i += 1
            current_base = bases[i]
            # print('i =', i, '-->', current_base)

            num_bases_in_number = num // current_base
            # print('num_bases_in_number =', num_bases_in_number)
            
            if num_bases_in_number in bases1:
                x = bases1.index(num_bases_in_number)
                # print('bases1 -->', x, '-->', bases[x])
                roman += symbol_dict[current_base] + symbol_dict[bases[i-1]]
            else:
                roman += symbol_dict[current_base] * num_bases_in_number

            num %= current_base
            # print('roman =', roman, '   num =', num)
            
        return roman



s = Solution()

# print(s.intToRoman(3))
# print(s.intToRoman(413))
# print(s.intToRoman(513))
# print(s.intToRoman(1994))

t = [1, 2, 3, 4 , 5, 9, 10, 44, 86, 99, 101, 190, 209, 399, 999, 1001]

for x in t:
    print(x, '-->', s.intToRoman(x))

