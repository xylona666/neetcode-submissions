class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result =[]
        path = []
        def backtracking(start,numm):
           
            if numm > target: #有个问题,如果超了怎么才能中断这层的尝试,break掉
                return
            if numm == target:
                self.result.append(path[:])
                return
            for i in range(start,len(nums)):
                numm += nums[i]
                path.append(nums[i])
    
                backtracking(i,numm)
                numm -= nums[i]
                path.pop()
        backtracking(0,0)
        return self.result
