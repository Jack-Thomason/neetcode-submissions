class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, profit = 0, 0 

        for r in range(1, len(prices)):

            if prices[l] > prices[r]:
                l = r
            else:
                val = prices[r] - prices[l]
                profit = max(profit, val)
        
        return profit
        