"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, 
and there will not be any division by zero operation.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for c in tokens:
            if c in ['+', '-', '*', '/']:
                num1, num2 = nums[-1], nums[-2]
                val = num1 + num2 if c == '+' else num2 - num1 if c == '-' \
                                                else num1 * num2 if c == '*' else int(num2 / num1)
                nums = nums[:-2]
                nums.append(val)
            else:
                nums.append(int(c))
            # print('nums =', nums)
        return nums[0]


s = Solution()

tokens = ["2","1","+","3","*"]
print(s.evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(s.evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(s.evalRPN(tokens))