"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""                             
Example 3:

Input: s = "s"
Output: "s"
"""

class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for c in s[1:]:
            if stack:
                top_char = stack[-1]
                if stack and c != top_char and (c.lower() == top_char or c == top_char.lower()):
                    # print('Remove these chars ', c, top_char)
                    # stack.remove(stack[-1]) . # Removes the first occurence of the last character
                    stack = stack[:-1]
                else:
                    stack.append(c)
            else:
                stack.append(c)
            print('Stack is ', stack)
        return s, ''.join(stack)


s1 = Solution()

s = 'cfJcaACjFC'
print(s1.makeGood(s))

"""
'cfJcaACjFC'
'cfJcCjFC'
'cfJjFC'
'cfFC'
'cC'
''
"""


# s = "leEeetcode"
# print(s1.makeGood(s))

# s = "abBAcC"
# print(s1.makeGood(s))

# s = "s"
# print(s1.makeGood(s))

# s = "abcdefFEDCBA"
# print(s1.makeGood(s))

# s = "abcdefFEDCBAA"
# print(s1.makeGood(s))


"""
def remove_pair (str):
    # Write your code here
    stk= []
    stk.append(str[0])
    top=0
    for i in range(1,len(str)):
        if top>=0 and str[i]==str[top]:
            top-=1
            stk.pop()
        else:
            top+=1
            stk.append(str[i])

    return ''.join(stk)

str = input()

out_ = remove_pair(str)
print (out_)
"""