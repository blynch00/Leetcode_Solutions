class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # Will use dynamic programming
    
        def check_path(root, total, goal):
            if root is None:
                return False
            if (root.val + total) > goal:
                return False
            if (root.val + total) == goal:
                if root.left is None and root.right is None:
                    return True
            

            total += root.val
            return True and (check_path(root.left, total, goal) or check_path(root.right, total, goal))

        final_value = check_path(root, 0, targetSum)
        return final_value