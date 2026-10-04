# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def sub(node):
            if not node:
                return 0
            left = sub(node.left) 
            right = sub(node.right) 
            if left == -1 or right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            return max(left,right)+1
        
        return sub(root) != -1
            