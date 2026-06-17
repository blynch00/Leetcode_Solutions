# Definition for a binary tree node.
from collections import *
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final_arr = []
        def orderHelper(level = 0, root= None):

            if root is None:
                return
            
            while level >= len(final_arr):
                final_arr.append([])
             
            final_arr[level].append(root.val)
            orderHelper(level + 1, root.left)
            orderHelper(level + 1, root.right)
            return

        orderHelper(0, root)
        return final_arr

