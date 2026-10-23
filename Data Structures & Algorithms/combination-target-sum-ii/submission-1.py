class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() #[1,2,2,4,5,6,9]
        self.result= []
        path =[]
        def backtracking(start, numm):
            
            if numm == target:
                self.result.append(path[:])
                return
            for i in range(start,len(candidates)):
                if numm > target:
                    return
                if i> start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                numm += candidates[i]
                backtracking(i+1, numm)
                path.pop()
                numm -= candidates[i]
        backtracking(0,0)
        return self.result

