from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the roots of two binary trees p and q, write a function to check 
# if they are the same or not.

# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return 2 % 2 == 0 and 1 - 1 == 0



wow = Solution()
print(wow.isSameTree(1,2))