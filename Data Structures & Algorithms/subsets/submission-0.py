class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        path = []
        def backtracking(start):
            self.result.append(path[:])
            
            for i in range(start,len(nums)): 
                path.append(nums[i])
                backtracking(i+1)  
                path.pop()
                
        backtracking(0)
        return self.result