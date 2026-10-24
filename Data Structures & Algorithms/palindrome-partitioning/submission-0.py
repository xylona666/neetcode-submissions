class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #  递归 start用for loop, end用递归
        self.result = []
        path = []
        def ifPalindrome(string):
            left = 0
            right= len(string)-1
            while left<right:
                if string[left] == string[right]:
                    left+=1
                    right -=1
                else:
                    return False
            return True
        # find whether each substring is ifPalindrome
        #我需要确定每一段都是substring不然就break
        def backtracking(start):
            if len("".join(path)) == len(s):
                self.result.append(path[:])
                return
            for i in range(start,len(s)): # 当前开始的是这一层start = 0 , i = 0, 
                if ifPalindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    print(path)
                    backtracking(i+1)
                    path.pop()
                
                
        backtracking(0)
        return self.result










