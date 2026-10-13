# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #重新写 !!!!
        if not root:
            return 0
        self.count = 0
        def dfs(node,maximum):
            if not node:
                return 
            if node.val>=maximum:
                self.count +=1
                maximum = node.val
            left = dfs(node.left,maximum)
            right = dfs(node.right,maximum)

  

        dfs(root,root.val)
        return self.count