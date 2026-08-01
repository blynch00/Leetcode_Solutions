from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Longest distance will be between 2 leaf nodes
        # # Of edges, i.e. nodes crossed
        # May or may not pass through root

        self.diameter = 0
        if root.left is None and root.right is None:
            return self.diameter

        self.helper_diameter(root)
        return self.diameter
    def helper_diameter(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return -1

        left_branch = self.helper_diameter(root.left)
        right_branch = self.helper_diameter(root.right)
        maximum = (left_branch + right_branch) + 2

        self.diameter = max(self.diameter, maximum)

        return max(left_branch, right_branch) + 1
