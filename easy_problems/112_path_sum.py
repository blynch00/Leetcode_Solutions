# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathHelper(root, targetSum, runningTotal=0) -> bool:
        # Because the nodes can be negative or positive, we must recursively travel to leaves and check the total path
            if root is None:
                return False
            
            if (root.left is None and root.right is None):
                if root.val + runningTotal == targetSum:
                    return True
                else:
                    return False
            else:
                return (pathHelper(root.left, targetSum, runningTotal + root.val) or pathHelper(root.right, targetSum, runningTotal + root.val))


        runningTotal = 0
        return pathHelper(root, targetSum, runningTotal)

        # Stores every route as node:path_value in dictionary for return calls.



        