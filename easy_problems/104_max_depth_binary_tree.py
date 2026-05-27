# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper_max(root) -> int:
            if root is None:
                return 0
            # determine if we can go lower, returning total sum
            if root.left is None and root.right is None:
                return 1
            
            else:
                if root.right is None and root.left is not None:
                    return 1 + helper_max(root.left)
                elif root.left is None and root.right is not None:
                    return 1 + helper_max(root.right)
                else:
                    # both left and right have nodes:
                    return 1 + max(helper_max(root.right), helper_max(root.left))
        
        return helper_max(root)