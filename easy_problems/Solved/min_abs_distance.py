# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # Given the root of a Binary Search Tree (BST), return the minimum 
        # absolute difference between the values of any two different nodes in the tree.
        seen = []
        # In order traversal.

        answer = self.min_diff_helper(root, seen)
        return_int = -2
        for x in range(1,len(answer)):
            if (answer[x] - answer[x-1]) < return_int or return_int == -2:
                return_int = answer[x] - answer[x-1]
        return return_int

    def min_diff_helper (self, root: TreeNode, seen: set) -> int:
        if root is None:
            return 
        left_node = self.min_diff_helper(root.left, seen)

        
        seen.append(root.val)
        
        right_node = self.min_diff_helper(root.right, seen)

        return seen