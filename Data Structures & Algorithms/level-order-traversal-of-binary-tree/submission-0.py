# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # deque的方法重写一遍
        # 中左右,两种方法都写一遍
        if not root:
            return []
        quene = deque([root])
        result = []
 
        while quene:
            level = []
            for _ in range(len(quene)):
                cur = quene.popleft() # node:1
                level.append(cur.val)
                if cur.left:
                    quene.append(cur.left)
                if cur.right:
                    quene.append(cur.right)
            result.append(level)
        return result