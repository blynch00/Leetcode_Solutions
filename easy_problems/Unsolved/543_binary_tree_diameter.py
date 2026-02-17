# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    def dfs(self, root:Optional[TreeNode], max_distance:int) -> int:
        if root is None:
            return 0
        
        left_node = self.dfs(root.left)
        right_node = self.dfs(root.right)

        current_max = left_node + right_node

        max_distance = max(max_distance, current_max)

        return 1+ max(current_max)

node_5 = TreeNode(5, None, None)
node_4 = TreeNode(4, None, None)
node_3 = TreeNode(3, node_4, node_5)
node_2 = TreeNode(2, None, None)   
node_1 = TreeNode(1, node_2, node_3)

sol = Solution()
print(sol.diameterOfBinaryTree(node_1))