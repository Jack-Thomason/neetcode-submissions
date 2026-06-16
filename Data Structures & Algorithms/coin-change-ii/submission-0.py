class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #top-down

        def count_rec(coins, n, count, dp):
            if count == 0:
                return 1
            if count < 0 or n == 0:
                return 0
            
            if dp[n-1][count] != -1:
                return dp[n-1][count]
            
            dp[n-1][count] = count_rec(coins, n, count - coins[n-1], dp) + count_rec(coins, n - 1, count, dp)

            return dp[n-1][count]
        
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        return count_rec(coins, len(coins), amount, dp)