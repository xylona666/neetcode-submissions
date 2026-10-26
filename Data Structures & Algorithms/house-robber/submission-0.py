class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)       
        if n == 1:
            return nums[0]

        prev0 = nums[0]               # dp[0]
        prev1 = max(nums[0], nums[1]) # dp[1]

        

        for i in range(2,n):
            prev2 = max(prev1, prev0 + nums[i])
            prev0 = prev1
            prev1 = prev2
        return prev1
