"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case
        if p == None and q == None: return True
        if p == None or q == None: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
def do_iot(root):
            if root:
                do_iot(root.left)
                nodes.append(None)
                nodes.append(root.val)
                nodes.append(None)
                do_iot(root.right)
            return nodes
        
        nodes = []
        p_nodes = do_iot(p)
        nodes = []
        q_nodes = do_iot(q)

        return p_nodes == q_nodes
"""
