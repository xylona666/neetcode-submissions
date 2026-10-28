class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        # 2 situations
        dp[0]= 0 # 从开始到当前值的cost
        dp[1]= 0
        
        for i in range(2,n+1):
            dp[i] = min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])  
       
    
        for i in range(3,n+1):
            dp[i] = min(dp[i],min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2]))
        
        return dp[n]