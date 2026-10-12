# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxm = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right =depth(node.right)
            self.maxm = max(self.maxm,left+right)
            return max(left,right)+1
        depth(root)
       
        return  self.maxm
