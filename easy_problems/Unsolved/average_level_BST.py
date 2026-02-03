from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if root is None:
            return []
        node_queue = deque()
        node_queue.append(root)
        values = []

        return values