class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # 我的问题: 1) left和right都得统计 
        #          2) 每次有两个选择所以不需要else
        self.result = []
        path = []
 
        def backtracking(n,count_right,count_left):
            if len(path) == 2*n:
                self.result.append("".join(path[:]))
                return
            if count_left < n:
                path.append("(")
           
                backtracking(n,count_right,count_left+1)
                path.pop()
                print(path,count_left)
            if count_right < count_left:
                path.append(")") #[((()]
                print(path)
                backtracking(n,count_right+1,count_left)
                path.pop()
 
        backtracking(n,0,0)
        return self.result
            
             

           
            
        