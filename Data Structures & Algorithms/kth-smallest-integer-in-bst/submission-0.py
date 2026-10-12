# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 我的思路是dfs,  如果左边没有了,那就把自己append近result
        self.result = []
        def dfs(node):
            if not node:
                return
            if  node.left:
                dfs(node.left)
            self.result.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return self.result[k-1]