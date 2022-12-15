"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value 
in the inclusive range [low, high].

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(cur_node):
            nonlocal ans
            if cur_node:
                if low <= cur_node.val <= high:
                    ans += cur_node.val
                if low < cur_node.val:  # Go left
                    dfs(cur_node.left)
                if cur_node.val < high:  # Go right
                    dfs(cur_node.right)

        ans = 0    
        dfs(root)
        return ans



"""
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        cur_node = root
        flag = True
        while flag:
            if cur_node.val >= low and cur_node.left:
                # Go left
                cur_node = cur_node.left
                if low <= cur_node.val <= high:
                    ans += cur_node.val 
            if cur_node.val <= high and cur_node.right:
                # Go right
                cur_node = cur_node.right
                if low <= cur_node.val <= high:
                    ans += cur_node.val 
            else:
                flag = False
        return ans
"""