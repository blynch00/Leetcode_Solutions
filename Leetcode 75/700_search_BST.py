from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 1. Check if root is empty
        if root is None:
            return root
        
        # 2. Check if root.left and root.right do not exist
        if root.right is None and root.left is None:
            if root.val != val:
                return None

        # 3. Determine if value is larger or smaller
        if root.val > val:
            return self.searchBST(root.left, val)

        elif root.val < val:
            return self.searchBST(root.right, val)
        
        else:
            return root