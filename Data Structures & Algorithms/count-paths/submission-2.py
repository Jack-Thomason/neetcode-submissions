class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom-up approach
        #dp[x] where x represents the current column value
        #value flows from above dp[x] and the left dp[x-1]

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(1, n):
                dp[j] += dp[j-1]
                
        return dp[n-1]

