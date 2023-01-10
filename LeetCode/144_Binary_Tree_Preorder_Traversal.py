"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def do_inorder(root):
            if root:
                order.append(root.val)
                do_inorder(root.left)
                do_inorder(root.right)
            return order

        order = []
        iot = do_inorder(root)
        # print(iot)

        return iot

