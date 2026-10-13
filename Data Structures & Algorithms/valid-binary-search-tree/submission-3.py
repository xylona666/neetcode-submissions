class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node,low,high):
            if not node:
                return True
            if low<node.val<high:
                left = dfs(node.left,low,node.val)
                right = dfs(node.right,node.val,high)
                return left and right
            else:
                return False


        return dfs(root,float("-inf"),float("inf"))
