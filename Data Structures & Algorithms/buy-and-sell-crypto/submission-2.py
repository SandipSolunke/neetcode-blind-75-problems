class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        ans = 0
        min_price = prices[0]
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            ans = max(ans, prices[i]-min_price)
        
        return ans