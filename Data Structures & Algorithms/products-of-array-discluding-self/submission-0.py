class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        l = len(nums)
        prefix = [1] * l
        suffix = [1] * l 
        for i in range(1,l):
            prefix[i] = nums[i-1] * acc
            acc = prefix[i]
    
        acc = 1
        for j in range(l-2,-1,-1):
            suffix[j] = nums[j+1] * acc
            acc = suffix[j]
 
        result = []
        for i in range(l):
            result.append(prefix[i]*suffix[i])
        return result


