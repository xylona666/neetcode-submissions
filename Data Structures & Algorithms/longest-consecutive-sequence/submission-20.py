class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 找当前的值是不是最小的,如果是开始找后面的,不是的continue
        nums_set = set(nums)# [2,20,4,10,3,5]
        maxCount = 0
        count = 1
        for i in nums_set:
            if i-1 not in nums_set:
                while i+1 in nums_set:
                    count +=1
                    i += 1
                else:
                    maxCount = max(maxCount,count)
                    count = 1    
        return maxCount