"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeafNodes(node): 
            nonlocal leaves
            if node:
                print('cur node =', node.val)
                if node.left:
                    print('Going left')
                    getLeafNodes(node.left)
                if not node.right and not node.left:
                    leaves.append(node.val)
                    print('adding into leaves')
                if node.right:
                    print('Going right')
                    getLeafNodes(node.right)
            return leaves
        leaves = []
        l1 = getLeafNodes(root1)
        leaves = []
        l2 = getLeafNodes(root2)
        return l1 == l2


