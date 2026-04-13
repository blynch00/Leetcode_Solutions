# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def node_traversal(root, node_list):
            if root is None:
                return
            
            node_traversal(root.left, node_list)
            node_list.append(root.val)
            node_traversal(root.right, node_list)

        node_list = []
        node_traversal(root, node_list)
        return node_list
        