# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # N L R 
        return_list = []
        self.preorder_helper(root, return_list)
        return return_list
    
    def preorder_helper(self, root:Optional[TreeNode], return_list:List)-> None:
        if root is None:
            return None

        return_list.append(root.val)
        self.preorder_helper(root.left, return_list)
        self.preorder_helper(root.right, return_list)

