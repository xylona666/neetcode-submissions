class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                minimum = min(minimum,prices[i]) # 最小值
            else:
                profit = max(profit,prices[i] - minimum)
        return profit
