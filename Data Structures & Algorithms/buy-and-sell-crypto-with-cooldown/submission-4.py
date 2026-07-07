class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ahead1_notholding = 0
        ahead1_holding = 0
        ahead2_notholding = 0

        for i in range(len(prices) - 1, -1, -1):
            curr_notholding = max(ahead1_notholding, -prices[i] + ahead1_holding)
            curr_holding = max(ahead1_holding, prices[i] + ahead2_notholding)


            ahead2_notholding = ahead1_notholding
            ahead1_notholding = curr_notholding
            ahead1_holding = curr_holding

        return ahead1_notholding