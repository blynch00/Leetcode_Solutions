from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is not None and q is None) or (p is None and q is not None):
            return False
        if p is None and q is None:
            return True
        else:
            return (self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right))

sol=Solution()
