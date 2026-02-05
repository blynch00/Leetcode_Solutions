from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        node_list  = []
        smallest_value = True
        self.traversal_helper(root, node_list)
    
        for x in range(1, len(node_list)):
            if smallest_value is True or node_list[x] - node_list[x-1] < smallest_value:
                smallest_value = node_list[x] - node_list[x-1]
        return smallest_value
    def traversal_helper(self, root:Optional[TreeNode], node_list:list) -> list:
        if root is None:
            return
        
        left_node = self.traversal_helper(root.left, node_list)

        node_list.append(root.val)
    
        right_node = self.traversal_helper(root.right, node_list)

        return node_list