class Solution:
    def maxProfit(self, prices: List[int]) -> int:
   
        ma = 0
        mi = prices[0]
        for i in range(1,len(prices)):
            mi = min(mi,prices[i])
            if prices[i] > prices[i-1] :
                    
                ma = max(ma,prices[i]-mi)
        return ma