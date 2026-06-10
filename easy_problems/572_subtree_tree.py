# Definition for a binary tree node.
from typing import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Def to test validity once subroot is found
        def is_valid(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            
            if not root and not subRoot:
                return True

            if (root and not subRoot) or (not root and subRoot):
                return False
            
            elif root.val != subRoot.val:
                return False
            
            else:
                return is_valid(root.left, subRoot.left) and is_valid(root.right, subRoot.right)
        
        # 1. Iterate through root until finding subroot
        # if it doesn't exist, i.e. we go left or right until None, return False
        # we can BFS the tree with a queue
        search_queue = deque()
        search_queue.append(root)

        while(search_queue):
            curr_node = search_queue.popleft()
            if curr_node is None:
                continue
            elif curr_node.val != subRoot.val:
                search_queue.append(curr_node.left) 
                search_queue.append(curr_node.right)

            else:
                if (is_valid(curr_node, subRoot)) is True:
                    return True
                else:
                    search_queue.append(curr_node.left) 
                    search_queue.append(curr_node.right)
                    
        return False
        # If the node is found, we recursively check left AND right until they are both None, returning
        #is_valid(root.left, subroot.left) AND is_valid(root.right, subroot.right)
