"""
You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit.
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree
(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""

from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2: return len(fruits)
        local_max, global_max = 0, 0
        start = 0
        i = 0
        while i < len(fruits):
            current_selection = fruits[start:i+1]
            num_unique_fruits = len(set(current_selection))
            if num_unique_fruits > 2:
                start += 1
                i -= 1
            # elif num_unique_fruits == 2:
            else:
                local_max = len(current_selection)
            global_max = max(global_max, local_max)
            # print(current_selection, num_unique_fruits, local_max, global_max)
            i += 1

        return global_max


# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         # Hash map 'basket' to store the types of fruits.
#         basket = {}
#         left = 0

#         # Add fruit from the right index (right) of the window.
#         for right, fruit in enumerate(fruits):
#             basket[fruit] = basket.get(fruit, 0) + 1

#             # If the current window has more than 2 types of fruit,
#             # we remove one fruit from the left index (left) of the window.
#             if len(basket) > 2:
#                 basket[fruits[left]] -= 1

#                 # If the number of fruits[left] is 0, remove it from the basket.
#                 if basket[fruits[left]] == 0:
#                     del basket[fruits[left]]
#                 left += 1

#         # Once we finish the iteration, the indexes left and right
#         # stands for the longest valid subarray we encountered.
#         return right - left + 1

s = Solution()

fruits = [3,3,3,3,3,3]
print(fruits, s.totalFruit(fruits))

fruits = [1,2,3,2,2,1,4]
print(fruits, s.totalFruit(fruits))

fruits = [1,2,1]
print(fruits, s.totalFruit(fruits))

fruits = [0,1,2,2]
print(fruits, s.totalFruit(fruits))
#
# fruits = [1,2,3,2,2]
# print(fruits, s.totalFruit(fruits))
