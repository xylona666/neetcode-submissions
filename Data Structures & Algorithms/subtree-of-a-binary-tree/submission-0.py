# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isSametree(p,q):
            if not p and not q:
                return True
            elif p and not q:
                return False
            elif not p and q:
                return False
            if p.val == q.val:
                left = isSametree(p.left,q.left)
                right = isSametree(p.right,q.right)
                return left and right
            else:
                return False
  
        if isSametree(root,subRoot):
                return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 
            







        