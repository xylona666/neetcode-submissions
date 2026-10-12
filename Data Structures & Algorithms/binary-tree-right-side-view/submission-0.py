# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # 思路错误了记得重新写
        if not root:
            return []
        self.res = []
        def dfs(node,level):
            if not node:
                return
            if len(self.res) == level :
                self.res.append(node.val)
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        dfs(root,0)   
        return self.res





















        # self.result = []
        # def dfs(node,level):
        #     if not node:
        #         return  
        #     else:
        #         if level == len(self.result):
        #             self.result.append(node.val)
        #         dfs(node.right,level+1)
        #         dfs(node.left,level+1)
        # dfs(root,0)
        # return self.result